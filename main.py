# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:11:03 2021

@author: yan-s
"""

from kivy.config import Config
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

import os, sys
from PIL import Image
from random import choice
from time import strftime
from shutil import move, rmtree
from string import ascii_letters
from resizeimage import resizeimage
from webbrowser import open_new_tab


screenEntry = int
imgPath = str

class StartWindow(Screen):
    def entry(self, int):
        global screenEntry
        screenEntry = int
        
    def start(self):
        if os.path.exists('exp/') or os.path.exists('temp/'):
            self.manager.current = 'Menu'
            self.manager.transition.direction = "up"
        else:     
            os.makedirs('temp/img')
            os.makedirs('exp/post'),os.makedirs('exp/img/head_p'),os.makedirs('exp/img/item'),os.makedirs('exp/img/post')
            self.manager.current = 'FileChooser'
            self.manager.transition.direction = "up"


class HeaderWindow(Screen):
    def HEADinputProcess(self):
        global imgPath
        name_alea = (''.join((choice(ascii_letters) for _ in range(8))))
        
        def imgItem():
            with open(imgPath, 'r+b') as ff :
                with Image.open(ff) as image:
                    widht, height = image.size
                    cover = resizeimage.resize_cover(image, [770, 340])
                    cover.save('exp/img/item/'+name_alea+ '-item.webp')
            with open(imgPath, 'r+b') as ff :
                with Image.open(ff) as image:
                    widht, height = image.size
                    cover = resizeimage.resize_cover(image, [270, 237])
                    cover.save('exp/img/item/'+name_alea+ '-av.webp')
                
        with open(imgPath, 'r+b') as ff :
            with Image.open(ff) as image:
                widht, height = image.size
                if(widht >= 1900 and height >= 600):
                    #exp
                    cover = resizeimage.resize_cover(image, [1900, 600])
                    cover.save('exp/img/head_p/'+name_alea+ '.webp')
                    #temp
                    cover = resizeimage.resize_cover(image, [1900, 600])
                    cover.save('temp/img/'+name_alea+ '-head.webp')
                    imgItem()
                elif(widht >= 950 and height >= 300):
                    #exp
                    cover = resizeimage.resize_cover(image, [950, 300])
                    cover.save('exp/img/head_p/'+name_alea+ '.webp')
                    #temp
                    cover = resizeimage.resize_cover(image, [950, 300])
                    cover.save('temp/img/'+name_alea+ '-head.webp')
                    imgItem()
                else:print('trop petite')   
                    
        
        text_a = self.ids.HEAD_input_a.text
        text_b = self.ids.HEAD_input_b.text
        text_c = self.ids.HEAD_input_c.text
        text_d = self.ids.HEAD_input_d.text   
        if text_a == '' or text_b == '' or text_c == '' or text_d == '':
            show_popup('Attention !', 'Entrez les données !')
        else:
            self.ids.HEAD_input_a.text = ''
            self.ids.HEAD_input_b.text = ''
            self.ids.HEAD_input_c.text = ''
            self.ids.HEAD_input_d.text = ''
            date= strftime('%d/%m/%y')   
            
            with open('temp/' + 'post.html','w') as fichier:    #temp
                img='img/'+name_alea+'-head.webp'
                fichier.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">        
    <title>Ile-Segal - %s</title>        
    <link href="../.needs/bootstrap.min.css" rel="stylesheet">
    <link href="../.needs/clean-blog.min.css" rel="stylesheet">        
    <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
</head>

<body>
    <nav class="navbar navbar-default navbar-custom navbar-fixed-top">
        <div class="container-fluid">
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    Menu <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand" href="../index">< Précédent</a>
                <a class="navbar-brand" href="../index">Suivant ></a>
            </div>
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="ile-segal.com">Home</a>
                    </li>
                    <li>
                        <a href="ile-segal.com/contact">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
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
    <article>
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">"""% (text_a,img,text_b,text_c,text_d,date))                

            with open('exp/post/' + 'post.html','w') as fichier:   #exp-webp
                img='../img/head_p/'+name_alea+'.webp'
                fichier.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Ile-Segal - %s</title>

    <link href="../css/post/bootstrap.min.css" rel="stylesheet">
    <link href="../css/post/clean-blog.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
