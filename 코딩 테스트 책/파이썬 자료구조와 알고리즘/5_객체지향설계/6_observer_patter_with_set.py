class Subscriber(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0}, {1}".format(self.name, message))

class Publisher(object):
    def __init__(self):
        self.subscribers = set()
    
    def register(self, who):
        self.subscribers.add(who)
    
    def unregister(self, who):
        self.subscribers.discard(who)
    
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

pub = Publisher()
hyunjin = Subscriber("현진이")
james = Subscriber("제임스")
jeff =Subscriber("제프")

pub.register(hyunjin)
pub.register(james)
pub.register(jeff)

pub.dispatch("점심시간입니다.")
pub.unregister(jeff)
pub.dispatch("퇴근이나해라")