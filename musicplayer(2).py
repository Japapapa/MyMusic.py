# Placing all the objects in all the three LabelFrames
# Creating the final Label that will display the status of the song


# Importing all the libraries
import pygame.mixer as mixer
import os
from tkinter import *
from tkinter import filedialog
import sqlite3

# Initializing the pygame.mixer
mixer.init()

# inicializing the root
root= Tk()
root.geometry('1000x520')
root.title('MusicP')
root.resizable(0, 0)

# Defining the play, stop, pause, resume and load functions
def play_song(song_name: StringVar, song_list: Listbox, status: StringVar):
    song_name.set(song_list.get(ACTIVE))

    mixer.music.load(song_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='THIS IS THE LIFE'))
    tracks = os.listdir()
    for track in tracks:
        listbox.insert(END, track)


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song resume")

# Creating the LabelFrames and StringVar variables
song_frame = LabelFrame(root, text="Current Song", bg='LightBlue', width= 700, height= 380)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='Turquoise', width=700, height=420)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
listbox_frame.place(x=700, y=0, height=500, width= 300)

current_song= StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not Available>')

playlist = Listbox(listbox_frame, font=('Helvetica', 21), selectbackground='Gold')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side='right', fill='both')

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

# SongFrame Labels
Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)
song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)

# Buttons in the main screen
pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=10,
    command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)
stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=10,
    command=lambda: stop_song(song_status))
stop_btn.place(x=155, y=10)
play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=10,
    command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=305, y=10)
resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=10,
    command=lambda: resume_song(song_status))
resume_btn.place(x=455, y=10)
load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=65, command=lambda: load(playlist))
load_btn.place(x=10, y=55)

#finalizing the root
root.update()
root.mainloop()