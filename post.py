from SceneCreator import SceneCreator
from TwitterWrapper.TweepyWrapper import TwitterApi

# Create Scene Image
sceneCreator = SceneCreator()
sceneImg, sceneTxt = sceneCreator.createScene(
            canvas=(100,100))
sceneImg.save('art/rendered/planet.png')

# Setup Twitter API and Post Tweet
twitter = TwitterApi()
twitter.postUpdateWithImage(
        filePath = 'art/rendered/planet.png',
        status = sceneTxt)

# sceneImg.show()
