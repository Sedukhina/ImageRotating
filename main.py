from PIL import Image
image1 = Image.new("RGB", (960, 960), "#000000")
handle = open("DS1.txt")
while True:
    line = handle.readline()
    if line != "":
        data = line.split()
        image1.putpixel((int(data[1]), int(data[0])), (0, 0, 255, 255))
    if not line:
        break
handle.close()
filename = "myImg.jpg"
image1 = image1.rotate(20)
image1.save(filename)