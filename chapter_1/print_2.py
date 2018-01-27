#------------------------------------------------------------------------------------------------格式化输出测试 start
print('格式化输出测试 start ------------------------------------------------------------------------------------------------')
#------------------------------------------------------------------------------------------------格式化打印字符串 start
print('格式化打印字符串 start ------------------------------------------------------------------------------------------------')

print("利用 % 格式打印字符串 --------------------------------")

'''
%s --- 字符串
%d --- dec 十进制
'''

strHello = "the length of (%s) is %d" %('Hello Watermelon',len('Hello Watermelon'))
print(strHello) # the length of (Hello Watermelon) is 16

strHello = "Hello Watermelon"
print(strHello) # Hello Watermelon
print ("%.*s" % (4,strHello)) # Hell
print ("%.3s " % (strHello)) # Hel
# print ("%.*S" % (4,strHello)) # ValueError: unsupported format character 'S' (0x53)
# print ("%.3S " % (strHello)) # ValueError: unsupported format character 'S' (0x53)
print ("%s" % ("Hello Watermelon")) # Hello Watermelon
print('\n')
print('\n')

print("利用str.format()格式打印字符串 --------------------------------")

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"


# 大括号和其中的字符会被替换成传入 str.format() 的参数。大括号中的数值指明使用传入str.format() 方法的对象中的哪一个:
print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs

print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam


# 如果在 str.format() 调用时使用关键字参数，可以通过参数名来引用值:
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.


# 定位和关键字参数可以组合使用:
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
other='Georg'))
# The story of Bill, Manfred, and Georg.


# '!a' (应用 ascii())，'!s' （应用 str() ）和 '!r' （应用 repr() ）可以在格式化之前转换值
import math
print('The value of PI is approximately {}.'.format(math.pi))
# The value of PI is approximately 3.141592653589793.

print('The value of PI is approximately {!a}.'.format(math.pi))
# The value of PI is approximately 3.141592653589793.

print('The value of PI is approximately {!s}.'.format(math.pi))
# The value of PI is approximately 3.141592653589793.

print('The value of PI is approximately {!r}.'.format(math.pi))
# The value of PI is approximately 3.141592653589793.

#字段名后允许可选的 ':' 和格式指令。这允许对值的格式化加以更深入的控制。下例将 Pi 转为三位精度。
import math
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
# The value of PI is approximately 3.142.

print('\n')
print('\n')
#------------------------------------------------------------------------------------------------格式化打印字符串 end

#------------------------------------------------------------------------------------------------格式化打印数字Number start
print('格式化打印数字Number start ------------------------------------------------------------------------------------------------')
print("--------------------------------利用 % 格式打印数字")
# 利用 % 格式化打印数字知识前置
# 请注意这种不会有二进制数据的转换
'''
%s --- 字符串
%x --- hex 十六进制
%d --- dec 十进制
%o --- oct 八进制
%f --- flo 浮点型
'''

print("\t\t\t\t其他数字类型转成10进制的数字")

# 浮点转为10进制
print('\n')
# print('浮点的300.50转成10进制的{:d}'.format(300.50)) 
# ValueError: Unknown format code 'd' for object of type 'float'
print('浮点的300.50转成10进制的%d' % 300.50) # 浮点的300.50转成10进制的300

# 2进制转为10进制
print('\n')
print('2进制的0b1001转成10进制的%d' % 0b1001) # 2进制的0b1001转成10进制的9

# 8进制到10进制
print('\n')
print('8进制的0o10转成10进制的%d' % 0o10) # 8进制的0o10转成10进制的8

# 10进制到10进制
print('\n')
print('10进制的10转成10进制的%d' % 10) # 10进制的10转成10进制的10

# 16进制到10进制
print('\n')
print('16进制的0xff转成10进制的%d' % 0xff) # 16进制的0xff转成10进制的255

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成8进制的数字")

# 浮点转为8进制
print("浮点转为8进制--error")
# print('浮点的300.50转成8进制的%o' % 300.50) 
# TypeError: %o format: an integer is required, not float

