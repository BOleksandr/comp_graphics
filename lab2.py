from PIL import Image, ImageDraw
image = Image.new('RGB', (960, 540), (255,255,255))
draw = ImageDraw.Draw(image)
with open(r'C:\Users\asus\labs\DS1.txt','r') as f:
    for line in f:
        y_x = line.split()
        x, y = int(y_x[1]), int(y_x[0])
        draw.point((x, y), fill=(0, 0, 0))
image.show()
image.save("image.png")        