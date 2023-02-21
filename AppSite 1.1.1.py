# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 23:08:28 2021

@author: yan-s
"""
import os, sys
from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
from PIL import ImageTk,Image
from resizeimage import resizeimage
from shutil import move, rmtree
from random import choice
from time import strftime, ctime
from webbrowser import open_new_tab
from string import ascii_letters

#---| Class popup |------------------------------#

class popup:
    def __init__(self, parent,typ):
        showinfo('Aide', 'Entrez un'+typ+' !' )
        top = self.top = Toplevel(parent)
        self.top.wm_title('Zone de Texte')
        self.top.geometry("350x475")
        self.top.config(bg='#e3e3e3')
        self.top.columnconfigure(0,weight=1)
        self.top.rowconfigure(0,weight=3)
        self.top.rowconfigure(1,weight=1)
        
        self.TextBox = Text(top, width= 70)
        self.TextBox.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.mySubmitButton = Button(top, text="Ok", command=self.send)
        self.mySubmitButton.grid(column=0,row=1,sticky='EWNS',padx=5,pady=5)

    def send(self):
        global varText
        varText = self.TextBox.get(1.0, END+"-1c")
        self.top.destroy()
        
class popup_header:
    def __init__(self, parent,typ):
        showinfo('Aide', 'Entrez les '+typ+' !' )
        top = self.top = Toplevel(parent)
        self.top.wm_title('Zone de Texte')
        self.top.geometry("350x475")
        self.top.config(bg='#e3e3e3')
        self.top.columnconfigure(0,weight=1),self.top.columnconfigure(1,weight=3)
        self.top.rowconfigure(0,weight=1),self.top.rowconfigure(1,weight=1)
        self.top.rowconfigure(2,weight=1),self.top.rowconfigure(3,weight=1)
        self.top.rowconfigure(4,weight=1)
        
        self.mylabel0 = Label(top,text='Titre de haut de page (la date peut suffire): ')
        self.mylabel0.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry0 = Entry(top)
        self.myEntry0.grid(column =1, row = 0,padx=5,pady=5,ipady=10)
        
        self.mylabel1 = Label(top,text='Titre du post : ')
        self.mylabel1.grid(column =0, row = 1,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry1 = Entry(top)
        self.myEntry1.grid(column =1, row = 1,padx=5,pady=5,ipady=10)
        
        self.mylabel2 = Label(top,text='Sous-titre du post : ')
        self.mylabel2.grid(column =0, row = 2,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry2 = Entry(top)
        self.myEntry2.grid(column =1, row = 2,padx=5,pady=5,ipady=10)
        
        self.mylabel3 = Label(top,text='Votre nom : ')
        self.mylabel3.grid(column =0, row = 3,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry3 = Entry(top)
        self.myEntry3.grid(column =1, row = 3,padx=5,pady=5,ipady=10)
        
        self.mySubmitButton = Button(top, text="Ok", command=self.send_header)
        self.mySubmitButton.grid(column=0,row=4,columnspan=2,sticky='EWNS',padx=5,pady=5)
        
    def send_header(self):
        global varText,varText1,varText2,varText3 
        varText = self.myEntry0.get()
        varText1 = self.myEntry1.get()
        varText2 = self.myEntry2.get()
        varText3 = self.myEntry3.get()
        self.top.destroy()
 
class popup_img:
    def __init__(self, parent,typ):
        showinfo('Aide', 'Entrez les informations de '+typ+' !' )
        top = self.top = Toplevel(parent)
        self.top.wm_title('Zone de Texte')
        self.top.geometry("450x375")
        self.top.config(bg='#e3e3e3')
        self.top.columnconfigure(0,weight=1),self.top.columnconfigure(1,weight=3)
        self.top.rowconfigure(0,weight=1),self.top.rowconfigure(1,weight=1)
        self.top.rowconfigure(2,weight=1)
        
        self.mylabel0 = Label(top,text='Entrez une description courte de l\'image (ne se verra pas) : ')
        self.mylabel0.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry0 = Entry(top)
        self.myEntry0.grid(column =1, row = 0,padx=5,pady=5,ipady=10)
        
        self.mylabel1 = Label(top,text='Entrez la description de l\'image : ')
        self.mylabel1.grid(column =0, row = 1,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry1 = Entry(top)
        self.myEntry1.grid(column =1, row = 1,padx=5,pady=5,ipady=10)
        
        self.mySubmitButton = Button(top, text="Ok", command=self.send_img)
        self.mySubmitButton.grid(column=0,row=2,columnspan=2,sticky='EWNS',padx=5,pady=5)

    def send_img(self):
        global varText,varText1,varText2
        varText = self.myEntry0.get()
        varText1 = self.myEntry1.get()
        self.top.destroy()

 
class popup_lien:
    def __init__(self, parent,typ):
        showinfo('Aide', 'Entrez les informations du '+typ+' !' )
        top = self.top = Toplevel(parent)
        self.top.wm_title('Zone de Texte')
        self.top.geometry("350x475")
        self.top.config(bg='#e3e3e3')
        self.top.columnconfigure(0,weight=1),self.top.columnconfigure(1,weight=3)
        self.top.rowconfigure(0,weight=1),self.top.rowconfigure(1,weight=1)
        self.top.rowconfigure(2,weight=1),self.top.rowconfigure(3,weight=1)
        self.top.rowconfigure(4,weight=1)
        
        self.mylabel0 = Label(top,text='Entrez votre texte : ')
        self.mylabel0.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry0 = Entry(top)
        self.myEntry0.grid(column =1, row = 0,padx=5,pady=5,ipady=10)
        
        self.mylabel1 = Label(top,text='Nom du lien (Obligatoire): ')
        self.mylabel1.grid(column =0, row = 1,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry1 = Entry(top)
        self.myEntry1.grid(column =1, row = 1,padx=5,pady=5,ipady=10)
        
        self.mylabel2 = Label(top,text='Entrez votre lien (ex: http://ile-segal.com/) : ')
        self.mylabel2.grid(column =0, row = 2,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry2 = Entry(top)
        self.myEntry2.grid(column =1, row = 2,padx=5,pady=5,ipady=10)
        
        self.mylabel0 = Label(top,text='Entrez votre texte  : ')
        self.mylabel0.grid(column =0, row = 3,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry0 = Entry(top)
        self.myEntry0.grid(column =1, row = 3,padx=5,pady=5,ipady=10)
        
        self.mySubmitButton = Button(top, text="Ok", command=self.send_lien)
        self.mySubmitButton.grid(column=0,row=4,columnspan=2,sticky='EWNS',padx=5,pady=5)

    def send_lien(self):
        global varText,varText1,varText2
        varText = self.myEntry0.get()
        varText1 = self.myEntry1.get()
        varText2 = self.myEntry2.get()
        self.top.destroy()
        
class popup_export:
    def __init__(self, parent,typ):
        showinfo('Aide', 'Entrez le'+typ+' !' )
        top = self.top = Toplevel(parent)
        self.top.wm_title('Zone de Texte')
        self.top.geometry("300x150")
        self.top.config(bg='#e3e3e3')
        self.top.columnconfigure(0,weight=1),self.top.columnconfigure(1,weight=1)
        self.top.rowconfigure(0,weight=1),self.top.rowconfigure(1,weight=1)
        
        self.mylabel0 = Label(top,text='Entrez votre texte : ')
        self.mylabel0.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS',ipady=10)
        self.myEntry0 = Entry(top)
        self.myEntry0.grid(column =1, row = 0,padx=5,pady=5,ipady=10)
    
        
        self.mySubmitButton = Button(top, text="Ok", command=self.send_export)
        self.mySubmitButton.grid(column=0,row=1,columnspan=2,sticky='EWNS',padx=5,pady=5)

    def send_export(self):
        global varText
        varText=''
        varText = self.myEntry0.get()
        self.top.destroy()

#---| Var Global |--------------------------------#
   
erreur=0
frame=int
projet = 0
varText = ''
varText1 = ''
varText2 = ''
varText3 = ''
dir_ch_dir = 0
fullScreenState = False   

#---| Balise |------------------------------------#

def header():
    global erreur
    showinfo('Aide', 'Séléctionnez une image pour commencer ! ' )
    name_alea = (''.join((choice(ascii_letters) for _ in range(8))))
    fenetre.filename =  filedialog.askopenfilename(title = "Sélectionnez un dossier",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))           
    try:
        with open(fenetre.filename, 'r+b') as ff :
            with Image.open(ff) as image:
                widht, height = image.size
                if(widht >= 1900 and height >= 600):
                    #exp
                    cover = resizeimage.resize_cover(image, [1900, 600])
                    cover.save('exp/img/head_p/'+name_alea+ 'head.webp')
                    cover = resizeimage.resize_cover(image, [1900, 600])
                    cover.save('exp/img/w-head_p/'+name_alea+ 'head.jpg')
                    #temp
                    cover = resizeimage.resize_cover(image, [1900, 600])
                    cover.save('temp/img/'+name_alea+ 'head.webp')
                    cover = resizeimage.resize_cover(image, [1900, 600])
                    cover.save('temp/img/'+name_alea+ 'head.jpg')
                elif(widht >= 950 and height >= 300):
                    #exp
                    cover = resizeimage.resize_cover(image, [950, 300])
                    cover.save('exp/img/head_p/'+name_alea+ 'head.webp')
                    cover = resizeimage.resize_cover(image, [950, 300])
                    cover.save('exp/img/w-head_p/'+name_alea+ 'head.jpg')
                    #temp
                    cover = resizeimage.resize_cover(image, [950, 300])
                    cover.save('temp/img/'+name_alea+ 'head.webp')
                    cover = resizeimage.resize_cover(image, [950, 300])
                    cover.save('temp/img/'+name_alea+ 'head.jpg')
                else:
                    trop_petite_b() 
                    
        with open(fenetre.filename, 'r+b') as f :
            with Image.open(f) as image:
                widht, height = image.size
                if(widht >= 306 and height >= 230):
                    #exp
                    cover = resizeimage.resize_cover(image, [306, 230])
                    cover.save('exp/img/av/'+name_alea+ 'av.webp')
                    cover = resizeimage.resize_cover(image, [306, 230])
                    cover.save('exp/img/w-av/'+name_alea+ 'av.jpg')                 
                else:
                    pass
        
        high_title = ''
        title = ''
        subtitle = ''
        autor = ''
        while high_title == '' or title == '' or subtitle == '' or autor == '':
            inputDialog = popup_header(fenetre,"données")
            fenetre.wait_window(inputDialog.top)
            high_title= varText
            title= varText1
            subtitle= varText2
            autor= varText3
            if high_title == '' or title == '' or subtitle == '' or autor == '':
                if askyesno("Erreur", "Laisser une case vide ?"):
                    break
                else :
                    pass
                
        date= strftime('%d/%m/%y')   
        frame_f(1)

        with open('temp/' + 'post.html','w') as fichier:    #temp
            bootstrap_css='../.needs/bootstrap.min.css'
            clean_blog='../.needs/clean-blog.min.css'
            img='img/'+name_alea+'head.webp'
            fichier.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>Île-Segal - %s</title>
    
    <!-- Bootstrap Core CSS -->
    <link href="%s" rel="stylesheet">
    
    <!-- Theme CSS -->
    <link href="%s" rel="stylesheet">
    
    <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-custom navbar-fixed-top">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    Menu <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand" href="../index">< Précédent</a>
                <a class="navbar-brand" href="../index">Suivant ></a>
            </div>
    
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="../index">Home</a>
                    </li>
                    <li>
                        <a href="../contact">Contact</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>
    
    <!-- Page Header -->
    <!-- Set your background image for this header on the line below. -->
    <header class="intro-header" style="background-image: url('%s')">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                    <div class="post-heading">
                        <h1>%s</h1>
                        <h2 class="subheading">%s</h2>
                        <span class="meta">Post par <a href="#">%s</a> le %s</span>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    <!-- Post Content -->
    <article>
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">"""% (high_title,bootstrap_css,clean_blog,img,title,subtitle,autor,date))                

        with open('exp/post/' + 'post.html','w') as fichier:   #exp-webp
            bootstrap_css='../../css/post/bootstrap.min.css'
            clean_blog='../../css/post/clean-blog.min.css'
            img='../../img/head_p/'+name_alea+'head.webp'
            fichier.write("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Île-Segal - %s</title>

<!-- Bootstrap Core CSS -->
<link href="%s" rel="stylesheet">

<!-- Theme CSS -->
<link href="%s" rel="stylesheet">

<link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
</head>

<body>

<!-- Navigation -->
<nav class="navbar navbar-default navbar-custom navbar-fixed-top">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header page-scroll">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                <span class="sr-only">Toggle navigation</span>
                Menu <i class="fa fa-bars"></i>
            </button>
            <a class="navbar-brand" href="../index">< Précédent</a>
            <a class="navbar-brand" href="../index">Suivant ></a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav navbar-right">
                <li>
                    <a href="../index">Home</a>
                </li>
                <li>
                    <a href="../contact">Contact</a>
                </li>
            </ul>
        </div>
        <!-- /.navbar-collapse -->
    </div>
    <!-- /.container -->
</nav>

<!-- Page Header -->
<!-- Set your background image for this header on the line below. -->
<header class="intro-header" style="background-image: url('%s')">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                <div class="post-heading">
                    <h1>%s</h1>
                    <h2 class="subheading">%s</h2>
                    <span class="meta">Post par <a href="#">%s</a> le %s</span>
                </div>
            </div>
        </div>
    </div>
</header>

<!-- Post Content -->
<article>
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">"""% (high_title,bootstrap_css,clean_blog,img,title,subtitle,autor,date))                

    except IOError:
        if erreur > 1:
            erreur_h()
        else:
            erreur +=1
            erreur_img_header()  

