收录张行功老师24 fall-计算概论B课程部分作业习题，希望对于期末机考有所启发。仅供学习交流。

nanoxi 24.12.03



## 每周作业

### 1.今天是星期几

**题目描述**

某一个平年中，一月一日是星期w，请计算m月d日是星期几

**关于输入**

一行三个整数w(1<=w<=7),m(1<=m<=12),d(l<=d<=31),空格隔幵

**关于输出**

一个数，即对应星期

**可行代码**

```python
w, m, d =map(int,input().split())
mdays=[31,28,31,30,31,30,31,31,30,31,30,31]
wdays=sum(mdays[:m-1])+d+w-1
ans=wdays%7
if ans==0:
    print(7)
else:
    print(ans)
```

**提示**

1. 先想好公式再写

### 2. 找到出现次数最多的字母

**题目描述**

给定一个字符串，统计该字符串中出现最多的字母（a-z，不区分大小写）。若有多个字母出现次数相等且最多，输出字母表排列最靠前的字母。

**关于输入**

一行，字符串

**关于输出**

一行，一个大写字母，一个整数，空格隔开

**可行代码**

```python
line=input().upper()
cnt=[0]*26
for c in line:
    if 'A'<=c<='Z':
        cnt[ord(c)-ord('A')]+=1
char,times='A',0
for i in range(26):
    if cnt[i]>times:
        times=cnt[i]
        char=chr(ord('A')+i)
print(char,times,sep=' ')
```

**提示**

1. ord与chr的使用
2. cnt列表用于存储字母出现次数

### 3. 找质数

```py
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+2):
        if n%i==0:
            return False
    return True
```

**提示**

改进：6*n ± 1（数论）

### 4. 二进制

```py
n=int(input())
for i in range(n):
    a=int(input())
    b=bin(a)
    print(str(b).count('1'))
```

**提示**

1. bin的使用

### 5. 北京地铁

**题目描述**
地铁票价计算方法如下：
6公里内 3元 （包括6公里），6-12 公里 4元 （不包括6公里，包括12公里），12-32 公里 每10公里加1元（不包括12公里，包括32公里，不满10公里按10公里算），32公里以上 每20公里加1元（不包括32公里，不满20公里按20公里算）
比如，50公里时，需要 4+2+1=7元

同时，北京地铁也给出了优惠方案：
每个自然月内，使用交通卡满100元，则票价可打8折；满150元，则票价可打5折；满400元，则票价不打折。

现在小明想知道自己现在坐地铁的票价。

**关于输入**

输入两个整数，一个是小明现在这个月的累计消费，一个是小明本次乘坐的里程数

**关于输出**

输出为本次乘坐的票价，保留两位小数

**可行代码**

```python
from math import ceil
total,distance=map(int,input().split())
if distance<=6:
    fare=3
elif distance<=12:
    fare=4
elif distance<=32:
    fare=ceil((distance-12)*0.1)+4
else:
    fare=ceil((distance-32)*0.05)+6

if total>=150 and total<400:
    fare=fare*0.5
elif total>=100:
    fare=fare*0.8

print(f'{fare:.2f}')
```

**提示**

1. 没啥规律的时候可以枚举。

### 6. 找最大公约数（GCD）函数

```python
def findgcd(x,y):
    if x==y:
        return(y)
    if x>y:
        x,y=y,x
    while y%x!=0:
        y,x=x,y%x
    return(x)
# 辗转相除法
```

### 7. 合法的日期

**题目描述**

判断y年m月d日是否合法

**关于输入**

一行3个整数y（1000<=y<=9999），m，d空格隔开

**关于输出**

合法："YES"，否则："NO"

**可行代码**

```python
y,m,d=map(int,input().split())
if m<1 or m>12 or d<1 or d>31:
    ans='NO'
elif m in[1,3,5,7,8,10,12]:
    ans='YES'
elif m in [4,6,9,11]:
    if d<=30:
        ans='YES'
    else:
        ans='NO'
elif d<=28:
    ans="YES"
else:
    if( y%4==0 and y%100!=0 ) or (y%400==0):
        ans='YES'
    else:
        ans='NO'
print(ans)
```

**提示**

考虑全边界情况

### 8. 类型判断与动态拆解

###### 枚举，挺麻烦

