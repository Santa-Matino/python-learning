#伟大的 ！！！for循环 循环并提取
magicans=['alic','davi','carolina']
for magican in magicans:
    print(f'{magican.title()},that was a great trick!')
    print(f'I can"t wait to see your next trick, {magican.title()}.\n')
print('Thank you every one, That was a great magic show!')
# 锁缩进错误 漏掉冒号
magicans=['alic','davi','carolina']
for magican in magicans:
    print(f'{magican.title()},that was a great trick!') # 一般for循环下第一条代码缩进会减少大量错误概率

magicans=['alic','davi','carolina']
for magican in magicans:
    print(f'{magican.title()},that was a great trick!')
print('I cant wait to see your next trick, {magican.title()}.\n') #代码不会报错 但是与本意偏离
#练习4-1
pisa_like=['apple','banana','orange']
for pisa in pisa_like:
    print(f'{pisa.title()}pisa,that was a dilicious food!')
print('I really love pisa!.\n')
#练习4-2
animals=['dog','cat','rabbit','dog','cat']
for animal in animals:
    print(f'A {animal.title()} is a great pet!')
print('I really love them all!')


# 数字列表
#range函数
for value in range(1,5):
    print(value) #输出1-4 差一行为结果
for value in range(6):
    print(value) #输出0-5 从0开始

#list 函数 将range函数中的数字放进列表中
numbers=list(range(1,6))
print(numbers)
# 步长 打印1-10的偶数
evevn_numbers=list(range(2,11,2))
print(evevn_numbers)
#创建一个列表包含1-10的平方
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#数字列表统计 min max sum
digits=[1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))
#列表解析
squares=[value**2 for value in range(1,11)]# 列表名【表达式 for循环变量值range（）】#无冒号
print(squares)
#练习 4-3
for ox in range(1,21):
    print(ox)
#exercise4-4
numbers=range(1,10)
for number in numbers:
    print(number)
#exercise 4-5
numbers=range(1,10)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# exercise 4-6
numbers=list(range(1,21,2))
for number in numbers:
    print(numbers)
#exercise 4-7
number=list(range(3,31,3))
for number in number:
    print(number)
#exercise4-8 立方解析
squares=[value**3 for value in range(1,10)]
print(squares)
#exercise 4-9
squares=[]
for value in range(1,10):
    squares.append(value**3)
print(squares)

#切片
players=['charls','wed','marko','kings','shart','james','kobi','kuri']
print(players[1:4]) #与range一样 差一
print(players[:3]) #无起始索引 从头开始前三位
print(players[2:]) #无终止索引 提取到尾
print(players[-3:]) # 提取后3个元素=【1:】
print(players[0:9:3]) #制定第三值  间隔
print(players[:]) # 头到尾
#遍历切片 WEb应用 分页显示信息 并显示合适数量
plyers=['charls','wed','marko','kings','shart','james']
print('Here are the first three players:')
for player in plyers[:-1]:
    print(player.title())

#复制列表
my_foods=['apple','banana','orange']
friend_foods=my_foods[:] #  ≠my_foods 可以试着运行一下
my_foods.append('piza')#注意结果 没有在两个都存在
friend_foods.append('chicken')#注意结果 没有在两个都存在
print(f'my favorite foods are \n{my_foods}.\n')
print(f'my friend favorite foods are\n{friend_foods}')

#练习4-10
players=['charls','wed','marko','kings','shart','james']
print(f'the first three players are:\n{players[:3]}.')
print(f' three itrems from the middle of the list are:\n{players[1:4]}.')
print(f'the last three players are:')
for player in players[-3:]:
    print(player.title())

#元组 不能改变的列表
dimensions=(100,50)
print(dimensions[0])
print(dimensions[1])

my_t=(7,)# 单元素元组用，结尾
#遍历元组
dimensions=(100,50)
for dimension in dimensions:
    print(dimension)# 也能用for循环遍历
#修改元组变量
dimensions=(100,50)
print(dimensions)
dimensions=(150,100)# 可以重新复制 定义元组
print(dimensions)

#练习4-13
foods=('apple','banana','orange','dumplings','rice')
for food in foods:
    print(food)

foods=('apple','duck','chicken','dumplings','rice')
for food in foods:
    print(food)
#代码格式
#缩进 4个空格= \t 同一份代码 尽量使用一种 全4空or全\t
#行长 小于80个字符
#空行 一个 不影响可读性