def titre_de_partie():
    txt_part = ''
    while txt_part == '':
        inputDialog = popup_export(fenetre," titre de partie")
        fenetre.wait_window(inputDialog.top)
        txt_part = varText
        if txt_part == '':
            if askyesno("Erreur", "Quitter ?"):
                break
            else :
                pass
        else:    
            with open('temp/' + 'post.html','a') as fichier:    #temp
                fichier.write("""
                    <h2 class="section-heading">%s</h2>\n"""% (txt_part))
                    
            with open('exp/post/' + 'post.html','a') as fichier:    #exp
                fichier.write("""
            <h2 class="section-heading">%s</h2>\n"""% (txt_part))

def resize_and_crop():
    global erreur
    showinfo('Aide', 'Séléctionnez une image ! ' )
    fenetre.filename =  filedialog.askopenfilename(title = "Sélectionnez un dossier",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    name_alea = (''.join((choice(ascii_letters) for _ in range(8))))    
    try:
        with open(fenetre.filename, 'r+b') as f:
            with Image.open(f) as image:
                widht, height = image.size
                if(widht >= 778 and height >= 514):
                    #exp
                    cover = resizeimage.resize_cover(image, [778, 514])
                    cover.save('exp/img/post/'+name_alea+ '.webp')
                    cover = resizeimage.resize_cover(image, [778, 514])
                    cover.save('exp/img/w-post/'+name_alea+ '.jpg')
                    #temp
                    cover = resizeimage.resize_cover(image, [778, 514])
                    cover.save('temp/img/'+name_alea+ '.webp')
                    cover = resizeimage.resize_cover(image, [778, 514])
                    cover.save('temp/img/'+name_alea+ '.jpg')
                    
                    inputDialog = popup_img(fenetre,"l\'image")
                    fenetre.wait_window(inputDialog.top)
                    descrp= varText
                    descrp_c= varText1
                       
                    with open('temp/' + 'post.html','a') as fichier:    #temp
                        fichier.write("""  
                    <a href="#">
                        <img class="img-responsive" src="%s" alt="%s">
                    </a>
                    <span class="caption text-muted">%s</span>\n                      
                      """% (('img/'+name_alea+'.webp'),descrp,descrp_c))
                       
                    with open('exp/post/' + 'post.html','a') as fichier:    #exp
                        fichier.write("""  
                    <a href="#">
                        <img class="img-responsive" src="%s" alt="%s">
                    </a>
                    <span class="caption text-muted">%s</span>\n                      
                      """% (('../../img/post/' +name_alea+'.webp'),descrp,descrp_c))  
                else:
                    trop_petite() 
    except IOError:
        if erreur > 1:
            erreur_r()
        else:
            erreur +=1
            erreur_img()
         
def texte():
    txt = ''
    while txt == '':
        inputDialog = popup(fenetre," texte")
        fenetre.wait_window(inputDialog.top)
        txt = varText
        if txt == '':
            if askyesno("Erreur", "Quitter ?"):
                break
            else :
                pass
        else:        
            with open('temp/' + 'post.html','a') as fichier:    #temp
                fichier.write("""
                    <p>%s</p>\n"""% (txt))
                    
            with open('exp/post/' + 'post.html','a') as fichier:    #exp
                fichier.write("""
                    <p>%s</p>\n"""% (txt))

def quote():
    txt_q = ''    
    while txt_q == '':
        inputDialog = popup(fenetre,"e citation")
        fenetre.wait_window(inputDialog.top)
        txt_q = varText
        if txt_q == '':
            if askyesno("Erreur", "Quitter ?"):
                break
            else :
                pass
        else:       
            with open('temp/' + 'post.html','a') as fichier:    #temp
                fichier.write("""
                    <blockquote>%s</blockquote>\n"""% (txt_q))
                    
            with open('exp/post/' + 'post.html','a') as fichier:    #exp
                fichier.write("""
                    <blockquote>%s</blockquote>\n"""% (txt_q))
                      
def lien():
    
    txt_l= ''
    n_l= ''
    lien= ''
    while txt_l == '' or n_l == '' or lien == '':
        inputDialog = popup_lien(fenetre,"lien")
        fenetre.wait_window(inputDialog.top)
        txt_l= varText
        n_l= varText1
        lien= varText2
        if txt_l == '' or n_l == '' or lien == '':
            if askyesno("Erreur", "Laisser une case vide ?"):
                with open('temp/' + 'post.html','a') as fichier:    #temp
                    fichier.write("""
                    <!-- Lien autre site -->
                    <p>%s <a href="%s">%s</a>.</a></p>\n"""% (txt_l,lien,n_l))
                        
                with open('exp/post/' + 'post.html','a') as fichier:    #exp
                    fichier.write("""
                    <!-- Lien autre site -->
                    <p>%s <a href="%s">%s</a>.</a></p>\n"""% (txt_l,lien,n_l)) 
                break
            else :
                if askyesno("Erreur", "Quitter ?"):
                    break
                else:
                    pass                    
        else:     
            with open('temp/' + 'post.html','a') as fichier:    #temp
                fichier.write("""
                    <!-- Lien autre site -->
                    <p>%s <a href="%s">%s</a>.</a></p>\n"""% (txt_l,lien,n_l))
                    
            with open('exp/post/' + 'post.html','a') as fichier:    #exp
                fichier.write("""
                    <!-- Lien autre site -->
                    <p>%s <a href="%s">%s</a>.</a></p>\n"""% (txt_l,lien,n_l))                     
                            
def footer():
    with open('exp/post/' + 'post.html','a') as fichier:    #exp
        jQuery='../../js/jquery/jquery.min.js'
        bootstrap_js='../../js/post/bootstrap.min.js'
        clean_js='../../js/post/clean-blog.min.js'
        fichier.write("""
             </div>
        </div>
    </div>
</article>
          
<hr>

<!-- Footer -->
<footer>
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                <ul class="list-inline text-center">
                    <li>
                        <a href="#">
                            <span class="fa-stack fa-lg">
                                <i class="fa fa-circle fa-stack-2x"></i>
                                <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <span class="fa-stack fa-lg">
                                <i class="fa fa-circle fa-stack-2x"></i>
                                <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <span class="fa-stack fa-lg">
                                <i class="fa fa-circle fa-stack-2x"></i>
                                <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                    </li>
                </ul>
                <p class="copyright text-muted">Copyright &copy; Île-Segal 2020</p>
            </div>
        </div>
    </div>
</footer>

<!-- jQuery -->
<script src="%s"></script>

<!-- Bootstrap Core JavaScript -->
<script src="%s"></script>
<!-- Theme JavaScript -->
<script src="%s"></script>

</body>
</html>"""% (jQuery,bootstrap_js,clean_js))

#---| Erreurs |-----------------------------------#

def oups(message):
    showinfo('Oups...',message)

def erreur_h():
    global erreur    
    if askyesno("Erreur", "Erreur lors de l\'ouverture de l\'image ! Quitter le processus ?"):
        frame_f(0)
        erreur=0
        rmtree('temp/'), rmtree('exp/')
    else:
        header()
        
def erreur_r():
    global erreur    
    if askyesno("Erreur", "Erreur lors de l\'ouverture de l\'image ! Quitter le processus ?"):
        erreur=0
    else:
        resize_and_crop()
        
def trop_petite():
    showwarning('Erreur', 'Image trop petite pour être redimensionnée ! Les dimensions minimales sont 778 x 514px.' )
    resize_and_crop()

def trop_petite_b():
    showwarning('Erreur', 'Image trop petite pour être redimensionnée ! Les dimensions minimales sont 950 x 300px, les optimales sont 1900 x 600px.' )
    header()

def erreur_img_header():
    showerror('Erreur', 'Erreur lors de l\'ouverture de l\'image ! ')
    header()
    
def erreur_img():
    showerror('Erreur', 'Erreur lors de l\'ouverture de l\'image ! ')
    resize_and_crop()   

#def alert():
    #showinfo("Désolé", "Pas encore configuré... ")

#---| Script |------------------------------------#  
  
def quit():
    if askyesno("Quitter", "Êtes-vous sûr de vouloir quitter l'application ?"):
        fenetre.destroy()
        
def restart():
    if askyesno("Quitter", "Êtes-vous sûr de vouloir relancer l'application ?"):
        fenetre.destroy()
        sys.stdout.flush()
        os.execv(sys.argv[0], sys.argv)
        
def aide():
    change_dir('.needs/')
    open_new_tab('aide.html')
    dir_change()
    
def ouvrir_projet ():
    if os.path.exists('exp/') and os.path.exists('temp/'):
        frame_f(1)
    else:
        showerror("Erreur", "Créez d\'abord un projet ! ")    
    
def apercu_web():
    global dir_ch_dir
    dir_ch_dir = 0
    change_dir('temp/')
    if dir_ch_dir == 0:
        open_new_tab('post.html')
    dir_change()
    
def exporter():
    if not os.path.isdir('exp'):
        showerror("Erreur", "Projet inexistant ! ")
    else:            
        if askyesno('Exporter','Attention ! Opération irréversible, soyez sûr de n\'avoir rien oublié. Êtes-vous sûr de vouloir continuer ?'):
            drc = ''
            inputDialog = popup_export(fenetre," nom du fichier")
            fenetre.wait_window(inputDialog.top)
            drc = varText
            if drc!='':                 
                dossier_exp = filedialog.askdirectory(title="Sélectionnez un dossier",mustexist=True,parent=fenetre)
                if dossier_exp != '' :   
                    try:
                        if os.path.isfile('exp/'):
                            os.remove('temp/post.html')
                        if os.path.exists('temp/'):
                            rmtree('temp/')
                    except:
                        oups('Vous avez un aperçu d\'ouvert, fermé le pour procéder !')
                    else:   
                        footer()
                        os.rename('exp', drc)                        
                        dossier_src = drc
                        move(dossier_src, dossier_exp)
                        try:
                            rmtree('temp/')
                        except:
                            pass
                        frame_f(0)
                        showinfo('Exporté','Opération réussie !' )
                else:
                    oups('Vous devez séléctioner un dossier !')
            else:
                oups('Vous avez oublié de définir un nom pour le dossier !')
                exporter()
        else:
            pass
        
def change_dir(Npath):
   global dir_ch_dir
   try:
       os.chdir(Npath)
   except OSError:
       dir_ch_dir += 1
       showwarning("Erreur", "Vous devez d'abord créer un nouveau projet !")               
        
def dir_change():
    try:
        os.chdir('../')
    except OSError:
        showerror("Erreur", "Il y a un problème... et ce n'est pas censé arriver")               
    
def der_modif():
    change_dir('exp/post/')
    showinfo("Dernière modification : ", ctime((os.path.getmtime("post.html"))))
    dir_change()
    dir_change()
    
def existe():
    global projet
    if askyesno('Dossier déjà existant','Un projet existe déjà, voulez-vous le supprimer ?'):
        if os.path.exists('exp/'):
            rmtree('exp/')
        if os.path.exists('temp/') :
            rmtree('temp/')
    else:
        projet =+1
 
def frame_f(int):
    global frame
    if int==0:
        fram_e.grid_forget()
    else:
        fram_e.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS',ipady=10)
    if int == 1:
        frame_accueil.grid_forget()
    else:
        frame_accueil.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS')
   
 
#---| Raccourcis clavier |-------------------------#   
            
def plein(event):
    global fullScreenState
    fullScreenState = not fullScreenState
    fenetre.attributes('-fullscreen',fullScreenState)
    
def q_plein(event):
    global fullScreenState
    fullScreenState = False
    fenetre.attributes('-fullscreen',fullScreenState)
    
def new(event):
     nouveau()
     
def quit_r(event):
    quit()
    
def open_r(event):
    ouvrir_projet()
    
def exporter_r(event):
    exporter()
    
def aide_r(event):
    aide()
    
def apercu_r(event):
    apercu_web()
    
#---| Séquence de lancement |----------------------#
        
def nouveau():
    global projet
    projet= 0
    if os.path.exists('exp/') or os.path.exists('temp/'):
        existe()
        if projet == 0:
            os.makedirs('temp/img')
            os.makedirs('exp/post'),os.makedirs('exp/img/head_p'),os.makedirs('exp/img/w-head_p'),os.makedirs('exp/img/post'),os.makedirs('exp/img/w-post'),os.makedirs('exp/img/av'),os.makedirs('exp/img/w-av')
            header()                     
    else:     
        os.makedirs('temp/img')
        os.makedirs('exp/post'),os.makedirs('exp/img/head_p'),os.makedirs('exp/img/w-head_p'),os.makedirs('exp/img/post'),os.makedirs('exp/img/w-post'),os.makedirs('exp/img/av'),os.makedirs('exp/img/w-av')
        header()
             
#---| Mise en place fenetre |-----------------------# 
         
fenetre = Tk()
#fenetre.option_add('*Font', 'BASKVILL') #<-- régler taille
fenetre.wm_iconbitmap('favicon.ico')
fenetre.wm_title('AppSite 1.1.1')
fenetre.attributes('-fullscreen',False)
fenetre.bind('<Control-F11>',plein)
fenetre.bind('<Control-n>',new)
fenetre.bind('<Control-o>',open_r)
fenetre.bind('<Control-e>',exporter_r)
fenetre.bind('<Control-h>',aide_r)
fenetre.bind('<Control-d>',apercu_r)
fenetre.bind('<Control-F12>',quit_r)
fenetre.geometry('550x550')
fenetre.config(bg='#e3e3e3')    #f7ef38

#Menu
menubar = Menu(fenetre)
#Menu 1
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouveau projet", command=nouveau)
menu1.add_command(label="Ouvrir", command=ouvrir_projet)
menu1.add_separator()
#menu1.add_command(label="Enregistrer", command=alert)
#menu1.add_command(label="Enregistrer sous...", command=alert)
#menu1.add_separator()
menu1.add_command(label="Relancer", command=restart)
menu1.add_command(label="Quitter", command=quit)
menubar.add_cascade(label="Fichier", menu=menu1)
#Menu 2
menu2 = Menu(menubar, tearoff=0)
#menu2.add_command(label="Annuler", command=alert)
#menu2.add_command(label="Refaire", command=alert)
#menu2.add_separator()
menu2.add_command(label="Aperçu web", command=apercu_web)
menu2.add_command(label="Exporter", command=exporter)
menubar.add_cascade(label="Editer", menu=menu2)
#Menu 3
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Dernière modification", command=der_modif)
menu3.add_command(label="A propos", command=aide)
menubar.add_cascade(label="Aide", menu=menu3)

#Fenetre Grid
fenetre.columnconfigure(0,weight=1)
fenetre.rowconfigure(0,weight=1)

#Fram_e : élément
fram_e = LabelFrame(fenetre,text='Éléments : ',relief=FLAT,bg='#5073FB',bd=1,fg='white')
fram_e.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS',ipady=10)
#colonne
fram_e.columnconfigure(0,weight=2),fram_e.columnconfigure(1,weight=1)
#ligne
fram_e.rowconfigure(0,weight=1),fram_e.rowconfigure(1,weight=1)
fram_e.rowconfigure(2,weight=1),fram_e.rowconfigure(3,weight=1)
fram_e.rowconfigure(4,weight=1),fram_e.rowconfigure(5,weight=1)
#Widget
Label(fram_e, text='Titre de partie :').grid(column=0,row=0,padx=5,sticky='EWNS')
Button(fram_e, text='Nouveau', command=titre_de_partie).grid(column=1,row=0,sticky='EWNS')
Label(fram_e, text='Texte :').grid(column=0,row=1,padx=5,sticky='EWNS')
Button(fram_e, text='Nouveau', command=texte).grid(column=1,row=1,sticky='EWNS',pady=5)
Label(fram_e, text='Image :').grid(column=0,row=2,padx=5,sticky='EWNS')
Button(fram_e, text='Nouvelle', command=resize_and_crop).grid(column=1,row=2,sticky='EWNS')
Label(fram_e, text='Citation :').grid(column=0,row=3,padx=5,sticky='EWNS')
Button(fram_e, text='Nouvelle', command=quote).grid(column=1,row=3,sticky='EWNS',pady=5)
Label(fram_e, text='Lien :').grid(column=0,row=4,padx=5,sticky='EWNS')
Button(fram_e, text='Nouveau', command=lien).grid(column=1,row=4,sticky='EWNS')
Button(fram_e, text='Exporter', command=exporter).grid(column=0,row=5,sticky='EWNS',pady=5,padx=5)
Button(fram_e, text='Aperçu', command=apercu_web).grid(column=1,row=5,sticky='EWNS',pady=5)

#frame_accueil : Accueil
frame_accueil = LabelFrame(fenetre,text='',relief=RIDGE,bg='#f7ef38',bd=3)
frame_accueil.grid(column =0, row = 0,padx=5,pady=5,sticky='EWNS')
#colonne
frame_accueil.columnconfigure(0,weight=1),frame_accueil.columnconfigure(1,weight=2)
#ligne
frame_accueil.rowconfigure(0,weight=9),frame_accueil.rowconfigure(1,weight=1)
frame_accueil.rowconfigure(2,weight=1),frame_accueil.rowconfigure(3,weight=1)
frame_accueil.rowconfigure(4,weight=1),frame_accueil.rowconfigure(5,weight=1)
frame_accueil.rowconfigure(6,weight=1)
#Widget
img_accueil=Image.open("AppSite.png")
photo=ImageTk.PhotoImage(img_accueil)
img_acc=Label(frame_accueil,image=photo).grid(column=0,row=0,columnspan=2,padx=10)
Button(frame_accueil, text='Aide', command=aide).grid(column=0,row=4,sticky='EWNS',columnspan=2,padx=5,pady=5)
Button(frame_accueil, text='Ouvrir', command=ouvrir_projet).grid(column=0,row=5,sticky='EWNS',columnspan=2,padx=5,pady=5)
Button(frame_accueil, text='Nouveau Projet', command=nouveau).grid(column=0,row=6,sticky='EWNS',columnspan=2,padx=5,pady=5)

if os.path.exists('exp/') and os.path.exists('temp/'):
    frame_f(1)
else:
    frame_f(0)
fenetre.config(menu=menubar)
fenetre.mainloop()