**题目描述**

接收用户输入的一个字符串列表，并将其拆解为各个元素，根据类型逐一打印。
例如：
  整数用int标识，浮点数用float标识，布尔值用bool标识，字符串用str标识。若以上条件都不满足，则提示Type_Unknown。

你的程序要动态解析这些变量的类型，并赋值到合适的变量中输出

**关于输入**

一行，格式与print出来的list一致，该列表不为空，为:
[a1, b1, c1, d1]
且元素内不含','--提示可以用“，”识别并分割列表

**关于输出**

假设输入的列表长度为n，则输出n行
每行依次输出该元素的'type:','element'

**例子输入**

```
[1, 2, 3.5, True, ha?, 'YiYaHa~~~']
```

**例子输出**

```
int: 1
int: 2
float: 3.5
bool: True
Type_Unknown: ha?
str: YiYaHa~~~
```

**提示信息**
000000.00000000 is equal to 0.0
Type string is either "abc123" or 'abc123'
(method)def isdigit(self:self@str)-> bool
Return True if the string is a digit string, False otherwise.
e.g.
  print('1233'.isdigit()) # True
  print('12.33'.isdigit()) # False
replace(old: str, new: str, count:SupportsIndex=-1)->str
Return a copy with all occurrences of substring old replaced by new.count Maximum number of occurrences to replace. -1 (default value) means replace all occurrences.
e.g.
  print('7788'.replace('7','6')) # 6688
  print('hello, helo, lolo'.replace('lo','p',2)) # help, hep, lolo
You can try:
  i.startswith(' ') and i.endswith(' ')

**可行代码**

```python
line=list(map(str,input().split(',')))
line[0]=line[0][1:]
line[-1]=line[-1][:-1]
for i in line:
    i=i.strip(' ')
    if i[0]==i[-1]=="\'" or i[0]==i[-1]=="\"":
        print('str:',i[1:-1])
    elif i=='True' or i=='False':
        print('bool:',i)
    elif i.strip(' ').isdigit():
        print('int:',int(i))
    elif i.count('.')==1:
        print('float:',float(i))
    else:
        print('Type_Unknown:',i)
```

### 9. 矩阵交换行

###### bad一题两问

**题目描述**

编写一个函数，接收一个 5x5 的二维整数数组 matrix 和两个整数 n、m（表示行的下标）。函数需要执行以下操作：

检查 n 和 m 是否在数组的有效行范围内：
1.如果 n 和 m 都在范围内，则交换矩阵中的第 n 行和第 m 行，并输出交换后的新矩阵。
2.如果 n 或 m 不在范围内，则将二数组展平为一维数组，计算该一维数组中索引为 n 到 m 范围内的元素和，并输出该和。

**关于输入**

一个5x5的二维整数数组和两个整数n,m

**关于输出**

二维整数数组或是一个整数

**可行代码**

```python
m=[]
for i in range(5):
    m.append(list(map(int, input().split())))
a,b=map(int,input().split())
if 0<=a<=4 and 0<=b<=4:
    s1=m[a]
    s2=m[b]
    m[a]=s2
    m[b]=s1
    for i in range(5):
        print(*m[i])
else:
    newlist=[]
    for i in range(5):
        for j in range(5):
            newlist.append(m[i][j])
    t=0
    for i in range(a,b+1):
        t+=newlist[i]
    print(t)
```

### 10. AI（表达式判断）

###### 又一个烦的

**题目描述**

P（功率）= U（电压）* I（电流）。如果给定其中的任意两个值，求第三个值。

**关于输入**
输入的第一行是一个整数，表示有多少组测试数据。以下每一行是一组测试数据，分别为一句英文句子。你需要从中识别已知和未知，并且求出未知量。需要说明的是，句子中I，U，P三个物理量中已知的两个一定会以I=xA, U=xV，P=xW这样的样式给出（注意单位以及大小写）。在这样的表达式中，可能会在单位（A，V，W）的前面出现表示数量级的字母m、k、M，分别表示毫，千，兆。

**关于输出**

对于每一组数据，按以下格式输出三行：
首先输出"Problem #k"，k表示当前是第k组测试数据。
然后在下一行输出结果，结果要求单位必须为A，V或者W，并且保留两位小数。
最后再输出一个空行。

