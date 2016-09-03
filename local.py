#!/usr/bin/python
from SceneCreator import SceneCreator
from PIL import Image, ImageDraw, ImageOps, ImageFont


# Create Scene Image
sceneCreator = SceneCreator()
sceneImg, sceneTxt = sceneCreator.createScene(
            canvas=(100,100))
sceneImg.convert('RGB')
width, height = sceneImg.size
sceneImg.resize((width, height), Image.ANTIALIAS)
sceneImg.save('art/rendered/planet.png', 'PNG', quality=100)

sceneImg.show()
