from tkinter import *
from PIL import Image, ImageTk
import random

computer_point = 0
player_point = 0

root = Tk()
root.title('Rock Paper Scissor')
root.geometry('600x500')
root.configure(bg='#34445e')

base_img = Image.open('base.png').resize((252, 150))
base_img = ImageTk.PhotoImage(base_img)

paper_img = Image.open('paper.jpeg').resize((252, 150))
paper_img = ImageTk.PhotoImage(paper_img)

rock_img = Image.open('stone.jpeg').resize((252, 150))
rock_img = ImageTk.PhotoImage(rock_img)

scissor_img = Image.open('scissor.jpeg').resize((252, 150))
scissor_img = ImageTk.PhotoImage(scissor_img)

images = [paper_img, rock_img, scissor_img]


def random_select():
    img = random.choice(images)
    com_play_lab.configure(image=img)


def rock_select():
    player_play_lab.configure(image=rock_img)
    random_select()


def paper_select():
    player_play_lab.configure(image=paper_img)
    random_select()


def scissor_select():
    player_play_lab.configure(image=scissor_img)
    random_select()


com_label = Label(root, text='Computer', width=10, font=('arial', 30, 'bold'))
com_label.place(x=15, y=20)

player_label = Label(root, text='Player', width=10, font=('arial', 30, 'bold'))
player_label.place(x=320, y=20)

com_play_lab = Label(image=base_img)
com_play_lab.place(x=15, y=70)

player_play_lab = Label(image=base_img)
player_play_lab.place(x=320, y=70)

rock_btn = Button(root, text='Rock', width=6, bg='blue', fg='black', command=rock_select)
rock_btn.place(x=320, y=250)

paper_btn = Button(root, text='Paper', width=6, bg='blue', fg='black', command=paper_select)
paper_btn.place(x=410, y=250)

Scissor_btn = Button(root, text='Scissor', width=6, bg='blue', fg='black', command=scissor_select)
Scissor_btn.place(x=500, y=250)

root.mainloop()
