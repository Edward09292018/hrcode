import requests

# 使用requests爬取58同城租房信息
url = 'http://www.bluecore.com.cn/'
req = requests.get(url, timeout=5000)

html = req.content.decode('utf-8')
with open('蓝创首页.html', 'w+', encoding='utf-8') as f:
    f.write(html)
