#模拟实物
#用代码表示实物
#9-6
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f'{self.restaurant_name} is in {self.cuisine_type} cuisine.')
    def open_restaurant(self):
        print(f'{self.restaurant_name} is opening!')
    def eat_number(self):
        print(f'{self.number_served} members have eaten so far!')
    def set_number_served(self,number):
        self.number_served=number
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['apple','banana','caffe','chocolate']
    def flavor_choices(self):
        for flavor in self.flavors:
          print(f'Our stand have :{flavor}-icecream.')
my_stand=IceCreamStand('BigDady','IceCream')
my_stand.describe_restaurant()
my_stand.flavor_choices()

#9-7 9-8
class User:
    def __init__(self,first_name,last_name,job,age):
        self.first_name=first_name
        self.last_name=last_name
        self.job=job
        self.age=age
        self.login_attempts=0
    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is a {self.job} in {self.age} years old.')
    def greet_user(self):
        print(f'Welcome Mr/Ms {self.first_name} {self.last_name}!your login attempts is: {self.login_attempts}.')
    def increment_login_attempts(self,attempts):
        self.login_attempts +=attempts #增加量
    def reset_login_attempts(self):
        self.login_attempts=0 #增减量
class Privileges:
    def __init__(self):
        self.privileges=['can','add post','can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print(f'Admin user can use this {privilege}')
class Admin(User):
    def __init__(self,first_name,last_name,job,age):
        super().__init__(first_name,last_name,job,age)
        self.admin_privileges=Privileges()
admin_user=Admin(first_name='aden',last_name='van hai',job='admin',age=22)
admin_user.admin_privileges.show_privileges()

#标准库
#9-13
import random
class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        resuit = random.randint(1,self.sides)
        print(f'You rolled a {resuit}')
my_die=Die(10)  #默认实参6面 10修改实参为10面
for _ in range(10): #掷骰子10次
   my_die.roll_die()

#9-14
import random
pool=[1,2,3,4,5,6,7,9,8,0,'a','b','c','d','e']
res=random.choices(pool,k=4) #k=4选4个 重复抽取
print(res)
res=random.sample(pool,3)  #一次性选 不重复抽取
print(res)
res=random.choice(pool) #一次抽一个
print(res)