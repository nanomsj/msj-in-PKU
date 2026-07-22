古堡探险，路径找max

```python
def max_value(i, j, N, grid):
    # 边界条件，如果到达右下角，返回该位置的宝物价值
    if i == N - 1 and j == N - 1:
        return grid[i][j]
    
    # 如果已经超出边界，返回负无穷（不能走到这些地方）
    if i >= N or j >= N:
        return 0
    
    # 递归地选择向下或向右走
    # 向下走
    down_value = max_value(i + 1, j, N, grid)
    # 向右走
    right_value = max_value(i, j + 1, N, grid)
    
    # 返回当前房间的宝物价值加上两者中较大的选择
    return grid[i][j] + max(down_value, right_value)

# 输入处理
N = int(input())  # 读取N
grid = [list(map(int, input().split())) for _ in range(N)]  # 读取宝物价值矩阵

# 从(0, 0)开始计算最大宝物价值
result = max_value(0, 0, N, grid)
print(result)
```

```python
def max_treasure(N, grid):
    # 初始化 DP 数组
    dp = [[0] * N for _ in range(N)]
    
    # 初始化起点
    dp[0][0] = grid[0][0]
    
    # 填充第一行
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # 填充第一列
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # 填充其他位置
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # 返回右下角的最大宝物价值
    return dp[N-1][N-1]

# 输入处理
N = int(input())  # 房间数
grid = [list(map(int, input().split())) for _ in range(N)]  # 宝物价值矩阵

# 计算最大宝物价值
result = max_treasure(N, grid)
print(result)
```

不用re的表达式匹配：

```python
def isMatch(p, s):
    # 获取 p 和 s 的长度
    m, n = len(p), len(s)
    
    # 创建动态规划表 dp，大小为 (m+1) * (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # 初始条件：dp[0][0] = True
    dp[0][0] = True
    
    # 处理 p 中以 '*' 开头的情况
    for i in range(1, m + 1):
        if p[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    
    # 填充 dp 表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]  # 字符匹配或 '?' 匹配任意字符
            elif p[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # '*' 匹配 0 或多个字符
    
    # 最终结果：dp[m][n]
    return dp[m][n]

# 输入
p = input()
s = input()

# 输出结果
print(isMatch(p, s))
```

数字转换

```python
#罗马转数
def q(x):
    ans=x.count('I')+x.count('V')*5+x.count('X')*10+x.count('L')*50+x.count('C')*100+x.count('D')*500+x.count('M')*1000
    if 'IV' in x:
        ans-=2
    if 'IX' in x:
        ans-=2
    if 'XL' in x:
        ans-=20
    if 'XC' in x:
        ans-=20
    if 'CD' in x:
        ans-=200
    if 'CM' in x:
            ans-=200
    return(ans)
#数转罗马
def s(x):
    t=int(x)
    line=[]
    line.append('M'*(t//1000))
    t=t%1000
    line.append('CM'*(t//900))
    t=t%900
    line.append('D'*(t//500))
    t=t%500
    line.append('CD'*(t//400))
    t=t%400
    line.append('C'*(t//100))
    t=t%100
    line.append('XC'*(t//90))
    t=t%90
    line.append('L'*(t//50))
    t=t%50
    line.append('XL'*(t//40))
    t=t%40
    line.append('X'*(t//10))
    t=t%10
    line.append('IX'*(t//9))
    t=t%9
    line.append('V'*(t//5))
    t=t%5
    line.append('IV'*(t//4))
    t=t%4
    line.append('I'*t)
    # print(line)
    ans=''.join(line)
    return ans


n=input()

if n[0] in ['0','1','2','3','4','5','6','7','8','9']:
    print(s(n))
else:
    print(q(n))
```

最小堆

```python
import heapq


def min_cost_to_cut_rope(L, lengths):
    # 创建最小堆，将所有绳子的长度加入堆中
    heap = []
    for length in lengths:
        heapq.heappush(heap, length)

    # 总开销
    total_cost = 0

    # 进行剪切操作直到堆中只剩下一个绳子
    while len(heap) > 1:
        # 取出最小的两段绳子
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        # 当前剪切的开销是这两段绳子的总长度
        cost = first + second
        total_cost += cost

        # 将剪切后的绳子重新加入堆中
        heapq.heappush(heap, cost)

    return total_cost


# 主程序入口
if __name__ == "__main__":
    # 读取输入
    L = int(input())  # 绳子的初始长度（这个值其实不需要在计算中使用）
    lengths = list(map(int, input().split()))  # 需要的绳子长度

    # 计算最小开销
    result = min_cost_to_cut_rope(L, lengths)

    # 输出结果
    print(result)
```

copypaste

```python
def process_samples(input_lines):
    output_lines = []
    exception_type = None
    is_namespace_line = False
    is_requirement_line = False

    for line in input_lines:
        # 检查是否是分割线
        if line.startswith('-' * 64):
            output_lines.append(line)
            continue

        # 处理 [Namespace] 行
        if line.startswith('[Namespace]'):
            is_namespace_line = True
            if '-' in line:
                # 提取异常类型
                exception_type = line.split('-')[1].strip()[1:-1]
                # 移除异常标记
                line = '[Namespace]\n'
        else:
            is_namespace_line = False

        # 处理 [Requirement] 行
        if line.startswith('[Requirement]'):
            is_requirement_line = True
            if exception_type is not None:
                # 将异常类型标记添加到 [Requirement] 行
                line = f'[Requirement]-({exception_type})\n'
                exception_type = None  # 清除异常类型
        else:
            is_requirement_line = False

        output_lines.append(line)

    return output_lines

def main():
    import sys
    input_lines = sys.stdin.readlines()  # 从标准输入读取所有行
    output_lines = process_samples(input_lines)
    sys.stdout.writelines(output_lines)  # 将处理后的行写到标准输出

if __name__ == "__main__":
    main()
```

pay

```python
n=int(input())
line=[100,50,20,10]
for _ in range(n):
    t=int(input())
    lst=list(map(int,input().split()))
    tot=0
    able = True
    for i in lst:
        cnt=0
        pre=i

        if i%10 !=0:
            able=False
            break
        else:
            for j in line:
                cnt+=pre//j
                pre=pre%j
            if tot<cnt:
                print(i)
            tot=max(tot,cnt)
    if able==True:
        print(tot)
    else:
        print(-1)
```

qiafan

```python
n=int(input())
line=[100,50,20,10]
for _ in range(n):
    t=int(input())
    lst=list(map(int,input().split()))
    tot=0
    able = True
    for i in lst:
        cnt=0
        pre=i

        if i%10 !=0:
            able=False
            break
        else:
            for j in line:
                cnt+=pre//j
                pre=pre%j
            tot=max(tot,cnt)
    if able==True:
        print(tot)
    else:
        print(-1)
```