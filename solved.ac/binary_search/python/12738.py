n = int(input())
arr = list(map(int,input().split(" ")))

def binary_search(start,end,target):
    if start > end:
        return start
       
    mid = (start+end) // 2
    
    if res[mid] > target:
        return binary_search(start,mid-1,target)
    elif res[mid] == target:
        return mid
    else:
        return binary_search(mid+1,end,target)

res = [arr[0]]

for i in range(1,len(arr)):
    if res[-1] < arr[i]:
        res.append(arr[i])
    else:
        res[binary_search(0,len(res)-1,arr[i])] = arr[i]
    print(res)

print(len(res))