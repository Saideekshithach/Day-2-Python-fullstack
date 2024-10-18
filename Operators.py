Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0

print(a/b)
0.5
print(a%b)
2
print(a**b)
16
#assignment operators
a=2
b=4
a+=b
a
6
a-=3
a
3
a*=5
a
15
a//=2
a
7
a/=2
a
3.5
a%=2
a
1.5
a**=4
a
5.0625
a=4
b=8
b+=a
b
12
b-=2
b
10
#comparison operators
a=5
b=7
a<b
True
b>a
True
a<=b
True
b>=a
True
a!=b
True
a==b
False
#logical operators
a=4
b=8
a==b and a!=b
False
a<b and b>a
True
a<=b and b>=a
True
a!=b or a==b
True
a>=b or a<=b
True
not True
False
#identify operators
a=4.5
if type(a) is float:
    print("true")
else:
    print("false")

    
true
if type(a) is not float:
    print("yes")
else:
    print("no")

    
no
#Membership operators
a=2,4,6,8,10
>>> if 10 in a:
...     print(10)
... 
...     
10
>>> if 20 in a:
...     print(20)
... 
...     
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> if 6 not in a:
...     print(6)
... 
...     
>>> a="word","bird"
>>> if "word" in a:
...     print("word")
... 
...     
word
>>> if "word" not in a:
...     print("word")
... 
...     
>>> 
>>> if "word" in a:
...     print(word)
... 
...     
Traceback (most recent call last):
  File "<pyshell#87>", line 2, in <module>
    print(word)
NameError: name 'word' is not defined. Did you mean: 'ord'?
