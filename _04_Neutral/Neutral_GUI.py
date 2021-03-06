
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
        <li>NEUTRAL</li>
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
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8</p><p>BOHEMIAN RHAPSODY</p></span></span> <a href="#"><img src="css/images/movie1.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1727824/">IMDB LINK</a></p>
           </div>
           <div class="rating">
             <p>GENRE : Biography, Drama, Music</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.2</p><p>THE KING</p></span></span> <a href="#"><img src="css/images/movie2.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt7984766/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Drama, History</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.7</p><p>JUMANJI: THE NEXT LEVEL</p></span></span> <a href="#"><img src="css/images/movie3.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt7975244/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Action, Adventure, Comedy</p>
          </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">6.9</p><p>THE LION KING</p></span></span> <a href="#"><img src="css/images/movie4.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt6105098/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Animation, Adventure, Drama</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.2</p><p>ARTICLE 15</p></span></span> <a href="#"><img src="css/images/movie5.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt10324144/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Crime, Drama</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8</p><p>SUPER 30</p></span></span> <a href="#"><img src="css/images/movie6.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt7485048/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Drama</p>
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
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.9</p><p>SCHINDLER'S LIST</p></span></span> <a href="#"><img src="css/images/movie7.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0108052/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Drama, History</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.7</p><p>GOODFELLAS</p></span></span> <a href="#"><img src="css/images/movie8.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0099685/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Crime, Drama</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.2</p><p>GULLY BOY</p></span></span> <a href="#"><img src="css/images/movie9.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt2395469/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Musical</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.1</p><p>THE PRINCESS BRIDE</p></span></span> <a href="#"><img src="css/images/movie10.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0093779/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Adventure, Family, Fantasy</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8.2</p><p>BHAAG MILKHA BHAAG</p></span></span> <a href="#"><img src="css/images/movie11.jpg" alt="" /></a> </div>
         <div class="rating">
            <p><a href="https://www.imdb.com/title/tt2356180/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Drama, Sport</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8</p><p>WONDER</p></span></span> <a href="#"><img src="css/images/movie12.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt2543472/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, Family</p>
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
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">8</p><p>THE SOUND OF MUSIC</p></span></span> <a href="#"><img src="css/images/movie13.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0059742/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Drama, Family</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.6</p><p>THE BLIND SIDE</p></span></span> <a href="#"><img src="css/images/movie14.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt0878804/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Drama, Sport</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.4</p><p>KESARi</p></span></span> <a href="#"><img src="css/images/movie15.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt6264938/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Action, Drama, History</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.3</p><p>GOLD</p></span></span> <a href="#"><img src="css/images/movie16.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt6173990/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Drama, History, Sport</p>
           </div>
        </div>
        <div class="movie">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.6</p><p>THE GREATEST SHOWMAN</p></span></span> <a href="#"><img src="css/images/movie17.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1485796/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Drama, Musical</p>
           </div>
        </div>
        <div class="movie last">
          <div class="movie-image"> <span class="play"><span class="name"><p class="comments">7.7</p><p>THE SOCIAL NETWORK</p></span></span> <a href="#"><img src="css/images/movie18.jpg" alt="" /></a> </div>
          <div class="rating">
            <p><a href="https://www.imdb.com/title/tt1285016/">IMDB LINK</a></p>
          </div>
            <div class="rating">
             <p>GENRE : Biography, Drama</p>
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
    
def browseLocal(webpageText, filename='Neutral_movie.html'):

    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))

#****************************************************************************************#
    
def Movie():
    main()
    

#****************************************************************************************#

def handle_click():
    def songs():
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_04_Neutral/1.mp3', True)
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_04_Neutral/2.mp3', True)
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_04_Neutral/3.mp3', True)
        playsound.playsound('C:/Users/Shivani/Documents/1 final project/Chatbot with mood based recommendation/Emotion-detection/src/GUI_Code/_04_Neutral/4.mp3', True)
    t = threading.Thread(target=songs)
    t.start()
    
#****************************************************************************************#
main_screen = Tk()
main_screen.geometry("400x260")
main_screen.iconbitmap("./icon2.ico")
main_screen.title("Entertainment for Your Mood")

HeadLabel=Label(main_screen, text="Face Emotion Detected    :   Neutral  ", bg="#FCF7DE", width="100", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 

#****************************************************************************************#

MButton=Button(main_screen, text="MOVIE", height="2", width="30",  command=Movie).pack() 
Label(text="").pack() 

#****************************************************************************************#

SButton=Button(main_screen, text="SONGS", height="2", width="30" , command=handle_click).pack()
Label(text="").pack() 

#****************************************************************************************#
QButton=Button(main_screen, text="QUIT" , height="2", width="30" , command=quit).pack()
Label(text="").pack() 

#main_account_screen() # call the main_account_screen() function

main_screen.mainloop()

#****************************************************************************************#

