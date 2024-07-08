import requests


res = requests.get('http://127.0.0.1:5000/response/')

# res = requests.get('http://127.0.0.1:5000/request/?name=xia&name=xu&age=16',
#                    cookies={'name':'hello'}
#                    )
print(res.text)


# res = requests.post('http://127.0.0.1:5000/request/',data={'name':'lucky','age':33})
# print(res.text)