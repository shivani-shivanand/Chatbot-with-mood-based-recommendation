
#****************************************************************************************#

from tkinter import *
from tkthread import tk, TkThread
import threading, time
import os
import playsound
from win32com.client import GetObject
import win32api

#****************************************************************************************#

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Movie For Your Mood</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="css/style.css" type="text/css" media="all" />
<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="js/jquery-func.js"></script>
<!--[if IE 6]><link rel="stylesheet" href="css/ie6.css" type="text/css" media="all" /><![endif]-->
</head>
<body>
<!-- START PAGE SOURCE -->
<div id="shell">
  <div id="header">
    <h1 id="logo"><a href="#">MovieForYourMood</a></h1>
    <div class="social"> <span>FOLLOW US ON:</span>
      <ul>
        <li><a class="twitter" href="#">twitter</a></li>
        <li><a class="facebook" href="#">facebook</a></li>
        <li><a class="vimeo" href="#">vimeo</a></li>
        <li><a class="rss" href="#">rss</a></li>
      </ul>
    </div>
    <div id="navigation">
      <ul>
        
      </ul>
    </div>
    <div id="sub-navigation">
      <ul>
        <li>YOUR CURRENT MOOD : </li>
        <li>DISGUSTED</li>
      </ul>
      <div id="search">
        <form action="#" method="get" accept-charset="utf-8">
          <label for="search-field">SEARCH</label>
          <input type="text" name="search field" value="Enter search here" id="search-field" class="blink search-field"  />
          <input type="submit" value="GO!" class="search-button" />
        </form>
      </div>
    </div>
  </div>
  <div id="main">
    <div id="content">
      <div class="box">
        <div class="head">
          <h2>LATEST MOVIES</h2>
          <p class="text-right"><a href="#">See all</a></p>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.1</p><p>Martyrs</p></span></span> <a href="#"><img src="css/images/movie1.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1029234/">IMDB LINK</a></p>
           </div>
           <div class="rating">
             <p>GENRE : Horror</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">4.4</p><p>The Human Centipede</p></span></span> <a href="#"><img src="css/images/movie2.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1467304/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.8</p><p>The Devil's Rejects</p></span></span> <a href="#"><img src="css/images/movie3.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0395584/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror</p>
          </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">4.7</p><p>Grotesque</p></span></span> <a href="#"><img src="css/images/movie4.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1352369/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror, Thriller</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.3</p><p>Dogtooth</p></span></span> <a href="#"><img src="css/images/movie5.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1379182/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Thriller</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">5.1</p><p>A Serbian Film</p></span></span> <a href="#"><img src="css/images/movie6.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1273235/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror, Mystery, Thriller</p>
           </div>
        </div>
        <div class="cl">&nbsp;</div>
      </div>
      <div class="box">
        <div class="head">
          <h2>TOP RATED</h2>
          <p class="text-right"><a href="#">See all</a></p>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.6</p><p>Se7en</p></span></span> <a href="#"><img src="css/images/movie7.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0114369/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Crime, Drama, Mystery</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.5</p><p>The Evil Dead</p></span></span> <a href="#"><img src="css/images/movie8.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0083907/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.2</p><p>The DescentR</p></span></span> <a href="#"><img src="css/images/movie9.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0435625/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Adventure, Horror, Thriller</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.5</p><p>The Last House on the Left</p></span></span> <a href="#"><img src="css/images/movie10.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0844708/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror, Thriller</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.3</p><p>The Hills Have Eyes</p></span></span> <a href="#"><img src="css/images/movie11.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0077681/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror, Thriller</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.4</p><p>Eraserhead</p></span></span> <a href="#"><img src="css/images/movie12.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0074486/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror</p>
           </div>
        </div>
        <div class="cl">&nbsp;</div>
      </div>
      <div class="box">
        <div class="head">
          <h2>RECOMMENDED</h2>
          <p class="text-right"><a href="#">See all</a></p>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.3</p><p>Poltergeist</p></span></span> <a href="#"><img src="css/images/movie13.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0084516/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror, Thriller</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.5</p><p>The Texas Chain Saw Massacre</p></span></span> <a href="#"><img src="css/images/movie14.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0072271/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.5</p><p>A Nightmare on Elm Street</p></span></span> <a href="#"><img src="css/images/movie15.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0087800/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Horror</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.9</p><p>District 9</p></span></span> <a href="#"><img src="css/images/movie16.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1136608/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Action, Sci-Fi, Thrillere</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.7</p><p>The Tenant</p></span></span> <a href="#"><img src="css/images/movie17.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0074811/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Thriller</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.6</p><p>Funny Games</p></span></span> <a href="#"><img src="css/images/movie18.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0119167/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Crime, Drama, Thriller</p>
           </div>
        </div>
        <div class="cl">&nbsp;</div>
      </div>
    </div>
    
   
  <div id="footer">
    <p class="lf">Copyright &copy; 2020 <a href="#">MovieForYourMood</a> - All Rights Reserved</p>
    <div style="clear:both;"></div>
  </div>
</div>
<!-- END PAGE SOURCE -->
</body>
</html>

'''

#****************************************************************************************#

def main():
    browseLocal(contents)

#****************************************************************************************#

def strToFile(text, filename):
    output = open(filename,"w")
    output.write(text)
    output.close()

#****************************************************************************************#
    
def browseLocal(webpageText, filename='Disgusted_movie.html'):

    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))

#****************************************************************************************#
    
def Movie():
    main()
    
#****************************************************************************************#

def handle_click():
    def songs():
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_01_Disgusted/1.mp3', True)
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_01_Disgusted/2.mp3', True)
       
    t = threading.Thread(target=songs)
    t.start()
  

#****************************************************************************************#
main_screen = Tk()
main_screen.geometry("400x260")
main_screen.iconbitmap("./icon2.ico")
main_screen.title("Entertainment for Your Mood")

HeadLabel=Label(main_screen, text="Face Emotion Detected    :   Disgusted  ", bg="#DEFDE0", width="100", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 

#****************************************************************************************#

MButton=Button(main_screen, text="MOVIE", height="2", width="30",  command=Movie).pack() 
Label(text="").pack() 

#****************************************************************************************#

SButton=Button(main_screen, text="SONGS", height="2", width="30" ,  command=handle_click).pack()
Label(text="").pack() 

#****************************************************************************************#
QButton=Button(main_screen, text="QUIT" , height="2", width="30" , command=quit).pack()
Label(text="").pack() 

#main_account_screen() # call the main_account_screen() function

main_screen.mainloop()

#****************************************************************************************#

