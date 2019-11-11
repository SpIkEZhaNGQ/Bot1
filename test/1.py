#import base64
#import cv2
#dict= {'hi':'hii'}
#Img = open('D:\downloads\sdff.png', 'rb')
#base64_img = base64.b64encode(Img.read())
#qq = str(bytes(base64_img), encoding='utf-8')
#qqq = 'img src=data:image/png;base64,'+qq
#qqqq = bytes(str(qqq), encoding='utf8')

#dict['qqqq'] = str(qqqq)
#out = dict['qqqq']
#print(out[0:100])

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '17749281'
API_KEY = 'EhIObLQzyXZgrVYxgCIhnZB2'
SECRET_KEY = 'AYwWjFF3OOI7EEs3tqXnguF6b5Gmifq3'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
a = 'how are you?'
result  = client.synthesis(str(a), 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)