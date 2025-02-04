from tkinter import Tk, Label, Entry, Button, filedialog
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageFont

def add_watermarker():
    global image, file_path

    if image:
        with Image.open(file_path) as image:
            width, height = image.size
            x = width / 2
            y = height / 2

            watermark_text = Image.new('RGBA', image.size, (255,255,255,0))
            watermark_font = ImageFont.truetype('arial.ttf', 40)

            watermark_draw = ImageDraw.Draw(watermark_text)

            watermark_draw.text((x,y), 'WATERMARKER', font=watermark_font, fill=(255,255,255,128))
            watermark_text = watermark_text.rotate(45)

            final_image = Image.alpha_composite(image.convert('RGBA'), watermark_text)

            panel.config(image=final_image)
            panel.image = final_image

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
