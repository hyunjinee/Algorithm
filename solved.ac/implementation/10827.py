a,b=list(input().split())

p = len(a[a.index('.')+1:]) # a의 소수점 위치. a = A * 10^p(A : 자연수)
a = a.replace('.','') # a의 소수점을 지워 A로 만듦

result = str(int(a)**int(b)) # A^b 연산 수행
p=str((10**p)**int(b)) # (10^p)^b 연산 수행
index = len(result)-len(p)+1
# index : 소수점을 붙여야 할 위치

if index >=0:
    print(result[:index]+'.'+result[index:])
else:
    print('0.'+'0'*(-index)+result)