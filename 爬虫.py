import requests
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
sanguo=res.text
print(sanguo[:800])
