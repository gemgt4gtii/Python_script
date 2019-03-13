from bs4 import BeautifulSoup                       #---
import requests                                     #    }   引用套件
from pytube import YouTube                          #---
def get_urls(url):                                  #定義一個函式 取得播放清單的網址
    urls=[]                                         #播放清單網址
    if '&list=' not in url : return urls            #單一影片
    response = requests.get(url)                    #定義變數 = 引用套件發出請求()
    if response.status_code != 200:                 #假如回傳 200
        print('請求失敗')
        return
    bs = BeautifulSoup(response.text,'lxml')        #定義變數 = 解析網頁
    a_list = bs.find_all('a')                       #定義變數 = 引用套件找出網頁碼所有的 <a> 標籤 
    base = 'https://www.youtube.com/'               #定義變數 = 網址
    for a in a_list:                                #for迴圈
        href = a.get('href')                        #定義變數 = 取得 <a> 的 href 屬性內容
        url = base + href                           #主網址結合href屬性內容才是完整的影片網址
        if ('&index=' in url ) and (url not in urls):   #if判斷 
            urls.append(url)
    return urls
sing_url = 'https://www.youtube.com/watch?v=-O_75Sm1dXY&list=PLGzC4gTcebz_o69e7GSAW25FPixEGy9OT&index=2&t=0s' #定義變數 = '完整網址'
playlist_url = ('https://www.youtube.com/watch?v=-O_75Sm1dXY'                                                 #定義變數 = '影片網址' '播放清單網址'          
               '&list=PLGzC4gTcebz_o69e7GSAW25FPixEGy9OT&index=2&t=0s')
urls = get_urls(playlist_url)
for url in urls:
    yt = YouTube(url)
    print(f'{yt.title}...下載中')
    yt.streams.first().download('C:\Downloads')
    print(f'{yt.title}...下載完成')