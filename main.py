import qrcode
from tkinter import *
import pyshorteners
import pyperclip


def generate_qr():
    global link_val,shortened_link
    short = pyshorteners.Shortener()
    link_string = short.tinyurl.short(link_val.get())
    pyperclip.copy(link_string)
    shortened_link.config(text=link_string)
    qr = qrcode.QRCode(version=1, box_size=6, border=6)
    qr.add_data(link_string)
    qr.make()
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qr.png')
    global qr_image
    qr_image = PhotoImage(file="qr.png")
    canvas.create_image(150, 150, image=qr_image)
    link_val.delete(0, END)


window=Tk()
window.title("Convert to QR")
window.config(padx=30,pady=30)

link_label=Label(text="Enter Link: ")
link_label.pack()

link_val=Entry(width=15)
link_val.pack()

get_qr_button=Button(text="Generate QR code",command=generate_qr)
get_qr_button.pack()

shortened_link=Label(text="")
shortened_link.pack()


canvas=Canvas(width=300,height=300)
qr_image=PhotoImage(file = "blank.png")
canvas.create_image(150,150,image=qr_image)
canvas.pack()





window.mainloop()