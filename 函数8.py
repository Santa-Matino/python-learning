#定义函数并传递信息
def greet_user(username): # 定义函数
    '''显示简单的问候语'''  #文档字符串doctoring 解释函数作用
    print(f' Hello, {username.title()}')  #函数体
greet_user('harry de suza') #调用函数

# 形参 'username' 函数完成工作所需的信息  函数定义中的变量
# 实参 ‘harry’ 调用用函数时传递给函数的信息 函数调用中的变量

#传递实参
#位置关联实参 根据形参变量的先后顺序 赋值实参
def describe_pet(animal_type,pet_name='matt'): #形参默认值Matt
    '''显示宠物信息'''
    print(f'I have a {animal_type.title()}')
    print(f' My {animal_type.title()}\'s name is {pet_name.title()}')
describe_pet('hamster', 'harry') #位置实参
describe_pet('dog','matt') #多次调用函数 效率极高
describe_pet(animal_type='tiger',pet_name='mike')  # 关键字实参
describe_pet('pig') #使用了默认值 默认宠物名字是Matt

#8-3
def make_shirt(size='XXXL',type='i love python'):
    print(f'The {type.title()} t-shirt has a {size.title()}')
make_shirt(type='i love u')

#返回值 return语句 处理数据不直接输出
def get_formatted_name(first_name,last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()   #将结果返回到函数调用行
musician=get_formatted_name('harry', 'de suza') #调用返回值函数提供变量
print(musician)
#相比于不用return的直接print return可以存储数据 直接调用 比如把名字存进musician变量中
# 这个函数中的形参和实参相当于榨汁机送水果的管道入口
#full相当于榨汁过程 return相当于底盘漏斗 musician是杯子
#你的输入是水果 杯子被存起来贴上musician封条 已备调用

#实参可选
def get_formatted_name(first_name,last_name,middle_name=''):#空字符
    if middle_name: #如果有中间
        full_name = f'{first_name} {middle_name} {last_name}'
    else: #没有
        full_name = f'{first_name} {last_name}'
    return full_name.title()
musician1=get_formatted_name('harry','suza','de')
#中间名是最后一个实参
print(musician1)
musician2=get_formatted_name('marxu','makangna')
print(musician2)

# 返回字典 实参可选
def build_person(first_name,last_name,age=''): #用一个空键值对站位 显示false
     person={'first_name':first_name,'last_name':last_name}
     if age: # 如果有输入为真启用
         person['age']=age #在字典person中添加一个新键值对
     return person
musician=build_person('harry','de suza','35')
print(musician)

#函数与while循环联动 混合榨汁店
def get_formatted_name(first_name,last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()
while True:
    print('\nPlease tell me your name:(enter "quit" to quit)')
    name1=input('First name: ')
    if name1=='quit': break
    name2=input('Last name: ')
    if name2=='quit': break
    formatted_name=get_formatted_name(name1,name2)
    print(f'Hello, {formatted_name}')
# 把输入交给用户 实现交互 并能存储进full

#8-6
def city_nation(name,country):
    print(f'The {country.title()} city is {name.title()}')
city_nation('New York',"USA")
city_nation('London',"UK")

#8-7
def make_album(singer,album,time=None):
    music={'singer':singer,'album':album}
    if time:
        music['time']=time
    return music
while True:
    print('\nPlease tell me your album:(enter "quit" to quit)')
    singer_name=input('Enter your singer name: ')
    if singer_name=='quit': break
    album_name=input('Enter your album name: ')
    if album_name=='quit': break
    album_time=input('Enter your album time: ')
    if album_time=='quit': break
    toto_album=make_album(singer_name,album_name,album_time)
    print(toto_album)



