from tkinter import Tk, Label, Entry, Button, filedialog
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageFont

def add_watermarker():
    global image, file_path

    if image and file_path:
        with Image.open(file_path).convert('RGBA') as image:
            # Crea un livello trasparente
            txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt_layer)
            font = ImageFont.load_default()
            text = 'watermarker'

            width, height = image.size

            # Calcola la dimensione del testo
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

            # Crea un'immagine separata abbastanza grande per la rotazione
            padding = 50  # Aggiunge spazio per evitare il ritaglio
            text_img = Image.new("RGBA", (text_width + padding, text_height + padding), (255, 255, 255, 0))
            text_draw = ImageDraw.Draw(text_img)

            # Disegna il testo con colore semi-trasparente
            text_color = (255, 255, 255, 120)  # Bianco semi-trasparente
            text_draw.text((padding // 2, padding // 2), text, font=font, fill=text_color)

            # Ruota il testo di 45 gradi
            text_img = text_img.rotate(45, expand=True)

            # Calcola la posizione per centrare il testo ruotato
            text_x = (width - text_img.width) // 2
            text_y = (height - text_img.height) // 2

            # Incolla il testo sul livello trasparente con la maschera
            txt_layer.paste(text_img, (text_x, text_y), text_img)

            # Combina l'immagine originale con il watermark
            watermarked_image = ImageTk.PhotoImage(Image.alpha_composite(image, txt_layer).resize((300,300), Image.LANCZOS))

            panel.config(image=watermarked_image)
            panel.image = watermarked_image
            
            
            
            
            
            
            # width, height = image.size
            # x = width / 2
            # y = height / 2

            # watermark_text = Image.new('RGBA', image.size, (255,255,255,0))
            # watermark_font = ImageFont.truetype('arial.ttf', 40)

            # watermark_draw = ImageDraw.Draw(watermark_text)

            # watermark_draw.text((x,y), 'WATERMARKER', font=watermark_font, fill=(255,255,255,128))
            # watermark_text = watermark_text.rotate(45)

            # final_image = Image.alpha_composite(image.convert('RGBA'), watermark_text)

            # panel.config(image=final_image)
            # panel.image = final_image

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
