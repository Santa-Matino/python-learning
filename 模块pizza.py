def make_pizza(size,*toppings):
    print(f'\nmaking a {size}-inch pizza with following toppings:')
    for topping in toppings:
        print(f'-{topping}')

def build_profile(first,last,**profile_kwargs):
    profile_kwargs['first_name']=first
    profile_kwargs['last_name']=last
    return profile_kwargs