# 2进制转为8进制
print('\n')
print('2进制的0b1001转成8进制的%o' % 0b1001) # 2进制的0b1001转成8进制的11

# 8进制到8进制
print('\n')
print('8进制的0o10转成8进制的%o' % 0o10) # 8进制的0o10转成8进制的10

# 10进制到8进制
print('\n')
print('10进制的10转成8进制的%o' % 10) # 10进制的10转成8进制的12

# 16进制到8进制
print('\n')
print('16进制的0xff转成8进制的%o' % 0xff) # 16进制的0xff转成8进制的377

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成16进制的数字")

# 浮点转为16进制
print("浮点转为16进制--error")
# print('浮点的300.50转成16进制的%x' % 300.50) 
# TypeError: %x format: an integer is required, not float

# 2进制转为16进制
print('\n')
print('2进制的0b1001转成16进制的%x' % 0b1001) # 2进制的0b1001转成16进制的9

# 8进制到16进制
print('\n')
print('8进制的0o10转成16进制的%x' % 0o10) # 8进制的0o10转成16进制的8

# 10进制到16进制
print('\n')
print('10进制的10转成16进制的%x' % 10) # 10进制的10转成16进制的a

# 16进制到16进制
print('\n')
print('16进制的0xff转成16进制的%x' % 0xff) # 16进制的0xff转成16进制的ff

print("\t\t\t\t其他数字类型转成浮点型的数字")

# 浮点转为浮点型
print('\n')
print('浮点的300.50转成浮点型的%.3f' % 300.50) # 浮点的300.50转成浮点型的300.500

# 2进制转为浮点型
print('\n')
print('2进制的0b1001转成浮点型的%.3f' % 0b1001) # 2进制的0b1001转成浮点型的9.000

# 8进制到浮点型
print('\n')
print('8进制的0o10转成浮点型的%.3f' % 0o10) # 8进制的0o10转成浮点型的8.000

# 10进制到浮点型
print('\n')
print('10进制的10转成浮点型的%.3f' % 10) # 10进制的10转成浮点型的10.000

# 16进制到浮点型
print('\n')
print('16进制的0xff转成浮点型的%.3f' % 0xff) # 16进制的0xff转成浮点型的255.000

print('\n')
print('\n')


print("--------------------------------利用内置函数格式打印数字")

print("\t\t\t\t其他数字类型转成10进制的数字")
# 使用int函数的时候，二进制，八进制，十六进制的前缀都可以忽略，当然加上也不算错

# 浮点转为10进制
print("浮点转为10进制")

print(int(300.50)) # 300

# 2进制转为10进制
print("2进制转为10进制")
print(int("0b1001",2)) # 9
print(int("1001",2)) # 9

# 8进制到10进制
print("8进制到10进制")
print(int("0o10", 8)) # 8
print(int("10", 8)) # 8

# 10进制到10进制
print("10进制到10进制")
print(int(10)) # 10

# 16进制到10进制
print("16进制到10进制")
print(int("ff", 16)) # 255
print(int("0xff", 16)) # 255

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成2进制的数字")

# 浮点转为2进制
print("浮点转为2进制")

# print(bin(300.50)) # TypeError: 'float' object cannot be interpreted as an integer

# 2进制转为2进制
print(bin(0b1010)) # 0b1010

# 10进制转为2进制
print("10进制转为2进制")

print(bin(10)) # 0b1010

# 8进制到2进制
print("8进制到2进制")

print(bin(0o10)) # 0b1000

# 16进制到2进制
print("16进制到2进制")

print(bin(0xff)) # 0b11111111

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成8进制的数字")

# 浮点转为8进制
print("浮点转为8进制--error")
# print(oct(300.50)) # TypeError: 'float' object cannot be interpreted as an integer

# 2进制转为8进制
print("2进制转为8进制")
print(oct(0b1001)) # 0o11

# 8进制到8进制
print("8进制到8进制")
print(oct(0o10)) # 0o10

# 10进制到8进制
print("10进制到8进制")
print(oct(10)) # 0o12

# 16进制到8进制
print("16进制到8进制")
print(oct(0xff)) # 0o377

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成16进制的数字")

