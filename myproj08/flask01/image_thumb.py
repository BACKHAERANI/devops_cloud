# pip install pillow


from PIL import Image

im = Image.open("static/tree.jpg")
im.thumbnail((800, 600))
im.save("static/tree.jpg")
