# pop方法 列表元素弹出备用 （）内可定元素位置
motocyco=['honda','yamaha','kawasaki']
popped_motocyco=motocyco.pop() #索引从0开始 -1最后
print(f'The last motocyco is {popped_motocyco.title()}')
print(motocyco)
print(popped_motocyco)

# remove方法 列表元素定值永久删除
moto=['h','e','f']
print(moto )
moto.remove('h')
print(moto)

# del语句 列表元素定位永久删除
moto=['h','e','f']
print(moto)
del moto[0]
print(moto)

# append方法 列表末尾添加新元素
motocyco=['w','e','f']
print(motocyco)
motocyco.append('s')
print(motocyco)

# insert方法 列表随机位置插入新元素
motocyco=['w','e','f']
print(motocyco)
motocyco.insert(1,'s')
print(motocyco)

# 练习题
guest_name=['edwd','xsi','frd','clt']
distinguished_guest=f'would you guys {guest_name} like to have a dinner with me '
print(distinguished_guest.title())
mercy_guest=f'{guest_name[0]} is not a dinner with me '
print(mercy_guest.title())
guest_name.remove('edwd')
guest_name.append('manny')
new_guest_name=f'{guest_name[3]} is a new dinner with me and this is the new list {guest_name}'
print(new_guest_name)
print(f'{guest_name} would you guys have a dinner with me?')
print('i can only invest two guests sorry ')
missing_guest1=guest_name.pop(1)
print(f'{missing_guest1} sorry you cant  have a dinner with me')
missing_guest2=guest_name.pop(2)
print(f'{missing_guest2} sorry you cant  have a dinner with me')
print(f'{guest_name}  you two can have a dinner with me ')
del guest_name[0]
del guest_name[0]
print(f'this is the new list {guest_name}')

#sort（）方法 列表元素字母正序永久排列 参数（reverse=true） 列表元素字母倒叙永久排列
motocyco=['honda','yamaha','kawasaki']
motocyco.sort(reverse=True)
print(motocyco)

#sorted（）函数 列表元素字母正序临时排列 参数（reverse=true） 反
motocyco=['honda','yamaha','kawasaki']
print(motocyco)
print(sorted(motocyco,reverse=True))
print(motocyco)

# reverse方法  反转列表元素位置排序 可恢复性永久 只需再次调用
motocyco=['honda','yamaha','kawasaki']
motocyco.reverse()
print(motocyco)
motocyco.reverse()
print(motocyco)

#len() 函数 快速获得列表长度
motocyco=['honda','yamaha','kawasaki']
print(len(motocyco))

#练习3-8
travel_place=['mediterranean','caribbean','australian','middleeast','northafrica']
print(travel_place)
#临时➕验证
print(sorted(travel_place))
print(travel_place)
# 临时反向
print(sorted(travel_place,reverse=True))
print(travel_place)
# 永久位置反向 再次反
travel_place.reverse()
print(travel_place)
travel_place.reverse()
print(travel_place)
# 永久➕反向 验证
travel_place.sort()
print(travel_place)
print(travel_place)
travel_place.sort(reverse=True)
print(travel_place)
print(travel_place)

# 练习3-9
print(len(travel_place))

#索引错误 [-1]很好用
