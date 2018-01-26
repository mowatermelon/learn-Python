

# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

#------------------------------------------------------------------------------------------------第一个参数value测试 start
print('第一个参数value测试 start ------------------------------------------------------------------------------------------------')
# ---------------------------------------------------------------一个参数都不传
print("一个参数都不传 ---------------------------------------------------------------")
print() # ''  不会报错，输出一个空值
print('\n')
print('\n')
# ---------------------------------------------------------------只传入一个value值
print("只传入一个value值 ---------------------------------------------------------------")
# --------------------------------打印数字Number
print("打印数字Number --------------------------------")

'''
整型(Int)
 - 通常被称为是整型或整数，是正或负整数，不带小数点，可以是二进制，八进制，十进制，十六进制。

长整型(long integers)
 - 无限大小的整数，整数最后是一个大写或小写的L。

浮点型(floating point real values)
 - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）

复数( (complex numbers))
 - 复数的虚部以字母J 或 j结尾 。如：2+3i

'''
# 赋值整型变量
print("\t\t\t\t赋值整型变量")

'''
1.二进制：除表示正负的符号外，以0b或者0B开头，由0和1组成。如，0b100，0b10，0b110。
2.十进制：除表示正负的符号外，以1~9开头，由0~9组成。如，128，+234，-278。
3,八进制：以0o或者0O开头，由0~7组成的数。如，0o126,0o50000.
4,十六进制：以0x或0X开头，由0~9，A~F或a~f 组成。如，0x12A,0x5a000。
'''
#10进制
print("10进制的数字")

print(10) # 10

#2进制转为10进制
print("2进制到10进制")
print(0B1001) # 9
print(0b1001) # 9

#16进制到10进制
print("16进制到10进制")
print(0Xab) # 171

print(0xab) # 171

#8进制转为10进制
print("8进制转为10进制")
print(0O12) # 10
print(0o12) # 10

# 长整型
print("\t\t\t\t长整型变量")
# 一个也没尝试成功，不知道python3中打印
# print(51924361L)
# print(-0x19323L) 
# print(0122L)
# print(0xDEFABCECBDAECBFBAEl) 
# print(535633629843L) 
# print(-052318172735L) 
# print(-4721885298529L) 

# 浮点型
print("\t\t\t\t浮点型变量")

print(1000.0) # 1000.0

# 复数型变量
print("\t\t\t\t复数型变量")

print(3.14j) # 3.14j
print(3.14) # 3.14
print(.876j) # 0.876j

print('\n')
print('\n')
# --------------------------------打印字符串String
print("打印字符串String--------------------------------")

# 打印中文字符串
print("\t\t\t\t打印中文字符串")

print("欢迎来到西瓜的世界") # 欢迎来到西瓜的世界

# 打印英文字符串
print("\t\t\t\t打印英文字符串")

print("hello watermelon!") # hello watermelon!

print('\n')
print('\n')

# --------------------------------打印布尔值Boolean
print("打印布尔值Boolean --------------------------------")
# 注意python中布尔值的首字母是大写的
# print(true) # name 'true' is not defined
print(True) #True
print(False) #False

print('\n')
print('\n')

# --------------------------------打印列表List
print("打印列表List --------------------------------")

#  List（列表） 可变
d_list = [66.25, 333, 333, 1, 1234.5]
d_list[4] = 6666
print(d_list) # [66.25, 333, 333, 1, 6666]

print('\n')
print('\n')

# --------------------------------打印元组Tuple
print("打印元组Tuple --------------------------------")

# Tuple（元组） 不可变
d_tuple_1 = 12345, 54321, 'hello!'
d_tuple_2 = ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
print(d_tuple_1) # (12345, 54321, 'hello!')
print(d_tuple_2) # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

print('\n')
print('\n')

# --------------------------------打印集合Sets
print("打印集合Sets --------------------------------")
# Sets（集合）{}
d_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(d_set) # {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print('\n')
print('\n')

