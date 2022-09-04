import instagrapi
import os
import apod

cl = instagrapi.Client()
cl.login('the_void.sea',os.environ.get('insta_pass'))
dlr = apod.APOD()
imgInfo = dlr.img('./')

img = imgInfo[0]
title = imgInfo[1]['title']
exp = imgInfo[1]['explanation']
copyright = imgInfo[1]['copyright']

media = cl.photo_upload(path=img,caption=f"{title}\n\n\n\n{exp}\n credits: {copyright}")

print(media.dict())