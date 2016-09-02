# Twitter Bio
# A procedurally-generated pastel universe. Tweet @FermiPasteladox with 16 digit hex (0—9 and A—F) address in format (000000-0000-000000) to explore!
# Twitter Website
# http://williamanderson.io/

from SceneCreator import SceneCreator

# Create Scene Image
sceneCreator = SceneCreator()
sceneImg, sceneTxt = sceneCreator.createScene(
            canvas=(100,100))
sceneImg.save('art/rendered/planet.png')

sceneImg.show()
