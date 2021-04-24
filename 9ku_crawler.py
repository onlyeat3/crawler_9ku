import json

import requests
from bs4 import BeautifulSoup

# 需要替换成自己想下载的关键词
response = requests.get('https://baidu.9ku.com/song/?key=%E7%A5%81%E9%9A%86')

bs = BeautifulSoup(response.text,'lxml')
lis =bs.select('#searchInfo > div.soMusic > div.songList > ul > li')
for li in lis:
    href = li.select('.play')[0].get('href')
    song = requests.get(href.replace('//','https://'))
    id = href.replace('//www.9ku.com/play/','').replace('.htm','')
    song_url = 'https://www.9ku.com/html/playjs/894/{}.js'.format(id)
    song_response = requests.get(song_url)
    json_text = song_response.text.replace("(",'').replace(')','')
    obj = json.loads(json_text)
    song_name = obj['mname']
    song_url = obj['wma']
    mp4_file_content = requests.get(song_url).content
    with open("music6/{}.mp3".format(song_name), "wb") as f:
        f.write(mp4_file_content)