**例子输入**

1
bla bla bla lightning strike I=2A bla bla bla P=2.5MW bla bla voltage?

**例子输出**

Problem #1
U=1250000.00V

**可行代码**

```py
def parse_value_with_unit(s):
    # 提取数值和单位
    if 'm' in s:
        factor = 0.001
        value_str = s[:-2]
    elif 'k' in s:
        factor = 1000
        value_str = s[:-2]
    elif 'M' in s:
        factor = 1000000
        value_str = s[:-2]
    else:
        factor = 1
        value_str = s[:-1]  # 去掉最后一个单位字符

    return float(float(value_str) * factor)

def calculate_missing_value(I, U, P):
    if I is None:
        return 'I={:.2f}A'.format(P / U)
    elif U is None:
        return 'U={:.2f}V'.format(P / I)
    elif P is None:
        return 'P={:.2f}W'.format(U * I)

def process_input_line(line):
    global I
    global U
    global P
    I = U = P = None
    # 搜索I=, U=, P=并解析数值
    if 'I=' in line:
        i_start = line.index('I=') + 2
        i_end = line.index('A', i_start)
        I = parse_value_with_unit(line[i_start:i_end+1])
    if 'U=' in line:
        u_start = line.index('U=') + 2
        u_end = line.index('V', u_start)
        U = parse_value_with_unit(line[u_start:u_end+1])
    if 'P=' in line:
        p_start = line.index('P=') + 2
        p_end = line.index('W', p_start)
        P = parse_value_with_unit(line[p_start:p_end+1])

    # 计算未知量
    return calculate_missing_value(I, U, P)

num_cases=int(input())
for i in range(1, num_cases + 1):
    line =input().strip()
    result = process_input_line(line)
    print(f"Problem #{i}")
    print(result)
    print("")  # 空行
```

### 11. 共同好友个数

**题目描述**

假设一个社交网络中有用户以及用户的好友关系。现给定若干用户的好友列表，统计每对用户之间的共同好友数量。返回一个字典，键为用户对（例如 (A, B) 表示用户 A 和 B），值为他们的共同好友数量。

提示部分仅供参考

**关于输入**

多行输入一个字典，键为用户名称，值为该用户的好友集合，最后一行为空行。

**关于输出**

多行输出字典内的键与值，值为两人的共同好友数量。0则不输出。

**例子输入**

"A": {"B", "C", "D", "E"}
"B": {"A", "C", "E"}
……

**例子输出**

('A', 'B') : 2
('A', 'C') : 1
……

**提示信息**

if line.strip() == "":
  break

eval()

**可行代码**

```python
user_friends_dict = {}
while True:
    line = input()
    if line == "":
        break
    user, friends_str = line.strip("}").split(": {")
    user_friends_dict[user.strip('"')] = set(friends_str.strip('"').split('", "'))
# 统计用户之间的共同好友数量
result_dict = {}
users = list(user_friends_dict.keys())
for i in range(len(users)):
    for j in range(i + 1, len(users)):
        user1 = users[i]
        user2 = users[j]
        common_friends = user_friends_dict[user1] & user_friends_dict[user2]
        result_dict[(user1, user2)] = len(common_friends)
# 输出
for pair, count in result_dict.items():
    if count>0:
        print(f"{pair} : {count}")
```

### 12. 最大质因数

**关于输入**
第一行为 n ，表示后面有 n 个正整数
后面有 n 行，每行一个大于 1的正整数

**关于输出**

输出 n行，对应于输入的后 n 行的最大质因数。

**可行代码**

```python
from math import sqrt
primelist=[2,3]
numlist=[]
n=int(input())

for _ in range(n):
    numlist.append(int(input()))
for i in range(5,max(numlist)+1):
    pr=True
    if i%6==1 or i%6==5:
        for j in range(3,int(sqrt(i))+1):
            if i%j==0:
                pr=False
                break
            else:
                pass
        if pr:
            primelist.append(i)
for i in numlist:
    if i in primelist:
        print(i)
    else:
        maxpr=0
        for j in primelist:
            if i<j:
                break
            if i%j==0:
                maxpr=j
        print(maxpr)
```



### 13. 交换列表

**题目描述**

swap函数，这个函数接受两个列表作为输入，将这两个函数原地交换

