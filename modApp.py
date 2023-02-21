# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:54:14 2021

@author: yan-s
"""

import os, sys
from PIL import Image
from resizeimage import resizeimage
from shutil import move, rmtree
from random import choice
from time import strftime, ctime
from webbrowser import open_new_tab
from string import ascii_letters

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