# 浮点转为16进制
print("浮点转为16进制--error")
# print(hex(300.50)) # TypeError: 'float' object cannot be interpreted as an integer

# 2进制转为16进制
print("2进制转为16进制")
print(hex(0b1001)) # 0x9

# 8进制到16进制
print("8进制到16进制")
print(hex(0o10)) # 0x8

# 10进制到16进制
print("10进制到16进制")
print(hex(10)) # 0xa

# 16进制到16进制
print("16进制到16进制")
print(hex(0xff)) # 0xff

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成浮点型的数字")

# 浮点转为浮点型
print("浮点转为浮点型")
print(float(300.50)) # 300.5

# 2进制转为浮点型
print("2进制转为浮点型")
print(float(0b1001)) # 9.0

# 8进制到浮点型
print("8进制到浮点型")
print(float(0o10)) # 8.0

# 10进制到浮点型
print("10进制到浮点型")
print(float(10)) # 10.0

# 16进制到浮点型
print("16进制到浮点型")
print(float(0xff)) # 255.0

print('\n')
print('\n')

print("--------------------------------利用str.format()格式打印数字")

print("\t\t\t\t其他数字类型转成10进制的数字")

# 浮点转为10进制
print("浮点转为10进制")
# print('浮点的300.50转成10进制的{:d}'.format(300.50)) 
# ValueError: Unknown format code 'd' for object of type 'float'
print('浮点的300.50转成10进制的{:.0f}'.format(300.50)) # 浮点的300.50转成10进制的300

# 2进制转为10进制
print('\n')
print('2进制的0b1001转成10进制的{:d}'.format(0b1001)) # 2进制的0b1001转成10进制的9

# 8进制到10进制
print('\n')
print('8进制的0o10转成10进制的{:d}'.format(0o10)) # 8进制的0o10转成10进制的8

# 10进制到10进制
print('\n')
print('10进制的10转成10进制的{:d}'.format(10)) # 10进制的10转成10进制的10

# 16进制到10进制
print('\n')
print('16进制的0xff转成10进制的{:d}'.format(0xff)) # 16进制的0xff转成10进制的255

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成2进制的数字")

# 浮点转为2进制
print("浮点转为2进制")
# print('浮点的300.50转成2进制的{:b}'.format(300.50))
# ValueError: Unknown format code 'b' for object of type 'float'

# 2进制转为2进制
print('\n')
print('2进制的0b1001转成2进制的{:b}'.format(0b1001)) # 2进制的0b1001转成2进制的1001

# 8进制到2进制
print('\n')
print('8进制的0o10转成2进制的{:b}'.format(0o10)) # 8进制的0o10转成2进制的1000

# 10进制到2进制
print('\n')
print('10进制的10转成2进制的{:b}'.format(10)) # 10进制的10转成2进制的1010

# 16进制到2进制
print('\n')
print('16进制的0xff转成2进制的{:b}'.format(0xff)) # 16进制的0xff转成2进制的11111111

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成8进制的数字")

# 浮点转为8进制
print("浮点转为8进制--error")
# print('浮点的300.50转成8进制的{:o}'.format(300.50)) 
# ValueError: Unknown format code 'o' for object of type 'float'

# 2进制转为8进制
print('\n')
print('2进制的0b1001转成8进制的{:o}'.format(0b1001)) # 2进制的0b1001转成8进制的11

# 8进制到8进制
print('\n')
print('8进制的0o10转成8进制的{:o}'.format(0o10)) # 8进制的0o10转成8进制的10

# 10进制到8进制
print('\n')
print('10进制的10转成8进制的{:o}'.format(10)) # 10进制的10转成8进制的12

# 16进制到8进制
print('\n')
print('16进制的0xff转成8进制的{:o}'.format(0xff)) # 16进制的0xff转成8进制的377

print('\n')
print('\n')

print("\t\t\t\t其他数字类型转成16进制的数字")

# 浮点转为16进制
print("浮点转为16进制--error")
# print('浮点的300.50转成16进制的{:x}'.format(300.50)) 
# ValueError: Unknown format code 'x' for object of type 'float'

