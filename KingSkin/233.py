import requests
import turtle
import pickle


#开始进入Python的世界
print('Api：1.墨天逸 2.韩小韩 3.樱花 4.小歪')
api = int(input('请输入API的数字来选择背景图片来源'))
if (api == 1):
    print('墨天逸Api')
    f = requests.get('http://api.mtyqx.cn/api/random.php')
    with open("./Pictures/00.jpg","wb") as code:
        code.write(f.content)
if (api == 2):
    print('韩小韩Api')
    f = requests.get('https://api.vvhan.com/api/acgimg')
    with open("./Pictures/00.jpg","wb") as code:
        code.write(f.content)
if (api == 3):
    print('樱花Api')
    f = requests.get('https://www.dmoe.cc/random.php')
    with open("./Pictures/00.jpg","wb") as code:
        code.write(f.content)
if (api == 4):
    print('小歪Api')
    f = requests.get('https://api.ixiaowai.cn/api/api.php')
    with open("./Pictures/00.jpg","wb") as code:
        code.write(f.content)