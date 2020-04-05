Python实现的短网址服务, Web框架为Flask  

## 本地运行  
1. 安装依赖  
```shell script
pip install -r requirements.txt
```

2. 运行
```shell script
python manage.py
```

## Usage
#### Long -> Short

Shell:
```shell script
# 返回json
curl http://127.0.0.1:5000/shorten -d '{"url":"baidu.com"}'  --header "Content-Type:application/json"
# 返回html
curl http://127.0.0.1:5000/shorten -d 'url=baidu.com'
```

Python:  
```python
import requests
url = 'http://127.0.0.1:5000/shorten'

headers = {
    'content-type': 'application/json'
}

data = {
    'url': 'baidu.com'
}

# 返回json
r = requests.post(url, json=data, headers=headers)
# 返回html
r = requests.post(url, data=data)
```

return json:  
```json
{"expand":"http://baidu.com","shorten":"http://127.0.0.1:5000/867nv"}
```


##### Short -> Long

shell: 
```shell script
# 返回json
curl http://127.0.0.1:5000/expand -d '{"shorten":"http://127.0.0.1:5000/867nv"}'  --header "Content-Type:application/json"
# 返回html(跳转)
curl http://127.0.0.1:5000/867nv
```

Python:  
```python
import requests
headers = {
    'content-type': 'application/json'
}

data = {
    'shorten': 'http://127.0.0.1:5000/867nv'
}

# 返回json
r = requests.post('http://127.0.0.1:5000/expand', json=data, headers=headers)

# 返回html
r = requests.get('http://127.0.0.1:5000/867nv', allow_redirects=True)
```