import re
from SceneCreator import SceneCreator
from TwitterWrapper.TweepyWrapper import TwitterApi

# Create Scene Image
sceneCreator = SceneCreator()

# Setup Twitter API and Post Tweet
twitter = TwitterApi()
explorations = twitter.recentMentions(minutes=10)

for tweet in explorations:
    pattern = '([A-Fa-f0-9]{6}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{6})'
    planetCode = re.search(pattern, tweet.text)
    planetId = planetCode.group(0)

    sceneImg, sceneTxt = sceneCreator.createScene(
                coordinates=planetId,
                canvas=(100,100))
    sceneImg.save('art/rendered/planet.png')

    twitter.postUpdateWithImage(
            filePath = 'art/rendered/planet.png',
            status = '@{0}\n{1}'.format(tweet.user.screen_name, sceneTxt))
