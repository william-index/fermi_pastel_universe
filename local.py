from SceneCreator import SceneCreator

# Create Scene Image
sceneCreator = SceneCreator()
sceneImg, sceneTxt = sceneCreator.createScene(
            canvas=(100,100))
sceneImg.save('art/rendered/planet.png')

sceneImg.show()
