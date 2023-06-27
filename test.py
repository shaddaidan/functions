def collatz(number):
    if ((number % 2) == 0):
        #print(number // 2)
        return number // 2
    else :
        #print(3 * number + 1)
        return 3 * number + 1
    # this is our initial function

#from here is the start of our program

try:
    print('input a number: ', end='')

    ref = input()
    while True:
        print(collatz(int(ref)))
        print(' ')
        ref = collatz(int(ref))
        if int(ref) == 1:
            break

    print('you are welcome from shaddai')

except:
    ValueError
    print('value isnt an integar')