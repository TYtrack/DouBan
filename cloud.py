
import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from scipy.misc import imread
font = r'C:\Windows\Fonts\simfang.ttf'
matplotlib.use('qt4agg')
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False
f=open('writefile.txt')
color_mask= imread("head.jpg")
k=1
for i in f:
    text_from_file_with_apath = i
    print(text_from_file_with_apath)
    
    my_wordcloud = WordCloud(font_path=font,mask=color_mask).generate(text_from_file_with_apath)
    my_wordcloud.to_file(str(k)+".jpg")
    k=k+1
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
