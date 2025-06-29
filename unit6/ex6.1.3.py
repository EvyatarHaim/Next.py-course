import tkinter as tk
from PIL import Image, ImageTk


def handel_click():
    label = tk.Label(window, text="This my favorite color!", font=("Arial", 14), fg="Black")
    label.pack()

    image = Image.open(r"C:\Networks\Sigit\Next\unit6\blue.png")
    photo_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(window, image=photo_image)
    image_label.image = photo_image
    image_label.pack()


window = tk.Tk()
window.geometry("500x500")
window.title("tk")
tk.Label(window, text="What is my favorite color?", font=("Arial", 14), fg="Blue").pack()
tk.Button(window, text="Click Me to find out !", command=handel_click).pack()


window.mainloop()
