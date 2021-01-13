from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title('Rock Paper Scissor')
root.geometry('600x500')
root.configure(bg='#34445e')
images = ['paper.jpeg', 'scissor.jpeg', 'stone.jpeg']

random_image = Image.open(random.choice(images))
random_image = ImageTk.PhotoImage(random_image)

base_img = Image.open('base.png')
base_img = ImageTk.PhotoImage(base_img)

paper_img = Image.open('paper.jpeg')
paper_img = ImageTk.PhotoImage(paper_img)

stone_img = Image.open('stone.jpeg')
stone_img = ImageTk.PhotoImage(stone_img)

scissor_img = Image.open('scissor.jpeg')
scissor_img = ImageTk.PhotoImage(scissor_img)


com_label = Label(root, text='Computer', width=10, font=('arial', 30, 'bold'))
com_label.place(x=15, y=20)

player_label = Label(root, text='Player', width=10, font=('arial', 30, 'bold'))
player_label.place(x=320, y=20)

root.mainloop()
