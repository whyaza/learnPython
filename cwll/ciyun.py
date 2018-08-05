import pymongo
#jieba用来分词，wordcloud用来制作词云
import json
import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator

from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator 

def get_data():
    client = pymongo.MongoClient(host='localhost',port=27017)
    db  = client.HEUteacher
    tecollection = db.teachers
    datalist = tecollection.find()
    for data in datalist:
        yield data['profile']
dstr = ''
for data in get_data():
    dstr += data
print(dstr)
print(type(dstr))

#用jieba进行分词
result = jieba.analyse.textrank(dstr,topK=50,withWeight=True)
keywords = dict()
for i in result:
      keywords[i[0]]=i[1]
print(keywords)

image= Image.open('tim.jpg')
graph = np.array(image)
wc = WordCloud(font_path='msyh.ttf',background_color='White',max_words=50,mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()

wc.to_file('gc_wordcloud.png')