# --------------------------------打印字典Dictionaries
print("打印字典Dictionaries --------------------------------")
# Dictionaries（字典）{ key:value }
d_dic = {'jack': 4098, 'sape': 4139}
print(d_dic) # {'jack': 4098, 'sape': 4139}

print('\n')
print('\n')

# --------------------------------打印数据类型检测
print("打印数据类型检测 --------------------------------")

d_list_1 = list([{'name':'melon','age':1},{'name':'water','age':2}]);
print(isinstance(d_list_1,list)) # True
print(isinstance(d_list_1,dict)) # False
print(isinstance(d_list_1,set)) # False

print('\n')

d_dic_1 = dict({'name':'melon','age':[1,2]})
print(isinstance(d_dic_1,list)) # False
print(isinstance(d_dic_1,dict)) # True
print(isinstance(d_dic_1,set)) # True

print('\n')

d_set_1 = set([1, 2, 3])
print(isinstance(d_set_1,list)) # False
print(isinstance(d_set_1,dict)) # False
print(isinstance(d_set_1,set)) # True

print('\n')
print('\n')

# ---------------------------------------------------------------传入多个value值
print("传入多个value值 ---------------------------------------------------------------")

print("hello","watermelon","!") # hello watermelon !

print("hello",1,"watermelon",[1.2],"!") # hello 1 watermelon [1.2] !

# 打印数字计算
print('100 + 200 =', 100 + 200) # 100 + 200 = 300

print('\n')
print('\n')

#------------------------------------------------------------------------------------------------第一个参数value测试 end

#------------------------------------------------------------------------------------------------第二个参数sep测试 start
print('第二个参数sep测试 start ------------------------------------------------------------------------------------------------')
# 设置多个value值之间间隔内容
print("hello","watermelon","!",sep='/') # hello/watermelon/!

print('\n')
print('\n')

#------------------------------------------------------------------------------------------------第二个参数sep测试 end

#------------------------------------------------------------------------------------------------第三个参数end测试 start
print('第三个参数end测试 start ------------------------------------------------------------------------------------------------')
# 设置多个value值的结尾内容
print("hello","watermelon","!",end='/') # hello watermelon !/

print('\n')
print('\n')

#------------------------------------------------------------------------------------------------第三个参数end测试 end

#------------------------------------------------------------------------------------------------第四个参数file测试 start
print('第四个参数file测试 start ------------------------------------------------------------------------------------------------')
print("在项目所在根文件夹下的chapter_1/a.txt下，查看输出内容")
d_list_1 = list([{'name':'melon','age':1},{'name':'water','age':2}]);
# 这样就会在项目所在根文件夹下的chapter_1下，新建 abc.txt
# 这个文本内容就是需要打印出来的内容，可以重复写入  

'''
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
'''

with open(r'chapter_1/a.txt', 'w') as demo:  
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)  
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)  
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)  

# open('file_name', mode, buffering)

# open中file_name的basedir默认是当前项目的根文件夹

# 举栗子啦

'''
r'chapter_1\abc.txt' 和 'chapter_1\\abc.txt'的意思是一致
加上 r ，就是双引号之内的反斜杠不会被认为是转译字符 

r'../abc.txt' 
是当前项目的上一级文件夹中的abc.txt

r'../chapter_1/abc.txt' 
是当前项目的上一级文件夹中的chapter_1/abc.txt，
由于当前项目的上一级文件夹中没有chapter_1，
所以会报错 [Errno 2] No such file or directory: '../chapter_1/abc.txt'
'''

# open中mode默认提供的类型很多

# 举栗子啦

