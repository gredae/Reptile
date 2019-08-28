import requests
import re
import uuid

'''图片'''
# for i in range(46):
#     path = f'http://www.xiaohuar.com/list-1-{i}.html'
#     data = requests.get(path).text
#     data = re.findall('/(d/file.*?.jpg)',data,re.S)
#     for i in data:
#         path ='http://www.xiaohuar.com/'+i
#         print(path)
#         img = requests.get(path).content
#         img_path = os.path.join(r'E:\图片',re.split('/',i)[-1])
#         with open(img_path,'wb') as fw:
#             fw.write(img)

'''视频'''

def save(url):
    response = requests.get(url=url)
    data = response.content
    file_name = fr'E:\SP\{str(uuid.uuid4()).replace("-","")+".mp4"}'
    with open(file_name,'wb') as fw:
        fw.write(data)
        print(file_name,'下载已完成')

count = 0
for i in range(6):
    data = requests.get(f'http://www.xiaohuar.com/list-3-{i}.html').text
    urls = re.findall('<a class="imglink" href="(.*?)" target="_blank"',data,re.S)
    for url in urls:
        data = requests.get(url).text
        url = re.findall('<source src="(.*?)"',data)
        if url:
            url = url[0]
            if 'http://xiaohuar.oss-cn-beijing.aliyuncs.com' in url:
                print(url)
                save(url)
print(count)

