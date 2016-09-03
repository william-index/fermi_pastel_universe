import re
from SceneCreator import SceneCreator
from TwitterWrapper.TweepyWrapper import TwitterApi
from PIL import Image, ImageDraw, ImageOps, ImageFont


# Create Scene Image
sceneCreator = SceneCreator()

# Setup Twitter API and Post Tweet
twitter = TwitterApi()
explorations = twitter.recentMentions(minutes=10)

for i,tweet in enumerate(explorations[0:14]):
    pattern = '([A-Fa-f0-9]{6}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{6})'
    planetCode = re.search(pattern, tweet.text)
    planetId = planetCode.group(0)

    sceneImg, sceneTxt = sceneCreator.createScene(
                coordinates=planetId,
                canvas=(100,100))
    sceneImg.convert('RGB')
    sceneImg.save('art/rendered/planet{0}.png'.format(i))

    twitter.postUpdateWithImage(
            filePath = 'art/rendered/planet{0}.png'.format(i),
            status = '@{0}\n{1}'.format(tweet.user.screen_name, sceneTxt))
