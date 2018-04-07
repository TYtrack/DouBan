from urllib.request import urlretrieve
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re

f = open('douban.txt', 'w',encoding='utf-8')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url="https://movie.douban.com/top250?filter=", headers=headers)  
html =urlopen(req)
bsObj = BeautifulSoup(html)

mem_url = bsObj.find("body").findAll("a",{"class":"","href":re.compile("https:\/\/movie\.douban\.com\/subject\/")})
#nameList = bsObj.find("body").findAll("span",{"class":"name_j"})
for i in range(len(mem_url)):
    mem_url[i].find("a")
    print(mem_url[i].attrs["href"]+"reviews")
    #<div class="review-content clearfix"
    #<div class="review-short hidden
    html1 = urlopen(mem_url[i].attrs["href"]+"reviews")
    bsObj2 = BeautifulSoup(html1)
    title1=bsObj2.find("div",{"class":"subject-title"}).find("a")
    f.write("\n"+title1.text)
    hkt_pic = bsObj2.find("body").findAll("div",{"class":"short-content"})
    #print(hkt_pic)
    #pattern = re.compile(r'<[^>]+>', re.S)
    #hkt_pic = pattern.sub('', hkt_pic)
    for j in range(len(hkt_pic)):
        #hkt_pic[j] = pattern.sub('', hkt_pic[j])
        hkt_pic[j]=hkt_pic[j].text.replace("(展开)","")
        hkt_pic[j]=hkt_pic[j].replace("这篇影评可能有剧透","")
        hkt_pic[j]=hkt_pic[j].replace("\n","")
        hkt_pic[j]=hkt_pic[j].replace("...","")
        hkt_pic[j]=hkt_pic[j].replace(" ","")
        print(hkt_pic[j])
        f.write(hkt_pic[j])
    #print(nameList[i].text)
    #urlretrieve (hkt_pic.attrs["src"],nameList[i].text+".jpg")


f.close()
