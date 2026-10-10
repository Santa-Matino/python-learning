#7-4
prompt='\nu can enter your wanted toppings'
prompt +='\nEnter "stop" when you are done.'
active=True
while active:
    topping=input(prompt)
    if topping=='stop':
        active=False
    else:
        print(topping)

#7-5
prompt='\nCan u tell me how old are you?'
prompt +='\nEnter "stop" when you are done.'
while True:
    user_age=input(prompt)
    user_age_number=int(user_age)
    if user_age=='stop': #这里不能用文本字符串 因为int会把文本强制转换为数字 所以可以用一个0
        break
    elif user_age_number<3:
        print('You are free')
    elif user_age_number<12:
        print('You cost $10')
    else:
        print('You cost $15')

#while 循环处理列表和字典
# 列表之间移动元素 pop()
unconfirmed_user=['harry','edwd','fred','alice']
confirmed_user=['charlotte','manny']
while unconfirmed_user: # 循环到空列表结束
    new_confirmed_user=unconfirmed_user.pop()
    confirmed_user.append(new_confirmed_user)
print('\nThe following users have been confirmed:')
for new_confirmed_user in confirmed_user:
    print(new_confirmed_user.title())

# 删除列表特定值 remove只能删一次一个太慢 可以用while=remove✖️n
pets=['dog','cat','rabbit','cat','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
responses={}
while True:
    name=input('\nWhat is the name?')
    response=input('\nWhat is your favorite color?')
    responses[name]=response #填充空白字典
    repeat=input('\nWould you like to let your friends respond it?(yes/no)')
    if repeat=='no':
        break
print('\n---Poll Results:---')
for name,response in responses.items():
    print(f'{name} \'s favorite color is {response}')

#7-8
sandwich_order=['chicken','beef','ponk','beef','beef']
finished_sandwich=[]
while sandwich_order:
    new_sandwich=sandwich_order.pop()
    print(f'\n we made your {new_sandwich} sandwich.')
    finished_sandwich.append(new_sandwich)
for sandwich in finished_sandwich:
    print(f'we all done these: {sandwich} sandwich.')

#7-10
favorite_places={}
while True:
    name=input('\nWhat is your name?')
    response=input('\nWhat is your favorite place?')
    favorite_places[name]=response
    repeat=input('\nWould you like to let your friends respond it?(yes/no)')
    if repeat=='no':
        break
for name,response in favorite_places.items():
    print(f'{name} \'s favorite place is {response}')