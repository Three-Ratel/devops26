# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# name=input('name:')
# age=input('age:')
#
# msg=f'''
# #========
# name:{name}
# age:{age}


# msg = input('输入留言: ')
# if '波多野结衣' in msg or '苍老师' in msg:
#     print('sb')
# else:
#     print('合法留言')

# print(0 and 1 or 2 and 0 or 1 or 2 and 3)
#        0    or   0     or 1 or  3


# count=0
# while count<=100:
#     print(count)
#     count+=1
s='测试'
print(s.encode('utf-8'))

x=b'\xe6\xb5\x8b\xe8\xaf\x95'
print(x.decode('utf-8'))

print('#===================>')
List = [1,2,3,4,5,3,2,1,4,5,6,4,2,3,4,6,2,2]
List_set = set(List) #List_set是另外一个列表，里面的内容是List里面的无重复 项
for item in List_set:
    print("the %d has found %d" %(item,List.count(item)))