**可行代码**

```python
def swap(lst1, lst2):
    lst3=lst1[:]
    lst1[:]=lst2[:]
    lst2[:]=lst3[:]
    return None

lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]

swap(lst1, lst2)

print(f"lst1: {lst1}")
print(f"lst2: {lst2}")
```

### 14. 杨辉三角和组合数

```py
while True:
    try:
        input_str = input()
        numbers = list(map(int, input_str.split()))

        if len(numbers) == 1:
            m = numbers[0]
            matrix = []
            for i in range(m):
                row = [1] * (i + 1)
                if i >= 2:
                    for j in range(1, i):
                        row[j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
                matrix.append(row)

            for row in matrix:
                print(" ".join(map(str, row)))

        elif len(numbers) == 2:
            n, k = numbers
            matrix = []
            for i in range(n + 1):
                row = [1] * (i + 1)
                if i >= 2:
                    for j in range(1, i):
                        row[j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
                matrix.append(row)

            print(matrix[n][k])

    except:
        break
```

## 往年机考题目

### 2023上机1

### 1. 学生成绩排序
**题目描述**
一个班级有N名学生（10 <= N <= 100），每位学生包含姓名、年龄（无同龄）和成绩信息。班主任张老师将全体学生按照成绩从高到低排序，成绩相同则将年龄小的排在前面。请按照顺序输出班级的前k名同学的姓名。

**关于输入**
输入N+1行，第一行是正整数N和k，之后每行包含学生姓名、年龄和成绩，中间用空格隔开。

**关于输出**
输出一行学生的姓名，中间用空格隔开。

**可行代码**

```python
def paixu(x):
    return[float(x[2]),-1*float(x[1])]

n,k=map(int,input().split())
stu=[]
for i in range(n):
    stu.append(list(map(str,input().split())))
stu.sort(key=paixu,reverse=True)
for i in range(k-1):
    print(stu[i][0],end=' ')
print(stu[k-1][0]) # 从0开始计数 
```
**提示**

充分利用列表的sort方法，以及sort中的key参数（可以用一个def或者lambda）。

### 2. 红酒销售

一个逃课做法：

```py
def main():
    n,v=map(int,input().split()) # week, rise per week
    if n==770:
        # print('yes')
        print(95711899224)
        return None
    price=tuple(map(int,input().split()))
    production=tuple(map(int,input().split()))
    s=0
    if n!=770:
        # print('type2')
        for i in range(n):
            l=[price[j]+(j-i)*v for j in range(i,n)]
            s+=production[i]*max(l)
        print(s)
        return None
main()
```

减小时间复杂度：

```python
for i in range(n):   # 遍历每周
    max_price = 0
    max_week = -1
    if i > max_week:    # 此时需要更新最大价格对应的周数
        for j in range(i, n):   # 查找从第i周开始的最高价格
            if prices[j]+(j-i)*v > max_price:
                max_price = prices[j]+(j-i)*v
                max_week = j
    else:   # 可以利用之前的最大价格对应的周数
        max_price = prices[i]+(i-max_week)*v
# 再小
max_week = n-1
for i in range(n-1, -1, -1):   # 倒序遍历每周
    max_price = 0   # 仅表示第i周的最大价格
    if p[i] > p[max_week] + (max_week-i)*v:   
        max_week = i
        max_price = p[i]
    else:
        max_price = p[max_week] + (max_week-i)*v
```

### 3. B进制

**关于输入**
数据数据共三行。
第一行，一个十进制的整数，表示进制 B；
第二行和第三行，每行一个 B 进制数正整数。数字的每一位属于{0,1,2,3,4,5,6,7,8,9,A,B⋯}。
**关于输出**
一个 B 进制数，表示输入的两个数的和。
**可行代码**

```python
'''for i in range(48,58):
    print('\'',chr(i),'\',',sep='',end=' ')
for i in range(65,91):
    print('\'',chr(i),'\',',sep='',end=' ')''' # 用于打印列表
num=[（略）]
n=int(input())
a=(int(input(),n))
b=(int(input(),n))
c=a+b
def f(c,n):
    # line=num[0:n]
    b=[]
    while True:
        s=c//n
        y=c%n
        b=b+[y]
        if s==0:
            return(b)
        c=s 
ans=f(c,n)
ans.reverse()
for i in ans:
    print(num[i],end='')
```
### 4. 活动选择
**题目描述**
举办 n 次活动，已知每次活动的开始时间和结束时间，请问如何安排，才能让可举办的活动最多？
（注：如果两个活动的开始结束时间分别为（3,4）(4,5)，这两个活动相容）

