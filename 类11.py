#类：一大类对象的通用行为  相似类可共享代码 可存储在模块中
#实例化（根据类创建的对象）：有这种通用行为并赋予个性
class Dog:
    def __init__(self,name,age):   #形参self必不可少放在其他形参前面 自动传入实参self
        ##类中的函数称为方法 都适用 调用有差别 -- init--每当创建新实例时python都运行它
        self.name=name #以self为前缀的变量可供类中所有方法使用 可通过实例访问的变量称为属性
        self.age=age
    def sit(self):
        print(f'{self.name} is now sitting.')
    def roll_over(self):
        print(f'{self.name} rolled over!')

my_dog=Dog('matt',6)
your_dog=Dog('john',6)
# python使用实参Matt，6 调用Dog--init-- 创建一个小狗实例并使用提供的值设置属性 返回一个实例赋给变量my_dog 首字母大写是类 小写的是实例
print(f'My dog name is {my_dog.name}.')  #访问属性 句点表示法
my_dog.sit() #调用方法（函数）
print(f'\nYour dog name is {your_dog.name}.')
your_dog.roll_over()

#9-1 9-4
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
restaurant1=Restaurant('woodie','chinese')
restaurant1.describe_restaurant()
restaurant1.number_served=1
restaurant1.eat_number()
restaurant1.set_number_served(23)
restaurant1.eat_number()

#9-3 9-5
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
user1=User('harry','de suza','gangster',35)
user1.increment_login_attempts(2) #0+2
user1.greet_user()
user1.increment_login_attempts(10) #2+10
user1.greet_user()
user1.reset_login_attempts() #12重置为0
user1.greet_user()

#使用类和实例
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0 #有些属性无需通过形参定义 添加一个属性 指定默认值
    def describe_car(self):
        long_name=f'{self.year} {self.make} {self.model}'
        return long_name.title()
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')
    def update_odometer(self,mileage): #通过方法修改属性
        if mileage >= self.odometer_reading: #扩展函数新指定属性值大于等于原来属性值则修改
          self.odometer_reading=mileage
        else:  #否则输出不能做
          print('You cannot do that!')
    def increment_odometer(self,miles): #将里程表读数增加指定量
        self.odometer_reading+=miles
my_car=Car('subaru','s4',2016)

my_car.odometer_reading=3 #方法1：直接访问属性修改值
my_car.read_odometer() #输出修改后的值

my_car.update_odometer(20) #方法2:使用函数实参赋值20修改属性
my_car.read_odometer() #输出修改的值

my_car.update_odometer(23_500)
my_car.read_odometer()
my_car.increment_odometer(100) #方法3：增加指定量修改属性值
my_car.read_odometer()

#继承 一个类继承另一个类自动获得另一个类的所有属性和方法还可以定义自己的属性和方法 父类子类
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size =75 #新属性
    def describe_battery(self): #新方法
        print(f'This car has a {self.battery_size}-kWh battery.')
my_tesla=ElectricCar('tesla','model y',2016)
print(my_tesla.describe_car())
my_tesla.describe_battery()
# 重写父类 继承精华去处糟粕 比如有子类完全用不到的父类方法 可以在子类重写一遍方法 代码将直接调用新的方法

#将实例用作属性  变量function—name=class()实例用作变量 现在换成 实例用作属性self.function=class()
#提取独立的类
class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')
    def get_range(self):
        if self.battery_size ==75:
            car_range = 6000
        elif self.battery_size ==100:
            car_range = 8000
        print(f'This car can go about {car_range} miles.')
    def upgrade_battery(self):
        if self.battery_size !=100:
            self.battery_size = 100
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery() #实例用作属性
my_tesla=ElectricCar('tesla','model y',2016)
my_tesla.battery.describe_battery() #查找属性battery 并对存储在属性battery中的实例Battery调用方法
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()