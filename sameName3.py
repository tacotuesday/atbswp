def spam():
    global eggs
    eggs = 'spam' # this is global

def bacon():
    eggs = 'bacon' # this is local

def ham():
    print(eggs) # this is global

eggs = 42 # this is the global
spam()
print(eggs)
