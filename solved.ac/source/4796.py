
count=0
#l,p,v입력받기
while 1:
  count+=1
  l,p,v=map(int,input().split()
  )
  #셋 전부 0인경우 종료
  if l==0 and p==0 and v==0:
    break
  #출력할 값 구하기 
  if v%p>=l:
    result=v//p*l+l
  else:
    result= v//p*l+v%p
  
  print("Case "+str(count)+": " +str(result) )