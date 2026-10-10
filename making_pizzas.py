# 调用模块中的函数 import module_name.function_name（）
import 模块pizza
模块pizza.make_pizza(12,'cheese')

from 模块pizza import make_pizza #导入特定函数
make_pizza(16,'beef','apple')

#使用as给函数指定名称 from module_name import function_name as fn
from 模块pizza import make_pizza as mp #指定为新名
mp(12,'cheese') #调用新名
#使用as给模块指定名字 import module_name as mn
import 模块pizza as p
p.make_pizza(12,'cheese')

#导入模块中的所有函数*
from 模块pizza import*
make_pizza(12,'cheese') #直接调用函数无需.

#8-9
def send_message(messages,sent_messages):
    print(messages,sent_messages)
    while messages:
      current_message=messages.pop()
      sent_messages.append(current_message)
messages=['fku','fkh','fkm']
sent_messages=[]
send_message(messages[:],sent_messages)
print(messages,sent_messages)
#8-12
def sandwich_order(toppings):
    while True:
        client_topping=input(f'\nWhat would u want to add?(enter "stop" to quit):')
        if client_topping=='stop':break
        toppings.append(client_topping)
toppings=[]
sandwich_order(toppings)
print(f'\nThis is your {toppings}-sandwich.' )

#8-13
import 模块pizza as p
user_profile=build_profile('Harry','Duan',location='shanghai',field='engineer',age=23)
print(user_profile)

#8-14
def car(band,type,**car_kwargs):
    car_kwargs['band']=band
    car_kwargs['type']=type
    return car_kwargs
car_info=car('audi','rs7',color='black',tow_package=True)
print(car_info)

#8-15