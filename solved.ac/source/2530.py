h,m,s = map(int,input().split())

splus = int(input())


fulltime= h*3600 + m *60 + s
addedtime=fulltime + splus

addedtime = addedtime %86400

hour = addedtime //3600
minute = (addedtime-hour*3600)//60
second = addedtime - hour*3600 - minute*60

print(hour, minute, second)