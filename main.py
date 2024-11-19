import googletrans
from googletrans import Translator
from logging import root
from tkinter import*
from PIL import Image, ImageTk
from httpx import delete
from matplotlib.pylab import box

root = Tk()
root.title('translator')
root.geometry("500x630")
root.iconbitmap('sakura.ico')

load = Image.open('background.jpg')
render = ImageTk.PhotoImage(load)
img =Label(root, image = render)
img.place(x = 0, y = 0)

name = Label(root, text = ("Translator"),fg = "#FFFFFF", bd = 0, bg = "#b6b5c3")
name.config(font = ("NotoSansJP-Black", 30))
name.pack(pady = 10)

boxinput = Text(root, width = 28, heigh = 8, font = ("NotoSansJP-Black", 16))
boxinput.pack(pady = 20)
boxoutput = Text(root, width = 28, heigh = 8, font = ("NotoSansJP-Black", 16))
boxoutput.pack(pady = 50)

button_frame = Frame(root).pack(side = BOTTOM)


def clear():
    boxinput.delete(1.0, END)
    boxoutput.delete(1.0, END)
def translate():
    input = boxinput.get(1.0, END)
    print(input)
    t = Translator()
    a = t.translate(input, src = "vi", dest = "ja")
    boxoutput.insert(END, a.text)
    
    
clear_button = Button(button_frame, text = "Clear text", font = (("Arial"), 10, 'bold'), bg = '#303030', fg = "#FFFFFF", command = clear)
clear_button.place(x = 140, y =310)
trans_button = Button(button_frame, text = "Translate", font = (("Arial"), 10, 'bold'), bg = '#303030', fg = "#FFFFFF", command = translate)
trans_button.place(x = 280, y = 310)




root.mainloop()