<body>
<nav class="navbar navbar-default navbar-custom navbar-fixed-top">
    <div class="container-fluid">
        <div class="navbar-header page-scroll">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                <span class="sr-only">Toggle navigation</span>
                Menu <i class="fa fa-bars"></i>
            </button>
            <a class="navbar-brand" href="../index">< Précédent</a>
            <a class="navbar-brand" href="../index">Suivant ></a>
        </div>
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
    </div>
</nav>
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
<article>
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">"""% (text_a,img,text_b,text_c,text_d,date))

            self.manager.current = 'Menu'
            self.manager.transition.direction = "up"

class MenuWindow(Screen):
    def entry(self, int):
        global screenEntry
        screenEntry = int

class ShowWindow(Screen):
    def show(self):        
        print('Woek')
        try:
            from webview import WebView
            WebView("https://www.google.com")
        except Exception:
            try:
                open_new_tab("https://www.google.com")
            except Exception:
                print('Doesn\'t woek')
        else:
            print('Doesn\'t woek d le dbut')

class ExportWindow(Screen):
    def thisIstheeEnd(self):
        with open('exp/post/' + 'post.html','a') as fichier:
            fichier.write("""
                 </div>
            </div>
        </div>
    </article>

    <hr>

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
                    <p class="copyright text-muted">Copyright &copy; Ile-Segal 2022</p>
                </div>
            </div>
        </div>
    </footer>
    <script src="../js/jquery/jquery.min.js"></script>
    <script src="../js/bootstrap_v3.3.7.min.js"></script>
    <script src="../js/clean-blog.min.js"></script>
</body>
</html>""")        
        
        app.rmall()
        self.manager.current = 'Start'
        self.manager.transition.direction = "up"

class FCWindow(Screen):
    def load(self, path, filename):
        global imgPath
        try:
            imgPath = os.path.join(path, filename[0])
        except:
            show_popup('Attention !', 'Séléctionez d\'abord un fichier !')
        else:            
            global screenEntry 
            if screenEntry == 1:
                self.manager.current = 'Header'
                self.manager.transition.direction = "up"
            else:
                self.manager.current = 'Img'
                self.manager.transition.direction = "left"
                
    def cancelScreen(self): 
        global screenEntry 
        if screenEntry == 1:
            app.rmall()
            self.manager.current = 'Start'
            self.manager.transition.direction = "down"
        else:
            self.manager.current = 'Menu'
            self.manager.transition.direction = "right"

class TDPWindow(Screen):
    def TDPinputProcess(self):
        text = self.ids.tdp_input.text        
        if text == '' :
            show_popup('Attention !', 'Entrez les données !')
        else:
            self.ids.tdp_input.text = ''  
            
            with open('temp/' + 'post.html','a') as fichier:        #temp
                fichier.write("""
                <h2 class="section-heading">%s</h2>\n"""% (text))                    
            with open('exp/post/' + 'post.html','a') as fichier:    #exp
                fichier.write("""
                <h2 class="section-heading">%s</h2>\n"""% (text))
            
            self.manager.current = 'Menu'
            self.manager.transition.direction = "left"

class TxtWindow(Screen):
    def TXTinputProcess(self):
        text = self.ids.txt_input.text
        if text == '' :
            show_popup('Attention !', 'Entrez les données !')
        else:
            self.ids.txt_input.text = ''
            
            with open('temp/' + 'post.html','a') as fichier:        #temp
                fichier.write("""
                <p>%s</p>\n"""""% (text.replace('\n', '<br>')))                    
            with open('exp/post/' + 'post.html','a') as fichier:    #exp
                fichier.write("""
                <p>%s</p>\n"""""% (text.replace('\n', '<br>')))
            
            self.manager.current = 'Menu'
            self.manager.transition.direction = "left"

