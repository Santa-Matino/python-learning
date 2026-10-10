#字典 动态结构 {}
from lib2to3.pygram import python_grammar
alien_0 = {'color':'green','points':10}  #键值对 键：值，键：值
print(alien_0['color']) #访问值 指定 （字典名【键】）
print(alien_0['points'])
new_points=alien_0['points']
print(f'you jiust eared {new_points}')
#添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#创建空白字典
alien_0={} #{}
alien_0['color']='green'
alien_0['points']=10
print(alien_0)
#修改值
alien_0={'color':'black'}
print(f'This alien is {alien_0["color"]}')
alien_0['color']='green'
print(f'The alien is now {alien_0["color"]}')
#例子：位置跟踪
alien_0={'x_position':7,'y_position':25,'speed':'fast'}
print(f'Original position:{alien_0["x_position"]}')
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=x_increment+alien_0['x_position']
print(f'The alien new position is: {alien_0["x_position"]}')
#删除键值对 del 永久删除
alien_0={'color':'green','points':10}
print(alien_0)
del alien_0['points']
print(alien_0)

#多行字典
favorite_languages={
    'jen':'python',
    'sar':'c',
    'edward':'ruby',
    'phil':'python',#最后也加，为后续添加准备
    } #缩进4字符
language=favorite_languages['sar']
print(f'Sara favorite language is {language.title()}')

#方法get() 如果指定键可能不存在可以用get测试
alion_0={'color':'green','points':10}
#指定键不存在 输出后面语句 在数据量很大时快速查找是否存在而不会报错【键】
point_value=alion_0.get('speed','No speed value assigned.')
print(point_value)

#6-3
python_grammar={'print':'dayin','len':'buchang'}
print(f'print:{python_grammar["print"]}\nlen:{python_grammar["len"]}')

#遍历所有键值对
alien_0={'color':'green','points':'10'}
for key,value in alien_0.items(): #items 键值对
     print(f'\nKey:{key.title()}')
     print(f'Value:{value.title()}')

#遍历字典默认遍历所有键 或 用keys()
alien_0={'color':'green','points':'10'}
for k in alien_0.keys():  # 或不用.keys()
     print(f'\n{k.title()}')
# 使用当前键来访问值
favorite_languages={
    'jen':'python',
    'sar':'c',
    'edward':'ruby',
    'phil':'python',#最后也加，为后续添加准备
    }
friends=['sar','phil'] #定义了一个新列表
for name in favorite_languages.keys(): #for遍历所有 键 赋值给name
    print(f'\nHi,{name.title()}')
    if name in friends:
        language=favorite_languages[name].title() #符合条件的值 赋给language
        print(f'\n{name.title()},I see you love {language.title()}')

# keys() 能返回一个列表包含字典中的所有键
favorite_languages={
    'jen':'python',
    'sar':'c',
    'edward':'ruby',
    'phil':'python',#最后也加，为后续添加准备
    }
if 'erin'not in favorite_languages.keys():
    print('Sorry, I don\'t understand your favorite language.')

#  按特定顺序遍历字典中的所有键
favorite_languages={
    'jen':'python',
    'sar':'c',
    'edward':'ruby',
    'phil':'python',#最后也加，为后续添加准备
    }
for name in sorted(favorite_languages.keys()): # sorted函数 按字母正序临时排序
    print(f'\n{name.title()},Thanks for taking the poll. ')

#遍历字典中的所有值 方法values（）返回一个值列表
for language in favorite_languages.values():
    print(f'\n{language.title()}')
# 集合set 将value提取的值列表中的重复项剔除 在大数据场景好用
for language in set(favorite_languages.values()):
    print(f'\n{language.title()}') # 输出没有最后的python 被剔除
# 集合 ≠ 字典 集合不会以特定顺序存储元素
numbers={'1','2','3','4','5','6','7','8','9'} #集合用花括号 逗号间隔

#6-4 6-3改良
python_grammar={'print':'dayin','len':'buchang'}
for key,value in python_grammar.items():
    print(f'\n{key.title()}:{value.title()}')
#6-5
river_nation={'huanghe':'china','cahngjiang':'china','nile':'egypt'}
for key,value in river_nation.items():
    print(f'\nThe {key.title()} runs through {value.title()}.')
#6-6
favorite_languages={
    'jen':'python',
    'sar':'c',
    'edward':'ruby',
    'phil':'python',#最后也加，为后续添加准备
    }
people=['fred','sar','harry','phil','max']
for person in people:
    if person in favorite_languages.keys():
        print(f'{person.title()} thanks for this investigate.')
    else:
        print(f' We investigate {person.title()} to our test .')

#嵌套 列表嵌套字典
alien_0={'color':'green','points':10}
alien_1={'color':'yellow','points':5}
alien_2={'color':'red','points':7}
aliens=[alien_0,alien_1,alien_2] #3个字典嵌套进一个列表
for alien in aliens:
    print(alien)

# 创建一个嵌套30个外星人的列表
aliens=[]
for alien_number in range(30):  #告诉python循环多少次
     new_alien={'color':'green','points':10}
     aliens.append(new_alien)
     # 虽然每个都相同但是python认为每个都是独立的 可以独立修改每个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
print(f'Total number of aliens: {len(aliens)}')

# 修改外星人 前三个修改为 黄色 15分
for alien in aliens[:3]:
    if alien['color']=='green': #可能不全是绿色 所以if确定
        alien['color']='yellow'
        alien['points']=15
    if alien['color']=='yellow':
        alien['color']='red'
        alien['points']=8
for alien in aliens[:5]:
    print(alien)
print('...')

#字典中嵌套列表
pizza={'crust':'thick',
       'topping':['mushroom','extra cheese'] # 一个键关联多个值 用列表
       }
print(f'You owerdered a {pizza["crust"]}-crust pizzza '
      'with the following topping:')
for topping in pizza['topping']:
    print('\t'+topping)

#字典中存储字典
users={
    'H':{
        'first':'harry',
        'last':'de suza',
        'locaion':'london',
         },
    'CT':{
        'first':'charlotte',
        'last':'de white',
        'locaion':'armstedan',
         },
    }
for user,user_info  in users.items():
    print(f'\nUsername:{user}')
    full_name=f'{user_info['first']} {user_info['last']}'
    location=user_info['locaion']
    print(f'\tFull name:{full_name.title()}')
    print(f'\tLocation:{location.title()}')

#6-8
pet1={'type':'keji','host':'harry'}
pet2={'type':'pika','host':'fred'}
ppet3={'type':'hasiki','host':'edwd'}
pets=[pet1,pet2,ppet3]
for pet in pets:
    print(pet)

#6-9
favorite_places={'harry':['shanghai'],
                 'fred':['paris','tokyo'],
                 'charlotte':['yokohama','rome','kingston'],
                 }
for name,places in favorite_places.items():
    print(f'\n{name.title()} favorite places:')
    for place in places:
        print(f'\t{place.title()}')

#6-11
cities={
    'shanghai':
        {'nation':'china',
         'population':'10000',
         'fact':'beautiful'},
    'tokyo':
        {'nation':'japan',
         'population':'1990',
         'fact':'nice'},
    'paris':{'nation':'france',
             'population':'2000',
             'fact':'luxury'},
        }
for city,places_info in cities.items(): #for循环 做第一个 其他复制
    print(f'\n{city.title()} "s information:')
    for place_1,place_2 in places_info.items():
        print(f'\t{place_1.title()}: {place_2.title()}')







