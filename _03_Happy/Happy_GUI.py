
#****************************************************************************************#

from tkinter import *
from tkthread import tk, TkThread
import threading, time
import os
import playsound

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
        <li>HAPPY</li>
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
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.9</p><p>CRAZY RICH ASIANS</p></span></span> <a href="#"><img src="css/images/movie1.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt3104988/">IMDB LINK</a></p>
           </div>
           <div class="rating">
             <p>GENRE : Comedy, Drama, Romance</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8</p><p>LA LA LAND</p></span></span> <a href="#"><img src="css/images/movie2.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt3783958/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Drama, Music</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.1</p><p>INSIDE OUT</p></span></span> <a href="#"><img src="css/images/movie3.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt2096673/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Animation, Adventure, Comedy</p>
          </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.2</p><p>TO ALL THE BOYS I'VE LOVED BEFORE</p></span></span> <a href="#"><img src="css/images/movie4.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt3846674/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Romance</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.1</p><p>YEH JAWAANI HAI DEEWANI</p></span></span> <a href="#"><img src="css/images/movie5.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt2178470/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Musical, Romance</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.1</p><p>GOOD NEWWZ</p></span></span> <a href="#"><img src="css/images/movie6.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt8504014/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Drama</p>
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
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.4</p><p>COCO</p></span></span> <a href="#"><img src="css/images/movie7.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt2380307/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Animation, Adventure, Family</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.8</p><p>THE LUNCH BOX</p></span></span> <a href="#"><img src="css/images/movie8.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt2350496/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Romance</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.6</p><p>DO DOONI CHAAR</p></span></span> <a href="#"><img src="css/images/movie9.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1714832/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Drama</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.1</p><p>THE TRUMAN SHOW</p></span></span> <a href="#"><img src="css/images/movie10.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0120382/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Drama, Sci-Fi</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.4</p><p>KABHI KHUSHI KABHIE GHAM</p></span></span> <a href="#"><img src="css/images/movie11.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0248126/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Musical, Romance</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.8</p><p>FOREST GUMP</p></span></span> <a href="#"><img src="css/images/movie12.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0109830/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Romance</p>
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
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.1</p><p>ZINDAGI NA MILEGI DOBARA</p></span></span> <a href="#"><img src="css/images/movie13.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1562872/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Drama</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.1</p><p>FREAKY FRIDAY</p></span></span> <a href="#"><img src="css/images/movie14.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0322330/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Family, Fantasy</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.5</p><p>THE PARENT TRAP</p></span></span> <a href="#"><img src="css/images/movie15.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0120783/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Adventure, Comedy, Drama</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.1</p><p>DIL CHAHTA HAI</p></span></span> <a href="#"><img src="css/images/movie16.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0292490/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Drama, Romance</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.3</p><p>THE PRINCESS DIARIES</p></span></span> <a href="#"><img src="css/images/movie17.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0247638/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Family, Romance</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.3</p><p>LEGALLY BLONDE</p></span></span> <a href="#"><img src="css/images/movie18.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0250494/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Comedy, Romance</p>
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
    
def browseLocal(webpageText, filename='happy_movie.html'):

    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))

#****************************************************************************************#
    
def Movie():
    main()
    


#****************************************************************************************#

def handle_click():
    def songs():
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_03_Happy/1.mp3', True)
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_03_Happy/2.mp3', True)
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_03_Happy/3.mp3', True)
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_03_Happy/4.mp3', True)
    t = threading.Thread(target=songs)
    t.start()

   
#**************************************************************************************************************#
    
main_screen = Tk()
main_screen.geometry("400x260")
main_screen.iconbitmap("./icon2.ico")
main_screen.title("Entertainment for Your Mood")

HeadLabel=Label(main_screen, text="Face Emotion Detected    :   Happy  ", bg="#FFFF66", width="100", height="2", font=("Calibri", 13)).pack() 
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

# main_account_screen() # call the main_account_screen() function

   # create a GUI window 
    
main_screen.mainloop()

#****************************************************************************************#

