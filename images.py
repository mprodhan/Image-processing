from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')

print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')

filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img2.save("smooth.png", 'png')

filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img3.save("sharp.png", 'png')

filtered_img4 = img.convert('L')
filtered_img4.save("grey_pika.png", 'png')
filtered_img4.show()

crooked = filtered_img4.rotate(90)
crooked.save("grey.png", 'png')
crooked.show()

resized = filtered_img4.resize((300,300))
resized.save("grey.png", 'png')

box = (100, 100, 400, 400)
cropped_img = filtered_img4.crop(box)
cropped_img.save("grey_crop.png", 'png')