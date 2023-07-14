import requests as req
data = req.get('https://www.py4e.com/code3/tracks/Library.xml')
with open('D:\python-databases\Library.xml','w') as f:
    f.write(str(data.text))
print('data done')