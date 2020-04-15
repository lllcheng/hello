a = (1,5,3,"哈哈","嘻嘻","哇哇",3,3,3,3,3,3,3,3,3,33,) 
# 从左往右是0开始数，从右往左是-1开始数
print(a[0:5])  #切片 左闭右开 没有右边的值 开头可以不写 结尾可以不写

print(a[3])  #取下标

print(a.index("嘻嘻")) # 查找某一值的下标
print(a.count(3))  #用来统计某个值的数量

b = (a,"嘿嘿嘿","lll")
print(b[0][3]) #用来打印a里面的哈哈  是并列



a = [1,5,9,5435,"你好","找工作","继续找"]
a.append(1)  
print(a)
a.insert(3,1)
print(a)
b = (1,3,5)
a.extend(b)
print(a)

a = {}
b = input("请输入您的名字：")
c = input("请输入您的年龄：")
d = input("请输入您的性别：")
a.update(name=b,age=c,sex=d)
print(a)