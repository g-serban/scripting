from PIL import Image, ImageFilter


img = Image.open('./Pokedex/pikachu.jpg')
filter_img = img.filter(ImageFilter.SHARPEN)
filter_img.save('blur3.png', 'png')  #name, img format

filter_grey = img.convert('L') # converts image to a grey format (it was RGB before)
filter_grey.save('grey1.png', 'png')

rotated = filter_grey.rotate(180)
rotated.save('rotated.png', 'png')

resized = filter_grey.resize((300, 300))  # -> resize accepts a tupple
resized.save('resized.png', 'png')

box = (100, 100, 400, 400)
cropped = filter_grey.crop(box)
cropped.save('croppedface.png', 'png')

astronaut = Image.open('./astro.jpg')
astronaut.thumbnail((400, 400)) # thumbnail method can't be saved to a variable -> NoneObject, because thumbnail
astronaut.save('thumbnail.png', 'png') # actually just edits the original image
 # thumbnail method is good for ex if you want to create a profile pic for a social media site
