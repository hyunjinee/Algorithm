import sys 
N = int(sys.stdin.readline()) 
mod = 9901 
no, left, right = 1, 0, 0 
for i in range(N): 
  # no, left, right = no + left + right, no + right, no + left 
  no = (no + left + right) % mod 
  left, right = no - right, no - left
sys.stdout.write(str( (no + left + right) % mod ))

