from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
root.title('Mp3 player') 
mixer.init()
songs_list=Listbox(root,bg="violet",fg="dark blue",font='arial 15',height=12, width=47,selectmode=SINGLE,selectbackground='brown',selectforeground='white')
songs_list.grid(columnspan=6)

def play():
    song=songs_list.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def previous():
    p_one=songs_list.curselection()
    p_one=p_one[0]-1
    temp=songs_list.get(p_one)
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(p_one)
    songs_list.selection_set(p_one)

def next():
    n_one=songs_list.curselection()
    n_one=n_one[0]+1
    temp2=songs_list.get(n_one)
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(n_one)
    songs_list.selection_set(n_one)

def add():
    temp_song = filedialog.askopenfilenames(title="Choose a song",filetypes=(("mp3 Files", "*.mp3"),))
    for s in temp_song:
        songs_list.insert(END, s)
def delete():
    curr_songs=songs_list.curselection()
    songs_list.delete(curr_songs[0])

play_btn=Button(root,text='play',font='arial',width=7,command=play)
play_btn.grid(row=1,column=0)

pause_btn=Button(root,text='pause',font='arial',width=7,command=pause)
pause_btn.grid(row=1,column=1)

stop_btn=Button(root,text='stop',font='arial',width=7,command=stop)
stop_btn.grid(row=1,column=2)

resume_btn=Button(root,text='resume',font='arial',width=7,command=resume)
resume_btn.grid(row=1,column=3)

previous_btn=Button(root,text='previous',font='arial',width=7,command=previous)
previous_btn.grid(row=1,column=4)

next_btn=Button(root,text='next',font='arial',width=7,command=next)
next_btn.grid(row=1,column=5)

my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add Songs",command=add)
add_song_menu.add_command(label="Delete Songs",command=delete)
root.mainloop()
