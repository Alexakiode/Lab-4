# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:40:06 2022

@author: Beth_El 2
"""


#class Music_collection:
    #def __init__(self,Artist,Song,Playlist):
       # self.Artist = Artist
        
        
class Artist:
    def __init__(self, name, album, release_date):
        self.name = name
        self.album = album
        self.release_date = release_date
        self.song_list = []
    
class Song:
    def __init__(self,artist_name,song_title,duration_of_song):
        self.artist_name = artist_name
        self.song_title = song_title
        self.duration_of_song = duration_of_song
        self.play_list = []
        
class Playlist:
    def __init__(self,song_folder,song_status,number_of_songs,date_created):
        self.song_folder = song_folder
        self.song_status = song_status
        self.number_of_songs = number_of_songs
        self.date_created = date_created

    def Song_list(self, song_list):
        #song1 = Song("Pajawiri")
        #song2 = Song("Alpha")
        #song3 = Song("Omega")
        
#def main():
    #song1 = Song("Pajawiri")
    #song2 = Song("Alpha")
    #song3 = Song("Omega") 
#print(song1)
    
    #(self, song1, song2, song3):
     #   song_list = song1, song2, song3

#print(song_list)

#main()
#artist1 = Artist("Skilo", "Friendly" , "2023")
#song1 = Song("Skilo", "Pajawiri", "3.41")
#playlist1 = Playlist("Circular" , "Favourite" , "5" , "1985")
#music_collection = Playlist("Gospel", "Favourite", "3", "2019")
#print(artist1.name, artist1.album, artist1.release_date, sep = " , ")
#print(song1.artist_name, song1.song_title, song1.duration_of_song, sep = " , ")
#print(playlist1.song_folder,playlist1.song_status,playlist1.number_of_songs,playlist1.date_created,  sep  = ", ")

#artist1 = Artist("Skilo", "Friendly" , "2023")
        song1 = Song("Skilo", "Pajawiri", "3.41")
        song2 = Song("Diamond", "Alpha" , "2.31")
        song3 = Song("Queen", "Omega", "4.12")
#playlist1 = Playlist("Circular" , "Favourite" , "5" , "1985")

print(song1.song_title, "\n ", song2.song_title, "\n ", song3.song_title)

    