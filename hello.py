#第一个注释
print('Hello,Python!')#第二个注释

'''
第一个注释
第二个注释
第三注释
'''

if True:
    print("True")
else:
    print("False")

str='123456789'

print(str) #输出字符串
print(str[0:-1])#输出第一个到倒数第二个的所有字符
print(str[0])#输出字符串第一个字符
print(str[2:5])#输出从第三个开始到第六个的字符（不包含）
print(str[2:])#输出从第三个开始后的所有字符
print(str[1:5:2])#输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str*2)#输出字符串两次
print(str + '你好')#连接字符串

print('----------------')

print('hello\nrunoob')#使用反斜杠（\)+n转义特殊字符
print(r'hello\nrunoob')#在字符串前面添加一个r，表示原始字符串，不会发生转义

print('\n') #输出空行
print(r'\n')#输出\n

#等待用户输入
input("\n\n按下enter键后退出")

#同一行显示多条语句
import sys;x='runoob';sys.stdout.write(x+'\n')

#多个语句构成代码组
if expression:
    suite
elif expression:
    suite
else:
    suite

#print输出（实现不换行）
x='a'
y='b'
#换行输出
print( x )
print( y )

print('--------')
#不换行输出
print(x,end=' ')
print(y,end=' ')
print()

import sys
print('==============Python import mode==============')
print('命令行参数为：')
for i in sys.argv:
    print (i)
print('\n python 路径为',sys.path)

from sys import argv,path#导入特定的成员

print('=============python from import===========')
print('path:',path )# 因为已经导入path成员，所以此处引用时不需要加sys.path

#python基础数据类型
counter=100#整型变量
miles=1000.0#浮点型变量
name='runoob'#字符串

print(counter)
print(miles)
print(name)

a=b=c=1

a,b,c=1,2,'runoob'

#标准数据类型
'''
包括：
不可变数据（3个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3个）：List（列表）、Dictionary（字典）、Set（集合）；
'''

#Number（数字）：int、float、bool、complex（复数）
a,b,c,d=20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))

a=111
isinstance(a,int)

class A:
    pass
class B(A):
    pass
isinstance(A(),A)
type(A())==A
isinstance(B(),A)
type(B())==A

#注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
issubclass(bool,int)
True==1
False==0
True+1
False+1
1 is True
0 is False