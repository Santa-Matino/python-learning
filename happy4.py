#if语句 检查当前程序状态 并采取措施
cars='audi','bmw','toyota','subaru'
for car in cars:
    if car=='bwm':
        print(car.upper())  #处理特殊情形
    else:
        print(car.title())  #处理大多数情况

#条件测试 if的核心是True或False
#检查是否相等
car='bmw' # =陈述
car=='audi' # false。#==发问 #大小写不同也不想等
# 忽略大小写问题 网站用类似测试确保用户名独一无二
car='Audi'
car.lower()=='bmw' #True

#检查是否不想等  可用数比较
request_topping=['mushrooms','beheve']
for request in request_topping:
    if request!='anchoives':  #!=不等于
      print('Hold the anchoives!')

#检查多个条件 and or
#检查特定值在不在列表中  in  notin
#布尔表达式 条件测试别名 记录条件 如用户是否可以编辑 游戏是否运行
#练习5-1
car='subaru'
print('Is car=="subaru"? I predict true ')
print(car=='subaru')
#5-2
words='i like you '
wordss='i dont like you '
print(words!=wordss) #字符串测试
#5-3
number1=18
number2=20
print(number1>=20 or number2>=20)
#5-4
numbers=['1','2','3']
print('1' in numbers)
print('2' not in numbers)

#### if-elif-else 测试一个条件 满足跳过其他步骤
age=67
if age<4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f'your cost is ${price}')
#省略else 只要不满足if或elif 代码都会执行 应考虑用elif 代替else 就可以肯定仅当满足条件才会执行
age=67
if age<4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f'your cost is ${price}')
# 测试多个条件 if-if-if
request_topping='apple','banana','orange'
if 'apple' in request_topping:
    print('Adding apple')
if 'banana' in request_topping:
    print('Adding banana')
if 'orange' in request_topping:
    print('Adding orange')
print('\nFinished making your pizza')
# 只要执行一个代码块就if- elif- else 否则if- if- if
#5-3
alien_color='red','yellow','green','blue'
if 'red' in alien_color:
    print('You just earned 5 points')
#5-4
alien_color='red','yellow','green','blue'
if 'yellow' not in alien_color:
    print('You just earned 5 points')
else:
    print('You just earned 10 points')

#if 处理列表
request_toppings=['apple','banana','orange']
for request in request_toppings:
    if request=='banana':
        print('Sorry we are out of banana')
    else:
        print(f'Adding {request}')
print('\nFinished making your pizza')
# 列表为空
request_toppings=[]
if request_toppings:# 先检查列表是否为空 为空执行else 不为空执行for循环
    for request in request_toppings:
        print(f'Adding {request}')
    print('\nFinished making your pizza')
else:
    print('You sure you want a plain pizza?')

# 使用多个列表
aviliable_toppings=['apple','banana','orange']
request_toppings=['apple','cheese','orange']
for request_topping in request_toppings:
    if request_topping in aviliable_toppings:
        print(f'Adding {request_topping}')
    else:
        print(f'We dont have {request_topping}')
print('\nFinished making your pizza')

#5-8
guest_names=['edwd','chalies','harry','fred','admin']
login_names=['edwd','admin','chalies']
vip_names=['admin','edwd']
if guest_names==[]:
    print('No guests yet')
else:
    for login_name in login_names:
       if login_name in vip_names:
          print(f'Hello {login_name} ,your grace!')
       else:
        print(f'Hello  {login_name} ,welcome back!')

#5-9 网站用户名未被使用
current_users=['eDw','chaR','haRry','Fred','adMiN'] #历史用户名列表
lower_current_names=[] #准备一个小写列表空集
for name in current_users: # for循环
    lower_current_names.append(name.lower()) # 把历史用户名小写放入空集中 形成与历史用户名相同的小写副本
new_users=['WeLl','HaRry','fRed','AdEn','aMy'] # 新用户名
for new_user in new_users:
    new_low=new_user.lower() #生成一个小写新用户集
    if new_low in lower_current_names: #对比两个完全小写
        print(f'Hello {new_user} ,your name was used') #被使用 注册失败
    else:
        print(f'Hello {new_user} ,your name was not used')#未被使用 注册
        current_users.append(new_user) #通过的名字放入历史用户中
        lower_current_names.append(new_low) #小写副本
print('\n Thanks for login')
print('\ncurrent_users=',current_users) #更新新的历史用户
print('\nlower_current_names=',lower_current_names) #更新小写集

#5-11
numbers=list(range(1,10))
for number in numbers:
    if number==1: # 不用‘1’ 这表示字符 你需要读取数字 ####字符≠数字
        print('1st')
    elif number==2:
        print('2nd')
    elif number==3:
        print('3rd')
    else:
        print(f'{number}th')

# if格式
#if空格age空格<4


