# 打印数字Number
'''
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]） 
float（浮点型） 
complex（复数） 
'''

# 赋值整型变量
print(1) # 1

# 长整型 尝试失败
#print(51924361L)

# 浮点型
print(1000.0) # 1000.0

# 复数
print(3.14j) # 3.14j
print(3.14) # 3.14
print(.876j) # 0.876j

# 打印数字计算
print(1+1) # 2

# 打印英文字符串
print("hello watermelon!") # hello watermelon!

# 打印中文字符串
# python3 默认支持UTF-8格式 不用设置编码格式
print("欢迎来到西瓜的世界") # 欢迎来到西瓜的世界

# python2 不支持UTF-8格式 需要设置编码格式 否则遇见中文会报错
print("欢迎来到西瓜的世界") 

'''
Non-ASCII character '\xe4' in file print.py on line 2, 
but no encoding declared; 
see http://www.python.org/peps/pep-0263.html for details
'''

# -*- coding: UTF-8 -*-
# 或者
# coding=utf-8
# 可以选择上面两种设置编码格式中一种就好了
print("欢迎来到西瓜的世界") # 欢迎来到西瓜的世界

# 打印布尔值
# 注意python中布尔值的首字母是大写的
# print(true) # name 'true' is not defined
print(True) #True
print(False) #False

#  List（列表） 可变
d_list = [66.25, 333, 333, 1, 1234.5]
print(d_list) # [66.25, 333, 333, 1, 1234.5]

# Tuple（元组） 不可变
d_tuple_1 = 12345, 54321, 'hello!'
d_tuple_2 = ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
print(d_tuple_1) # (12345, 54321, 'hello!')
print(d_tuple_2) # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Sets（集合）{}
d_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(d_set) # {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# Dictionaries（字典）
d_dic = {'jack': 4098, 'sape': 4139}
print(d_dic) # {'jack': 4098, 'sape': 4139}

# 打印数据类型检测
d_list_1 = [{'name':'melon','age':1},{'name':'water','age':2}];
print(isinstance(d_list_1,list)) # True
print(isinstance(d_list_1,dict)) # False
print(isinstance(d_list_1,set)) # False

d_dic_1 = dict({'name':'melon','age':[1,2]})
#{'name':'melon','age':[1,2]]},{'name':'water','age':[3,4]};
print(isinstance(d_dic_1,list)) # False
print(isinstance(d_dic_1,dict)) # True
print(isinstance(d_dic_1,set)) # True

d_set_1 = set([1, 2, 3])
#{'name':'melon','age':[1,2]]},{'name':'water','age':[3,4]};
print(isinstance(d_set_1,list)) # False
print(isinstance(d_set_1,dict)) # False
print(isinstance(d_set_1,set)) # True
