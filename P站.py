import setting
import os
import requests
import re
import time

headers = {
    'cookie': 'PHPSESSID=4dceb06e7220f590131a097b051e18fe;',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
headers_img = {

    'Referer': 'https://www.pixiv.net/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
url = 'https://www.pixiv.net/ajax/user/7210261/profile/all'
name = re.sub('\D','',url)
print(name)
data = requests.get(url, headers=headers)

dic = data.json()

lt = list(dic.get('body').get('illusts').keys())
if lt:
    IMG_PATH = os.path.join(setting.PC_PXIMG_PATH,name)
    print(IMG_PATH)
    setting.mkdir_path(IMG_PATH)
    for index,i in enumerate(lt):
        img_url = f'https://www.pixiv.net/member_illust.php?mode=medium&illust_id={i}'
        data = requests.get(img_url, headers=headers).content.decode('utf-8')
        try:
            url = re.findall('"original":"(.*?)"', data, re.S)[0]  # type:str
            url = url.replace('\\/', '/')
            img = requests.get(url, headers=headers_img).content
            file_img = os.path.join(IMG_PATH,i+'.png')
            if os.path.exists(file_img):
                continue
            with open(file_img, 'wb') as fw:
                fw.write(img)
            print(f'第{index+1}张')
        except IndexError:
            print('URL错误！')
        time.sleep(0.2)