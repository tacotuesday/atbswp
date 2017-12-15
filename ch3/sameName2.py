def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'     # No local eggs variable created, since 'spam' assignment was global.
spam()
print(eggs)
