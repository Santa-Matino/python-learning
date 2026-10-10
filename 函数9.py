# 向函数传递列表 实参是列表
def greet_users(names): #定义函数
    '''向列表中的每位用户发出简单问候'''
    for name in names: #函数体
        print(f'Hello,{name.title()}!')
names=['harry','charlotte','dickson'] #实参输入为一个列表
greet_users(names) #调用函数

#函数中修改列表  每个函数都应只负责一项具体工作
def printed_design(unprinted_designs,completed_designs): #打印每个设计
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing design:{current_design}.')
        completed_designs.append(current_design)
def completed_model(completed_designs): #显示打印好的模型
    print('The following designs completed successfully:')
    for completed_design in completed_designs:
        print(completed_design)
unprinted_designs=['sam','john','jack','mike']
completed_designs=([])
printed_design(unprinted_designs[:],completed_designs)
completed_model(completed_designs)
# 定义一个函数之前要知道你的预期目标
# 1你定义的函数要处理的数据是哪些 2你想要的处理完的数据是什么样子？怎么处理 3你要显示什么内容
#拿这个举例 第一个定义的函数处理两个列表所以2个形参，1列表是数据集2列表是空 希望处理完是1空2数，显示打印每一条字符
# 第二个函数只处理1函数处理的列表2，所以一个形参，处理完2不变，打印每一个字符

#修改列表但是要保留原文本 可以将副本传给函数 用function_name(list_name[:]) 代表原文件的副本
#切片表示法[:] 除非有充分理由 还是应该将原始列表传给函数 避免花时间内存创建副本

#传递任意数量的实参 *语句将不定数实参封装进一个元组中 *args通用形参收集任意数量的位置实参
def make_pizza(size,*toppings):
    print(f'\nmaking a {size}-inch pizza with following toppings:')
    for topping in toppings:
        print(f'-{topping}')
make_pizza(16,'chicken','pork','sheep')
#结合使用位置 任意数量实参
#python先匹配位置 默认为一个 余下的匹配任意数量实参 所以将任意数量放在最后

#任意数量的关键字实参 **语句让python创建一个空字典并将收到的所有键值对放进字典中 **kwargs
def build_profile(first,last,**profile_kwargs):
    profile_kwargs['first_name']=first
    profile_kwargs['last_name']=last
    return profile_kwargs
user_profile=build_profile('keven','harrigen',location='london',field='gangster')
print(user_profile)

#函数封装进模块中 import
