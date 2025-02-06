from tkinter import Tk, Label, Entry, Button, filedialog
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageFont

def add_watermarker():
    global image, file_path

    if image and file_path:
        with Image.open(file_path).convert('RGBA') as image:
            width, height = image.size

            # make a blank image for the text, initialized to transparent text color
            txt = Image.new('RGBA', image.size, (255,255,255,0))

            # get a font
            font = ImageFont.load_default(size=40)
            # get a drawing context
            d = ImageDraw.Draw(txt)

            x = width/2
            y = height/2

            # draw text, half opacity
            d.text((x,y), "Watermark", font=font, fill=(255,255,255,128))
            txt = txt.rotate(45)

            w_i = Image.alpha_composite(image, txt)
            w_i = ImageOps.cover(w_i, (300, 300))
            watermarked_image = ImageTk.PhotoImage(w_i)

            panel.config(image=watermarked_image)
            panel.image = watermarked_image
            

def upload_image():
    global image, file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
    if file_path:
        with Image.open(file_path) as image:
            image = ImageOps.cover(image, (300, 300))
            img_to_show = ImageTk.PhotoImage(image) 
        
        panel.config(image=img_to_show)
        panel.image = img_to_show

# Global scope
image = None
file_path = None

window = Tk()

window.minsize(height=300, width=400)
window.title('Add watermarking')
window.config(padx=10, pady=10)

info_label = Label(text='Type the watermaking to add:')
info_label.grid(row=0, column=0, padx=10, pady=10)

watermaking_entry = Entry(width=30)
watermaking_entry.grid(row=1, column=0, padx=10, pady=10)

btn_upload = Button(text="Carica Immagine", command=upload_image)
btn_upload.grid(row=2, column=0, padx=10, pady=10)

panel = Label(window)
panel.grid(row=3, column=0, padx=10, pady=10)

confirm_button = Button(text='Add', command=add_watermarker, width=10)
confirm_button.grid(row=4, column=0, padx=10)

window.mainloop()
