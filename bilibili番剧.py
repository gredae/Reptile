import requests
import os
import re

def mkdir_path(path):
    #获取绝对路径
    path = os.path.abspath(path)
    if not os.path.exists(path):
        mkdir_path(os.path.dirname(path))
        os.mkdir(path)

PC_BILIFJ_VIDEO_PATH = r'E:\爬虫数据\哔哩哔哩\番剧'

mkdir_path(PC_BILIFJ_VIDEO_PATH)

ep = input('请输入番剧的ep号，暂不可爬取大会员番剧：').strip()
# B站的番剧是flv格式
file_name = os.path.join(PC_BILIFJ_VIDEO_PATH,ep+'.flv')
# 拼接番剧链接地址
url = fr'https://www.bilibili.com/bangumi/play/{ep}'
# 两种请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

headers_4_3 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Origin': 'https://www.bilibili.com',
        'Referer': url,   # 跳转地址，是从什么地方过来的
    }
# 获取番剧页面
data = requests.get(url,headers = headers).text
# 通过re获取番剧的播放地址
url = re.findall(r'"backup_url":\["(.*?)"',data,re.S)[0]
if url:   # 如果找不到这个番剧的url就不进行爬取
    # 爬取视频
    data = requests.get(url,headers = headers_4_3)
    # 将视频写入文件
    with open(file_name,'wb') as fw:
        fw.write(data.content)
else:
    print('抱歉，找不到视频链接！')

