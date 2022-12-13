from PIL import Image, ImageDraw
import math
image = Image.new('RGB', (960, 960), (255,255,255))
draw = ImageDraw.Draw(image)
angle = math.radians(20)
with open(r'C:\Users\asus\labs\DS1.txt','r') as f:
    for line in f:
        y_x = line.split()
        i, j = int(y_x[1]) - 480, int(y_x[0]) - 480
        x = i * math.cos(angle) - j * math.sin(angle)
        y = i * math.sin(angle) + j * math.cos(angle)
        draw.line((x + 480, y + 480, x + 481, y + 481), fill=(0, 0, 255))
image.show()
image.save("result.png") 