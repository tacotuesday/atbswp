def grammarer(list):
    list.insert(-1, 'and')
    for i in range(len(list)):
        print(list[i])


spam = ['apples', 'bananas', 'tofu', 'cats']
grammarer(spam)
print(spam)