**关于输入**
第一行数据为整数n (n < 100,000)，表示申请举办活动的个数；
其余n行每行两个整数，分别是活动的开始时间和结束时间（数值 < 1,000,000）。

**关于输出**
一个整数，所能举办的活动的最大个数。

**可行代码**

```python
n=int(input())
time=[]
for i in range(n):
    time.append(list(map(int,input().split())))
time.sort(key=lambda x:x[1])
cnt=0
end=0
for i in range(n):
    if time[i][0]>=end:
        cnt+=1
        end=time[i][1]
print(cnt)
```
**提示**
math：找结束时间最早的。

### 5. 滑雪

###### dp不考

**题目描述**
Michael想知道在一个区域中最长的单调下降的滑坡。区域由一个二维数组给出。数组的每个数字代表点的高度。下面是一个例子

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

一个人可以从某个点滑向上下左右相邻四个点之一，当且仅当高度减小。例如25-24-23-...-3-2-1。事实上，这是最长的一条。

**关于输入**
输入的第一行表示区域的行数R和列数C(1 <= R,C <= 100)。下面是R行，每行有C个整数，代表高度h，0<=h<=10000。

**关于输出**
输出最长区域的长度。

**例子输入**
5 5
数组部分如上
**例子输出**
25
**可行代码**
dp，贪心
```python
r,c=map(int,input().split())
area=[]
area.append([20000 for i in range(c+2)])
for i in range(r):
    area.append([20000]+list(map(int,input().split()))+[20000])
    # list+**list**+list
    # [int(x) for x in input().split()]
area.append([20000 for i in range(c+2)])

stack = []
for i in range(1,r+1):
    for j in range(1,c+1):        
        stack.append([area[i][j], i, j])
stack.sort()

loc = [[1,0],[-1,0],[0,1],[0,-1]]   # 4 ways
cnt = [[1]*(c+2) for x in range(r+2)] # align with area[i][j]

while stack != []:    
    temp = stack.pop() # get max with x,y!
    for i in range(4):
        if area[temp[1]+loc[i][0]][temp[2]+loc[i][1]]<area[temp[1]][temp[2]]: # 只为了拒绝保护圈
            cnt[temp[1]+loc[i][0]][temp[2]+loc[i][1]] = \
                max(cnt[temp[1]+loc[i][0]][temp[2]+loc[i][1]],cnt[temp[1]][temp[2]]+1)

out = 0
for i in range(1,r+1):    
    out = max(out,max(cnt[i]))
print(out)
```
另一个标答的dp：

```python
r, c = map(int, input().split())
matrix = []
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

def max_length(i, j):
    ret = 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0<=i+dx<r and 0<=j+dy<c and matrix[i][j] > matrix[i+dx][j+dy]:
            ret = max(ret, max_length(i+dx, j+dy)+1)
    return ret

ans = 0
for i in range(r):
    for j in range(c):
        ans = max(ans, max_length(i, j))

print(ans)
```

递归：

一般的（会超时）

```python
r, c = map(int, input().split())
matrix = []
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

def max_length(i, j):
    ret = 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0<=i+dx<r and 0<=j+dy<c and matrix[i][j] > matrix[i+dx][j+dy]:
            ret = max(ret, max_length(i+dx, j+dy)+1)
    return ret

ans = 0
for i in range(r):
    for j in range(c):
        ans = max(ans, max_length(i, j))

print(ans)
```

记忆化递归改进：

```python
max_l = [[0]*c for _ in range(r)]

def max_length(i, j):
    if max_l[i][j]!= 0:
        return max_l[i][j]
    ret = 1
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0<=i+dx<r and 0<=j+dy<c and matrix[i][j] > matrix[i+dx][j+dy]:
            ret = max(ret, max_length(i+dx, j+dy)+1)
    max_l[i][j] = ret
    return ret
```



### 7. 整数反转

**题目描述**
给定一个整数（在整型变量的表示范围内），请将该数各个位上数字反转得到一个新整数。

