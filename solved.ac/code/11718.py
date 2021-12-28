while True:
  try:
    a = input()
    if len(a) <= 0 : 
      raise ValueError
    print(a)
  except:
    break