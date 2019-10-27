from random import randint
def pick_a_number():
    number = randint(1,10)
    while True:
        
        try:
            guess = int(input('pick a number! (between 1 and 10): '))
            if guess == number: break
            print('Too High' if guess > number else 'Too low!')
        except:
            print('Thats not a number')
    print(f'Well done, the number was {number}')


def think_of_a_number():
    from math import floor
    def find_the_number(low, high):
        breakpoint()
        answer = input(f'Was your number {floor((low+high)/2)}? (y for yes, l for lower, h for higher):  ').lower()
        if answer == 'y': return answer
        if answer == 'l': find_the_number(low, floor((low+high)/2))
        if answer == 'h': find_the_number(floor((low+high)/2), high)
        if answer not in 'yhl': print('That wasnt an option!')
        return find_the_number(low, high)


    print("Think of a number between 1 and 10")

    answer = find_the_number(1,10)

    print(f'Your number was {answer}!')