# -*- coding: utf-8 -*-
import pysrt
import webvtt
from webvtt import WebVTT, Caption
subs = pysrt.open('Tanmay Bakshi - New Google Employee Indian Boy Going To Ninth Grade.srt', encoding='utf-8')
vtt = WebVTT()
for ligne in subs:
    print(str(ligne.start))
    print(str(ligne.end))
    print(str(ligne.text))
    caption = Caption(
            str(ligne.start),
            str(ligne.end),
            str(ligne.text)
            )
            #print(caption.start)
            #print(caption.end)
            #print (var2)
    vtt.captions.append(caption)
vtt.save('_fr.vtt')
