x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.append(y)
print('x:', x)

x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y)
print('x:', x)


x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.append(y)
print('x:', x)

x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.extend(y)
print('x:', x)


x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.append(y)
print('x:', x)

x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.extend(y)
print('x:', x)