from tkinter import *

root = Tk()
background_image=PhotoImage("C:\Dev\music.png")
background_label = Label(root, image=background_image)
background_label.pack(side=TOP, padx=10, pady=10)



root.wm_geometry("600x400+20+40")
root.title('Menu')


playButton = Button(root, text='Play', command=root.destroy)
playButton.pack()
root.mainloop()