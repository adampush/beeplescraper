# go through each image in beeple_images folder and show them using tkinter

import tkinter as tk
from itertools import cycle
import PIL
import PIL.Image
import PIL.ImageTk
import os

WRITE_FOLDER = "/home/anhad/Pictures/beeple_images/"
BAD_FOLDER = "/home/anhad/Pictures/bad/"

root = tk.Tk()
root.title('Beeple Images')
root.geometry('{}x{}'.format(800, 600))
label = tk.Label(root)
label.pack()


image_list = []

image_number = 1
for image_file in os.listdir(WRITE_FOLDER):
    if image_file.endswith('.jpg'):
        image_path = os.path.sep.join([WRITE_FOLDER, image_file])
        #print(image_path)
        image_list.append(image_path)
        image_number += 1

i = 0
bad_indexes = []

def handle_up(event):
    global i
    i += 1
    print("current image: {}".format(i))

def handle_down(event):
    global i
    i -= 1
    print("current image: {}".format(i))

def handle_space(event):
    global i
    if i in bad_indexes:
        bad_indexes.remove(i)
        print("removed {} from bad_indexes".format(i))
    else:
        print("bad image: {}".format(i))
        bad_indexes.append(i)

def print_list(event):
    print(bad_indexes)

loop = True

def stop_loop(event):
    global loop
    loop = False
    

root.bind('<Up>', handle_up)
root.bind('<Down>', handle_down)
root.bind('<space>', handle_space)
root.bind('<Return>', print_list)
root.bind('<Escape>', stop_loop)

while(loop):
    image = PIL.Image.open(image_list[i]).resize((800, 600))
    image_tk = PIL.ImageTk.PhotoImage(image)
    label.config(image=image_tk)

    # if i is in bad_indexes, draw a red X over the image
    if i in bad_indexes:
        label.config(borderwidth=3, relief="solid")
    else:
        label.config(borderwidth=0)

    label.pack()
    
    root.update()

    # get keyboard input
    # up arrow: increment i
    # down arrow: decrement i
    # space, save i to a list called bad images

    


    # get keyboard input from the user
    # 

    #image_number += 1
    #time.sleep(1000)
    #if image_number > MAX_IMAGES:
    #    break
#root.mainloop()

root.destroy()
root.quit()

    # find the image in the image_list with the index i
    # move this image from beeple_images to bad_images
for i in bad_indexes:
    image_path = image_list[i]
    dest = image_path.replace(WRITE_FOLDER, BAD_FOLDER)
    os.rename(image_path, dest)

    



