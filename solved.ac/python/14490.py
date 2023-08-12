n, m  = map(int,input().split(":"))

# 약분을 조질려면 어떻게 해야하지? 

# 최대 공약수로 나눠야하는 거아닌가 ? 

# 두수의 최대 공약수를 구하는 방법은 뭔가? 

# 

from math import gcd 

temp = gcd(n, m) 


print(f'{n // temp}:{m//temp}')