import time
def classic_fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        say = 'FizzBuzz!'
    elif number % 5 == 0:
        say = 'Buzz!'
    elif number % 3 == 0:
        say = 'Fizz!'
    else:
        say = str(number)
    
    return say
    
c=0
while 1 == 1:
    print(classic_fizzbuzz(c))
    c += 1
    time.sleep(1/10)