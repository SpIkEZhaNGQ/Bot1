import urllib.request
import urllib.error
import json
import base64
import cv2

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

#Img = open('D:\downloads\sdff.png', 'rb')
#base64_img = base64.b64encode(Img.read())
#qq = str(bytes(base64_img), encoding='utf-8')
#qqq = 'data:image/png;base64,'+qq
#qqqq = bytes(str(qqq), encoding='utf8')
params = {}
params["image"] = str('https://img-blog.csdnimg.cn/20190424143728874.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2EzMTI4NjMwNjM=,size_16,color_FFFFFF,t_70')
params["image_type"] = "URL"
params["face_field"] = "faceshape, facetype, expression"
params = bytes(str(params), encoding='utf8')


#params = b"{\"image\":\"qqqq\",\"image_type\":\"BASE64\",\"face_field\":\"faceshape,facetype,expression\"}"

access_token = '[24.a4bd4dc7a6dd951b3fc73897eb3b8a1a.2592000.1574891061.282335-17630942]'
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/json')

response = urllib.request.urlopen(request)
result_all = response.read().decode("utf-8")
result = json.loads(result_all)
#Out_put_ans = result['result']
#ans = Out_put_ans['face_list']
#next_ans = ans[0]
#face_type = next_ans['face_type']

print (result)

#content = response.read()
#if content:
   # print(content)