# 2进制转为16进制
print('\n')
print('2进制的0b1001转成16进制的{:x}'.format(0b1001)) # 2进制的0b1001转成16进制的9

# 8进制到16进制
print('\n')
print('8进制的0o10转成16进制的{:x}'.format(0o10)) # 8进制的0o10转成16进制的8

# 10进制到16进制
print('\n')
print('10进制的10转成16进制的{:x}'.format(10)) # 10进制的10转成16进制的a

# 16进制到16进制
print('\n')
print('16进制的0xff转成16进制的{:x}'.format(0xff)) # 16进制的0xff转成16进制的ff

print("\t\t\t\t其他数字类型转成浮点型的数字")

# 浮点转为浮点型
print('\n')
print('浮点的300.50转成浮点型的{:.3f}'.format(300.50)) # 浮点的300.50转成浮点型的300.500

# 2进制转为浮点型
print('\n')
print('2进制的0b1001转成浮点型的{:.3f}'.format(0b1001)) # 2进制的0b1001转成浮点型的9.000

# 8进制到浮点型
print('\n')
print('8进制的0o10转成浮点型的{:.3f}'.format(0o10)) # 8进制的0o10转成浮点型的8.000

# 10进制到浮点型
print('\n')
print('10进制的10转成浮点型的{:.3f}'.format(10)) # 10进制的10转成浮点型的10.000

# 16进制到浮点型
print('\n')
print('16进制的0xff转成浮点型的{:.3f}'.format(0xff)) # 16进制的0xff转成浮点型的255.000

print('\n')
print('\n')
#------------------------------------------------------------------------------------------------格式化打印数字Number end

#------------------------------------------------------------------------------------------------格式化打印错误集合 start
print('格式化打印错误集合 start ------------------------------------------------------------------------------------------------')

print("逗号错误 --------------------------------")
# 请注意`左参数`和`右参数`之间不存在逗号，如果写了逗号，会报错。

# print("%s,%s", % ("hello","watermelon"))
# SyntaxError: invalid syntax

print("进制转换错误 --------------------------------")

print("\t\t\t\t数据类型必须是小写字母")
# `八进制类型`，`十进制类型`和`字符串类型`的缩写必须是`小写字母`，换成`大写字母`会报错。

# print ("%O " % ("Hello Watermelon"))
'''
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print ("%O " % ("Hello Watermelon"))
ValueError: unsupported format character 'O' (0x4f) at index 1
'''

# print ("%D " % ("Hello Watermelon"))
'''
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print ("%D " % ("Hello Watermelon"))
ValueError: unsupported format character 'D' (0x44) at index 1
'''

# print ("%S " % ("Hello Watermelon"))
'''
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print ("%S " % ("Hello Watermelon"))
ValueError: unsupported format character 'S' (0x53) at index 1
'''

print("\t\t\t\t数据类型必须是数字类型")
# 做`类型转换`的时候，`浮点类型`和`十进制类型`需要传入的参数必要是`数字类型`的。
# print ("%d " % ("Hello Watermelon"))
'''
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print ("%d " % ("Hello Watermelon"))
TypeError: %d format: a number is required, not str
'''

# print ("%F " % ("Hello Watermelon"))
'''
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print ("%F " % ("Hello Watermelon"))
TypeError: must be real number, not str
'''


print("\t\t\t\t数据类型必须是整型")
# 做`类型转换`的时候，`十六进制类型`和`八进制类型`需要传入的参数必要是`整型`。
# print ("%X " % ("Hello Watermelon"))
'''
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print ("%X " % ("Hello Watermelon"))
TypeError: %X format: an integer is required, not str
'''

# print ("%o " % ("Hello Watermelon"))
'''
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print ("%o " % ("Hello Watermelon"))
TypeError: %o format: an integer is required, not str
'''


print("参数个数错误 --------------------------------")
# `左参数`的`个数`和`右参数`的`个数`一定要相等。
# print ("%s,%s" % ("Hello","Watermelon","!"))
'''
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print ("%s,%s" % ("Hello","Watermelon","!"))
TypeError: not all arguments converted during string formatting
'''

#------------------------------------------------------------------------------------------------格式化打印错误集合 end














