def spam(dev) :
    try:
        return 42 / dev
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(12))
print(spam(45))
print(spam(90))
print(spam(0))
print(spam(78))