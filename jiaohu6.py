#用户输入 input（prompt）函数 向用户显示提示或说明 字符串
message=input('Which car do you live in?') #提示词prompt 等待用户输入确认后继续执行
print(f'That is wonderful!') #输入确认后的运行代码

# 多个prompt
promt=input('if you tell us who u r ,we can message u.')
promt +=('What is your name?')
name=input(promt)  #用name代替用户的输出内容
print(f'\nHi,{name.title()}')

#数值prompt int()
age=int(input('How old are you?'))
if age<18:
    print('You are young.')
# 求模运算符 %
number=int(input('Give me a number and I\'ll tell you if it\'s even or odd.'))
if number%2!=0:
    print('Even')
elif number%2==0:
    print('Odd')
# 7-1 租车
car=input('What type car do you want to rent?')
print(f'\nLet me see if i can find u a {car.title()}')

#7-2 餐馆订位
client=int(input('How many people do you have?'))
if client>8:
    print('We don\'t have enough space.')
else:
    print('We have enough space.')

#7-3 10的倍数
number=int(input('Yoou can give me a number and I\'ll tell you if it\'s a 10s.'))
if number%10==0:
    print('10s')
elif number%10!=0:
    print('Not 10s')

# while 循环 不断运行直到不满足条件 例如游戏闪退或持续运行直到玩家发出退出指令
current_number=1    #运行起点
while current_number<10:  #运行终点
    print(current_number)
    current_number +=2  #间距

#用户选择何时退出 一个条件使程序退出
prompt='\nTell me something,and i will repeat it back to you:' #prompt 提前写好的等待输出的提示词库
prompt+='Enter"quit" to end the program.'
message='' #记录用户输入 初始设置空字符串 能被while循环识别
while message!='quit': #用户输入与quit比较
    message=input(prompt)
    #显示提示消息 等待用户输入 并赋给message
    if message!='quit': #修复用户退出也有quit弹出的问题
        print(f'I\'m happy to see u {message}')

# 标志变量 flag 程序交通信号灯 True运行 false退出 很多事件导致程序运行停止的游戏
prompt='\nTell me something,and i will repeat it back to you:' #prompt 提前写好的等待输出的提示词库
prompt+='Enter"quit" to end the program.'
active=True #标志变量 初始程序为真 不需要比较
while active: #只要active为真 代码继续运行
    message=input(prompt)
    if message=='quit': #如果用户输入为quit就设置为false 循环停止
        active=False
    else:
        print(message)

#立刻退出while循环 while-true。。。break 语句 循环不断运行直到遇到break停止
#python任何循环都可以使用break
prompt='\nPlease enter the name of a city you have visited '
prompt+='\n(Enter "quit" when you are done)'
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print(f'I\'d love to go to {city.title()}')

# continue 跳回循环开头，并根据测试决定是否继续执行循环
current_number=1
while current_number<10:
    current_number=current_number+1
    if current_number%2==0:
        continue #例如到2468 触发continue 返回循环开头测试小于10 继续循环 直到9停止
    else:
        print(current_number)

#避免无限循环 按ctrl+c
x=1
while x<5:
    print(x)
#没有设置间隔 一直 循环111111