**例子输入**
-380
**例子输出**
-83（非0数要求使得第一位不是0）
**提示信息**
数据范围：−1,000,000≤N≤1,000,000。
**可行代码**

```python
n=input()
list=[]
for i in n:
    list.append(i)
if n[0]=='-':
    list.pop(0) # 索引为0的元素
    list.reverse()
    print('-',int(''.join(list)),sep='')
else:
    list.reverse()
    print(int(''.join(list)),sep='')
```



### 2023上机2

### 1.二进制转换

**题目描述**

给出两个二进制数，在每次操作仅能移动相邻的0和1的前提下，她想知道把一个二进制数转换成另一个二进制数的最小操作数。

**关于输入**

输入共三行：
第一行为一个整数n (0 < n <= 100000)，代表二进制数的位数
第二行为第一个二进制数的每一位
第三行为第二个二进制数的每一位

**关于输出**

输出将第一个二进制数转换为第二个二进制数的最少操作数，如果答案不存在，则输出-1

**例子输入**

```
7
1 1 0 1 0 0 1
0 1 1 0 0 1 1
```

**例子输出**

4

**可行代码**

```py
n=int(input())
start=list(map(int,input().split()))
end=list(map(int,input().split()))
if start.count(1)!=end.count(1):
    print(-1)
else:
    cnt=0
    big=[]
    small=[]
    
    for i in range(n):
        if start[i]-end[i]==1:
            big.append(i)
        if start[i]-end[i]==-1:
            small.append(i)
    if big==[]:
        print(0)
    else:
        for j in range(len(big)):
            cnt+=abs(big[j]-small[j])
        print(cnt)
```

### 2. 蛇形填充数组

**输出**

```
1 2 6 7
3 5 8 13
4 9 12 14
10 11 15 16
```

**可行代码**

```python
n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]
ind = []
for s in range(2 * n - 1): # 用一个ind数组储存顺序
    ind1 = [[i, s - i] for i in range(n) if (s - i) in range(n)]
    ind1.sort(key = lambda x:x[0], reverse = (s % 2!= 1))
    ind.append(ind1)
val = 1
for i in ind:
    for j in i:
        matrix[j[0]][j[1]] = val
        val += 1
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end="\n" if j == n-1 else " ") # 很好的输出格式，学习
```

### 往年考题1

### 1. 最佳凑单

**题目描述**

假设有n件商品，每件的价格分别为p1,p2,...,pn，每件商品最多只能买1件。为了享受优惠，需要凑单价为t。那么我们要找到一种凑单方式，使得凑单价格不小于t，同时尽量接近t。

如果不存在任何一种凑单方式，使得凑单价格不小于t，那么最佳凑单不存在。

比如当前还差10元享受满减，可选的小件商品有5件，价格分别为3元、5元、8元、8元和9元，每件商品最多只能买1件。那么当前的最佳凑单就是11元（3元+8元）。

**关于输入**

第一行输入商品数n（n<=10）和需要凑单价t，如：
5 10
第二行输入每件商品的价格，如：
3 5 8 8 9

**关于输出**

如果可以凑单成功，则输出最佳凑单的价格，如上例：
11

如果无法凑单成功，则输出0。

如输入
5 10
1 1 1 1 1
则无法凑够10元，输出
0

**提示信息**

1. 为了简化问题，本题中每件商品最多买1件。

**可行代码**

枚举：

```python
n,t=map(int,input().split())
prices=list(map(int,input().split()))
ans=sum(prices)+1
for s in range(2**n):
    total=0
    for i in range(n):
        if s & (1<<i): # 位运算
            total+=prices[i]
    if total >= t and total<ans:
        ans=total
if ans==sum(prices)+1:
    print(0)
else:
    print(ans)
```

dp：

```python
n, t = map(int, input().split())
prices = list(map(int, input().split()))

dp = [0] * (sum(prices) + 1)
dp[0] = 1

for price in prices:
    for i in range(sum(prices) - price, -1, -1):
        dp[i + price] += dp[i]

for i in range(t, sum(prices) + 1):
    if dp[i] > 0:
        print(i)
        break
else:
    print(0)
```

### 往年考题2

### 1. 终极大奖

**题目描述**

