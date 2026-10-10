#程序把用户输入的信息存储在数据结构中 如字典 列表 保存用户信息
#json模块存储共享数据
#json.dump 存储
#json.load 调取
#存储列表
import json #调用模块
numbers=[2,3,4,5,6,7,8,9]
filename='numbers.json' #指定存储文件
with open(filename,'w') as f:
  json.dump(numbers,f) #数字列表存储进文件。json中

#列表读取到内存  程序间简单共享数据
import json
filename='numbers.json' #读取前面写入文件
with open(filename) as f: #只读方式打开
  numbers=json.load(f) #加载存储信息进变量
print(numbers) #打印

#保存读取用户生成数据
import json
filename='username.json'
try:
  with open(filename) as f:
    username=json.load(f)
except FileNotFoundError:
  username=input('what is your name?')
  with open(filename,'w') as f:
    json.dump(username,f)
    print(f'we will remember your name {username}')
else:
  print(f'welcome back  {username}')

#重构 将代码划分为一系列具体工作的函数
#使用一个函数
import json
def greet_user():
  filename = 'username.json'
  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    username = input('what is your name?')
    with open(filename, 'w') as f:
      json.dump(username, f)
      print(f'we will remember your name {username}')
  else:
    print(f'welcome back  {username}')
greet_user()
#问候 存储的获取 没存储的提示

#重构使用多个函数
import json
def get_stored_username():
  filename = 'username.json'
  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    return None
  else:
    return username
def greet_user():
  username = get_stored_username()
  if username:
    print(f'welcome back {username}')
  else:
    username = input('what is your name?')
    with open(filename, 'w') as f:
      json.dump(username, f)
      print(f'we will remember your name {username}')
greet_user()