'''
r 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。

rb 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。

r+ 打开一个文件用于读写。文件指针将会放在文件的开头。

rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。

w 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

wb 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

ab 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''

print('\n')
print('\n')

#------------------------------------------------------------------------------------------------第四个参数file测试 end

#------------------------------------------------------------------------------------------------第五个参数flush测试 start
print('第五个参数flush测试 start ------------------------------------------------------------------------------------------------')
print("在项目所在根文件夹下的chapter_1/b.txt下，查看输出内容")
d_list_1 = list([{'name':'melon','age':1},{'name':'water','age':2}]);
# 这样就会在项目所在根文件夹下的chapter_1下，新建 abc.txt
# 这个文本内容就是需要打印出来的内容，可以重复写入  

'''
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
1,2,3,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
'''

# 先获取完输入内容，再一起输入到文件流中
with open(r'chapter_1\b.txt', 'w') as demo:
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)   
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)  
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)   
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)  
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)   
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)  
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)   
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)  
    print(1, 2, 3, d_list_1, sep = ',', end = '\n', file = demo)

'''
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
4,5,6,[{'name': 'melon', 'age': 1}, {'name': 'water', 'age': 2}]
'''

with open(r'chapter_1\b.txt', 'w') as demo:
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)   
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)  
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)   
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)  
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)   
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)  
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)   
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)  
    print(4, 5, 6, d_list_1, sep = ',', end = '\n', file = demo, flush=True)

print('\n')
print('\n')

#------------------------------------------------------------------------------------------------第五个参数flush测试 end

#------------------------------------------------------------------------------------------------与python2的不同 start
print('与python2的不同 start ------------------------------------------------------------------------------------------------')

'''
在Python2和Python3中都提供print()方法来打印信息,但两个版本间的print稍微有差异

主要体现在以下几个方面：

1.python3中print是一个内置函数，有多个参数，而python2中print是一个语法结构；

2.Python2打印时可以不加括号：print 'hello world'， Python3则需要加括号   print("hello world")

3.Python2中，input要求输入的字符串必须要加引号，为了避免读取非字符串类型发生的一些行为，
不得不使用raw_input()代替input()
'''

# ---------------------------------------------------------------设置输出内容不换行
print("设置输出内容不换行 ---------------------------------------------------------------")

# --------------------------------python2中设置输出内容不换行

'''
Python2.x下的print语句在输出字符串之后会默认换行，
如果不希望换行，只要在语句最后加一个“，”即可。
'''

# print 'hello watermelon,'

# --------------------------------python3中设置输出内容不换行

print ('hello watermelon',end='')

print('\n')
print('\n')

# ---------------------------------------------------------------打印中文字符串
print("打印中文字符串 ---------------------------------------------------------------")

# --------------------------------python2 不支持UTF-8格式 需要设置编码格式 否则遇见中文会报错
# print "欢迎来到西瓜的世界"  

'''
Non-ASCII character '\xe4' in file print.py on line 370, 
but no encoding declared; 
see http://www.python.org/peps/pep-0263.html for details
'''

# -*- coding: UTF-8 -*-
# 或者
# coding=utf-8
# 可以选择上面两种设置编码格式中一种就好了
# print "欢迎来到西瓜的世界" # 欢迎来到西瓜的世界

# --------------------------------python3 默认支持UTF-8格式 不用设置编码格式
print("欢迎来到西瓜的世界") # 欢迎来到西瓜的世界

print('\n')
print('\n')


# ---------------------------------------------------------------打印中文字符串
print("打印中文字符串 ---------------------------------------------------------------")
# --------------------------------python2 八进制数字前面只用加一个数字0，就可以了
# print(01,020,0377)      # 1, 16, 255  

# --------------------------------python3 八进制数字前面需要加一个数字0和一个小写字母o，
首先，python2.6的用户应该记住在编写八进制之前，直接用一个0开头，python中最初的八进制格式如下：
#python2.6与python3.0中都可用
print(0o1,0o20,0o377)   # 1, 16, 255  

print('\n')
print('\n')
#------------------------------------------------------------------------------------------------与python2的不同 end
