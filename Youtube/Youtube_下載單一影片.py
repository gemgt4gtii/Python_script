from pytube import YouTube                          #引用套件

url='https://www.youtube.com/watch?v=sg_WE0ToJjM'   #宣告變數 = '網址'
yt=YouTube(url)                                     #套件名稱=YouTube(網址)
print('開始下載')
yt.streams.first().download('C:\Downloads')         #套件名稱.streams.first().download('儲存路徑')
print('下載完成')