class ImgWindow(Screen):
    def IMGinputProcess(self):
        global imgPath
        name_alea = (''.join((choice(ascii_letters) for _ in range(8))))
        
        with open(imgPath, 'r+b') as f:
            with Image.open(f) as image:
                widht, height = image.size
                if(widht >= 778 and height >= 514):
                    #exp
                    cover = resizeimage.resize_cover(image, [778, 514])
                    cover.save('exp/img/post/'+name_alea+ '.webp')                    
                    #temp
                    cover = resizeimage.resize_cover(image, [778, 514])
                    cover.save('temp/img/'+name_alea+ '.webp')
                else:print('trop petite')
        
        text_c = self.ids.IMG_input_c.text
        text_l = self.ids.IMG_input_l.text
        
        if text_c == '' or text_l == '':
            show_popup('Attention !', 'Entrez les données !')
        else:        
            self.ids.IMG_input_c.text = ''
            self.ids.IMG_input_l.text = ''
            
            with open('temp/' + 'post.html','a') as fichier:        #temp
                fichier.write("""  
                <a href="#">
                    <img class="img-responsive" src="%s" alt="%s">
                </a>
                <span class="caption text-muted">%s</span>                     
              """% (('img/'+name_alea+'.webp'),text_c,text_l))
               
            with open('exp/post/' + 'post.html','a') as fichier:    #exp
                fichier.write("""  
                <a href="#">
                    <img class="img-responsive" src="%s" alt="%s">
                </a>
                <span class="caption text-muted">%s</span>                      
              """% (('../img/post/' +name_alea+'.webp'),text_c,text_l))  
            
            self.manager.current = 'Menu'
            self.manager.transition.direction = "left"

class QuoteWindow(Screen):
    def QUOTEinputProcess(self):
        text = self.ids.QUOTE_input.text
        if text == '' :
            show_popup('Attention !', 'Entrez les données !')
        else:
            self.ids.QUOTE_input.text = ''
            
            with open('temp/' + 'post.html','a') as fichier:        #temp
                fichier.write("""
                <blockquote>%s</blockquote>\n"""""% (text.replace('\n', '<br>')))                    
            with open('exp/post/' + 'post.html','a') as fichier:    #exp
                fichier.write("""
                <blockquote>%s</blockquote>\n"""""% (text.replace('\n', '<br>')))
        
            self.manager.current = 'Menu'
            self.manager.transition.direction = "left"

class LinkWindow(Screen):
    def LINKinputProcess(self):
        text_a = self.ids.LINK_input_a.text
        text_b = self.ids.LINK_input_b.text
        text_c = self.ids.LINK_input_c.text
        text_d = self.ids.LINK_input_d.text    
        if text_a == '' or text_b == '' or text_c == '' or text_d == '':
            show_popup('Attention !', 'Entrez les données !')
        else:
            self.ids.LINK_input_a.text = ''
            self.ids.LINK_input_b.text = ''
            self.ids.LINK_input_c.text = ''
            self.ids.LINK_input_d.text = ''
        
            print(text_a, text_b, text_c, text_d)
        
            self.manager.current = 'Menu'
            self.manager.transition.direction = "left"

class WindowManager(ScreenManager):
    pass    


kv = Builder.load_file("AppSite.kv")


class V2_2App(App): 
    def build(self):
        return kv
    
    def rmall(self):
        if os.path.exists('exp/'):
            rmtree('exp/')
        if os.path.exists('temp/') :
            rmtree('temp/')
        print('del')

def show_popup(_title, _text):  
    popupWindow = Popup(title = _title, 
                        title_align = 'left',
                        title_size = '20sp',
                        title_color =  [1, 1, 1, 1],
                        separator_color =[47 / 255., 167 / 255., 212 / 255. ,1.],
                        separator_height ='2dp',
                        content = Label(text= _text,
                                        halign = 'center',
                                        valign = 'top',
                                        text_size = (180, None)
                                        ),
                        size_hint =(.6, .4)
                        )
  
    popupWindow.open()

if __name__ == "__main__":
    app = V2_2App()
    app.run()
    
"""
-Problème lors erreur dans image si trop petite:
    mettre les fonctions transformations d'images dans fchooser, et mettre 
    var global pour récup le nom des images
-Finir fonction exporter
-s'oocuper des liens :
    mettre un bouton lien directement dans le module texte ?
"""