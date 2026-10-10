#定义两个整型变量 求两个变量和 打印结果
name1=30
name2=50
name3=name1+name2
print(name3)
#定义两个整型变量 比较值 打印结果
name1=60
name2=50
if name1<=name2:
    print('name1<=name2')
else:
    print('name1>name2')


#编写一个程序，该程序用于计算从1到100（包含1和100）所有整数的和，并将结果打印出
#sum内置函数版 只想求和中间不做其他
sum_numbers=sum(range(1,101))
print(sum_numbers)
#for循环版 中间需要额外工作 比如for里要 判断if i % 2 ==0 或 打印 print（i）
total=0
for i in range (1,101):
    total += i
print(total)
#进阶写法 生成器表达式
print(sum(i for i in range (1,101)))


#有四个数字：1、2、3、4，统计能组成多少个互不相同且无重复数字的三位数？各是多少？
#我的解法 两个问题没有解决 1 while true循环没有设置停止点 2 输出3位数中有重复数字 3没有计数
numbers=['1','2','3','4']
new_numbers=numbers[:] #神点子 用副本pop不破坏原有的数据列表
while True:
    number_pop=new_numbers.pop()
    if not new_numbers: break #问题1解决
    for number2 in numbers:
        add_number=f'{number_pop}{number2}'
        for number3 in numbers:
            final_number=f'{number_pop}{number2}{number3}'
            print(final_number) #问题2 切换思路 放弃pop 很繁琐
#新解法 三层for- if循环 原理设置百十个位 ABC if验证互不相等
numbers=['1','2','3','4']
count=0 #计数变量
for bai in numbers:
    for shi in numbers:
        for ge in numbers:
            if bai != shi and shi!=ge and bai!=ge:
                num=bai+shi+ge
                print(num)
                count+=1
print('we have:',count)
#python内置库专门算排列 itertools.permutations
import itertools
nums=['1','2','3','4']
for item in itertools.permutations(nums,3):
    print(''.join(item))
#while-pop 解法 不推荐 非常繁琐
numbers=['1','2','3','4']
new_numbers=numbers[:]
count=0
while True:
    if not new_numbers: break #一定放在开头 先if再pop 不然会缺少数据百位为1的6个数据 最后剩【1】先pop弹出 剩空集不运行
    a=new_numbers.pop() #设置百位数字
    candidate_b=[x for x in numbers if x!=a] #列表解析式 高级写法 备选十位列表
    for b in candidate_b: #提取十位数
        candidate_c=[x for x in numbers if x!=a and x!=b] #备选个位列表
        for c in candidate_c: #提取个位数
            num=a+b+c #三位数组合
            print(num)
            count+=1 #计数+1
print('we have:',count)



#编写一个程序，该程序用于打印9*9乘法口诀表
#首先观察一个乘法表 他是a*b=c a是1-9 b是1-a c是结果
for a in range(1,10):  #循环1-9
    for b in range(1,a+1): #1-a 差1 原理 A+1=A
        c=a*b
        print(f'{b}*{a}={c}',end='\t') #注意交换了ab顺序 为了输出效果
        # 以为print本身每执行一次自动默认换行 所以end=‘’代码意思是内循环内不换行
    print() #一个内循环结束 换行


#编写一个程序，该程序用于找出并打印所有的水仙花数。
#水仙花数：指一个三位数，其各位数字立方和等于该数本身。如：1³ + 5³ + 3³ = 153。
#解法1 拼装法
count=0
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            num=a*100+b*10+c
            if num == a**3+b**3+c**3:
                print(num)
                count+=1
print('we have:',count)
#解法2 拆解法 降维打击
for num in range(100,1000): #界定三位数的起始和终到 去不到100和1000 完美
    a = num // 100 #例如 153 整除 100 得1 为百位数 余数53
    b = num // 10 % 10 #153 整除10 得15 余3 15除10取余数为5 为十位
    c = num % 10  #153 除10取余数3 为个位
    if num == a**3+b**3+c**3:
        print(num)

#猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个，第二天早上又将剩下的桃
#子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个，到第10天早上想再吃时，
#见只剩下一个桃子了，求第一天共摘了多少个。
peach=1
for i in range (9): #存结果的变量peach不要用来当for循环的迭代变量 9为0-8 9次
  peach=(peach+1)*2
print(peach)
