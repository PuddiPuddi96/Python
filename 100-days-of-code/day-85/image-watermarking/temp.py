from PIL import Image, ImageDraw, ImageFont

def watermark_photo(input_image_path, watermark_image_path, output_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    # add watermark to your image
    position = base_image.size
    newsize = (int(position[0]*8/100),int(position[0]*8/100))
    # print(position)
    watermark = watermark.resize(newsize)
    # print(newsize)
    # return watermark

    new_position = position[0]-newsize[0]-20,position[1]-newsize[1]-20
    # create a new transparent image
    transparent = Image.new(mode='RGBA',size=position,color=(0,0,0,0))
    # paste the original image
    transparent.paste(base_image,(0,0))
    # paste the watermark image
    transparent.paste(watermark,new_position,watermark)
    image_mode = base_image.mode
    print(image_mode)
    if image_mode == 'RGB':
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert('P')
    transparent.save(output_image_path,optimize=True,quality=100)
    print("Saving"+output_image_path+"...")




base = Image.open('cats.jpg').convert('RGBA')
width, height = base.size

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('arial.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

x = width/2
y = height/2

# draw text, half opacity
d.text((x,y), "Hello", font=fnt, fill=(255,255,255,128))
txt = txt.rotate(45)

out = Image.alpha_composite(base, txt)
out.show()
