from tkinter import *
import pygame
import os
import random

root = Tk()
root.title("MUSIC PLAYER")
root.geometry("600x350")

pygame.mixer.init()
count=0
songs =[]
history=[]
current_music = ""
paused = False
position=0


def load_music():
    root.directory = "AI1110_audios"

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)

def play_music():
    global current_music, paused,position,count
    current_music=songs[count]
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory,current_music))
        history.append(current_music)
        position+=1
        pygame.mixer.music.play()
        
    else:
        pygame.mixer.music.unpause()
        paused=False


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True
    

def next_music():
    global current_music,paused,count,position
    pygame.mixer.music.pause()
    count+=1
    if count == 20:
        count=0
        random.shuffle(songs)
    paused=True
    current_music=songs[count]
    pygame.mixer.music.load(os.path.join(root.directory,current_music))
    history.append(current_music)
    position+=1
    pygame.mixer.music.play()

def prev_music():
    global current_music,position
    pygame.mixer.music.pause()
    paused=True
    if position ==1:
        pygame.mixer.music.load(os.path.join(root.directory,current_music))
        pygame.mixer.music.play()

    else:
        position-=1
        pygame.mixer.music.load(os.path.join(root.directory,history[position-1]))
        pygame.mixer.music.play()

songlist = Listbox(root, bg="seagreen", fg="maroon", width=100, height=13)
songlist.pack()

play_btn_img = PhotoImage(file="images/play.png")
pause_btn_img = PhotoImage(file="images/pause.png")
next_btn_img = PhotoImage(file="images/next.png")
prev_btn_img = PhotoImage(file="images/previous.png")

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image = play_btn_img, borderwidth=10,command=play_music)
pause_btn = Button(control_frame, image = pause_btn_img, borderwidth=10,command=pause_music)
next_btn = Button(control_frame, image = next_btn_img, borderwidth=5,command=next_music)
prev_btn = Button(control_frame, image = prev_btn_img, borderwidth=5,command=prev_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

load_music()
random.shuffle(songs)

root.mainloop()