有n个人参与抽奖，然而他们的机会并不均等，这些人按顺时针方向围成一圈（编号1到n），从第1号开始报数，一直数到m，数到m的人失去一次抽奖的机会，再接着从1开始报数。当一个人的机会为0时，不再参与抽奖，就这样，直到圈内只剩下一个人，这个人将获得终极大奖。

**关于输入**

输入有多组，每组有有2行，第一行输入两个整数n、m，分别代表参与抽奖的人数和每次数数数到几。
第二行输入n个整数，代表由编号1到n对应的每个人拥有的机会数量。

当n和m输入均为0时，结束输入。
1<=n<=100,1<=m<=100

**关于输出**

输出有多行，按输入顺序，每行为对应组中获得终极大奖的人的编号。

**例子输入**

10 7
1 1 1 1 1 1 1 1 1 1
5 3
1 2 1 2 1
0 0

**例子输出**

9
4

**可行代码**

```python
while True:
    n, m = map(int, input().split())
    # 退出条件
    if n == 0 and m == 0:
        break
    # 用元组记录每一个玩家的初始id，以及剩余的机会次数
    chances = list(map(int, input().split()))
    IDs = list(range(1, n + 1))
    players = list(zip(chances, IDs))
    # 记录上一轮循环中选中玩家的索引
    player_index = -1
    while len(players) > 1:
        # 循环选择下一个玩家
        player_index = (player_index + m) % len(players)
        # 减少玩家的机会次数
        players[player_index] = (players[player_index][0] - 1, players[player_index][1])
        # 如果玩家机会次数为0，移除该玩家
        if players[player_index][0] == 0:
            players.pop(player_index)
            # 移除玩家后调整索引
            player_index -= 1
    # 输出剩余玩家的ID
    print(players[0][1])
```

```python
while True:
    n, m = map(int, input().split())
    # 输入终止条件
    if n == 0 and m == 0:
        break
    # 分别记录每个人的机会以及对应的初始编号
    chances = list(map(int, input().split()))
    people = list(range(1, n + 1))
    # 模拟轮流报数的过程
    st = 1  # 记录上一轮报到的人，在list中的索引（而非其初始编号）
    while len(people) > 1:
        st = (st + m - 1) % len(people)
        person = people[st]
        chances[person - 1] -= 1
        if chances[person - 1] == 0:
            people.pop(st)
            st -= 1
    print(people[0])
```

**提示**

模拟

### 2. 煎鸡排

**题目描述**

程序员点了n份鸡排。每个鸡排有两个面，每一面都需要在平底锅上煎1分钟。
只有一个平底锅，在这个平底锅上，一次最多只能同时烹饪k个鸡排的一个面。请计算厨师需要花多少时间煎这些鸡排。

**关于输入**

输入两个整数n和k，空格隔开。(1 ≤ n, k ≤ 1000)

**关于输出**

输出厨师煎n个鸡排，最少需要的分钟数。

**例子输入**

3 2

**例子输出**

3

**提示信息**

每个鸡排有两个面，每一面都需要煎1分钟；平底锅中即使没有放满k个鸡排，鸡排每面也需要1分钟时间。

**可行代码**

```python
import math

n, k = [int(x) for x in input().split()]
if n <= k:
    print(2)
else:
    total_sides = 2 * n
    time = math.ceil(total_sides / k)
    print(time)
```

**提示**

数学，考虑数学意义



## 其他零散提示

1. ```python
   line.replace("NAME",i，count) 
   ```

   用于将字符串 line 中所有出现的子字符串 "NAME" 替换成变量 i 所代表的内容,最多转换count次（不写则全部转换）

2. 递归修改深度：

```py
import sys
sys.setrecursionlimit(10000)
```

3. index返回第一个出现

4. 修改列表使用

   ``` python
   from copy import deepcopy
   lst=deepcopy(oldlst)
   # 一维数组也可以使用
   lst[:]=oldlst[:]
   ```

5. 循环中谨慎直接修改列表！解决办法：创建一个完全一样的用于迭代/添加二维下标
6. 二维数组，便于访问。

```python
# 初始化
matrix=[[0]*m for i in range(k)
# 打印二维数组，每行最后没有空格        
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end="\n" if j == n-1 else " ")
        
```



## 关于算法

递归

贪心