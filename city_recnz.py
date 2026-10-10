def world_definition(city,country,population=''):
    if population:
      full_world=f'{city},{country}-population:{population}'
    else:
      full_world=f'{city},{country}'
    return full_world

class Eployee:
    def __init__(self,first_name,last_name,year_salary):
        self.first_name=first_name
        self.last_name=last_name
        self.year_salary=year_salary
    def give_raise(self,add=5000):
        self.year_salary += add
