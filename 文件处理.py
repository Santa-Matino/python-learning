####文本文件一次性读取打印
with open('learning_python.txt')as file_object:
    #open打开文件函数 close手动关闭 with随时访问自动关闭
    text = file_object.read()
    #read方法 读取文本内容将其作为一个长字符串赋给变量
print(text.strip())
#输出多一行空行 read到达文件末尾返回一个空字符串 可以用strip删除

#open在当前执行文件.py目录中查找
#python相对文件路径查找在pycharm目录中的某一个文件夹里的文件
#with open('text_files/filename.txt')as file_object

#python绝对文件路径查找任意位置的文件 将路径赋给变量再打开
#例如file_path='/home/matthes/other_files/text_files/filename.txt
#with open=(file_path) as file_object
#在文件路径中用反斜杠\引发错误 反斜杠用于字符串中的字符转义或识别为制表符 一定使用时对反斜杠转义\\

###逐行读取for
filename= 'learning_python.txt'  #变量并非实际文件 指示python查找文件字符串 因此可以随意替换‘’里文件名称
with open(filename)as file_object: #实际文件及内容
    for line in file_object: #遍历每一行
        print(line.rstrip()) #每行末尾两个空白

##创建一个包含文件各行内容的列表
filename= 'learning_python.txt'
with open(filename)as file_object:
    lines = file_object.readlines()
    #文件读取每一行并将内容存储在一个列表中 赋给lines with代码块外也可以使用这个变量
for line in lines:
    print(line.rstrip())

###使用文件内容
filename= 'learning_python.txt'
with open(filename)as file_object:
    lines = file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))
#读取文本文件时python将所有文本解读为字符串 如果读取数 并要用于数值可以用int() float()
#一百万位大型文件


##写入文件
#写入空白文件 只能将字符串写入文本文件 函数str()
#覆盖原有内容写入
filename= 'learning_python.txt'
with open(filename,'w')as file_object:
#两个实参 以写入模式打开文件 模式：只读模式‘r' 写入'w' 附加'a' 读写'r+' 省略模式实参默认只读‘r'
#如果写入文件不存在python 将自动创建它 写入模式打开文件时如果已存在python返回文件对象前清空文件内容
    file_object.write('i love u\n')
     #原文件内容被清空
    file_object.write('i love python\n')
     #写入多行用换行符

###给文件附加内容
#附加模式打开文件 不会清空 将添加文件行到文本末尾
filename= 'learning_python.txt'
with open(filename,'a')as file_object:
    file_object.write('i love create apps\n')
    #文件原内容未消失
#10-1 10-2
with open('learning_python.txt',)as f:
    for line in f:
        new_line=line.replace('love','hate')
        #replace方法替换原来内容
        print(new_line.rstrip())
#10-3
question=input('Please remanber enter your username: ')
with open('guest.txt','a')as fuck:
    fuck.write(question)
#10-4
while True:
    question=input('Please remember enter your username: ')
    if question=='quit':
        break
    print(f'welcome {question}')
    with open("guest_book.txt",'a',encoding='utf-8')as fuck:
        #utf-8 编码规则
       fuck.write(f'{question} have been visited\n')

#异常处理 try-except代码 即便程序出现异常也照样运行 不会报错traceback
#处理ZeroDivisionError
try:
    print(5/0) #如果try代码正常跳过except
except ZeroDivisionError:
    print('u can\'t divide by zero') #输出提示文本正常运行而不是traceback
#创建一个执行除法的计算器
#else代码块
print('Give me two numbers,and I will divide them.')
print('Enter"q" to quit.')
while True:
    first_number=int(input('Please enter your first number: '))
    if first_number=='q':
        break
    second_number=int(input('Please enter your second number: '))
    if second_number=='q':  #为0时程序崩溃
        break
    try:
        #try代码如果因为除0失败打印友好消息程序继续运行
        #只有可能引发异常的代码放入try中
       answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        #try代码引发指定异常怎么处理
        print('u can\'t divide by zero')
    else: #try成功运行时运行的代码
        print(answer)

#处理FileNotFoundError异常
filename='alice.txt' #不存在文件
try:
  with open(filename,encoding='uft-8')as f:
      contents=f.read()
except FileNotFoundError:
    print('file not found')
else:
    words=contents.split()
    num_words=len(words)
    print(f'There are {num_words} words in this file')
#扩展 提取大文本计算包含多少单词
# split（）方法 根据字符串以空格为分隔符创建一个单词列表

#使用多个文件
def count_words(filename):
    try:
        with open(filename, encoding='uft-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print('file not found')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'There are {num_words} words in this file')
filenames=['alice.txt','bob.txt','little.txt']
for filename in filenames:
  count_words(filename)
#try-except 优点：避免用户看到traceback以及程序继续运行
#pass语句 except。。。Error：pass 异常静默处理 不会有任何显示
#pass还充当了占位符你可以随时在这里修改代码

#控制显示报告哪些异常 何时向用户报告？何时静默？
#只要程序依赖外部输入就可能有异常 凭借经验在何处处理异常
#10-6
#10-7
#10-8
