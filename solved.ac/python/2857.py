cnt =0 
for i in range(5):
  person = input()
  if person.find('FBI') > -1:
    print(i + 1, end = ' ')
    cnt += 1
    # print(person)

if cnt == 0 :
  print('HE GOT AWAY!')
