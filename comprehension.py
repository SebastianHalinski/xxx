import random  # wczytanie funkcji random | load function random

guesses_taken = 0  # przypisanie wartości 0 do zmiennej guesses_taken | set 0 to variable guesses_taken

print('Hello! What is your name?')  # wypisanie zawartości() | print out content
myName = input()  # przypisanie podaniej przez użytkownika wartości do zmiennej myName | Assigning values ​​to a variable

number = random.randint(1, 20)  # zwraca losowy integer z przedziału do 1 do 20 | Return a random integer number such that 1 <= number <= 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Wypisuje zmienną to co w () i zmienna myName w odpowiednim miejscu | print out content and variable in correct place

while guesses_taken < 6:  # wykonuje pętle dopuki zmienna guesses_taken >= 6 | Loops until variable >= 6
    print('Take a guess.')  # wypisuje to co w () | print out content
    guess = input()  # przypisuje do zmiennej guess wartość podaną przez użytkownika | Assigning values ​​to a variable
    guess = int(guess)  # zmienna guess ustawiona jako integer | set variable as integer

    guesses_taken += 1  # guesses_taken zwiększa wartość o 1 | increases value by 1

    if guess < number:  # jeżeli zmienna guess < od zmiennej number | if guess < number
        print('Your guess is too low.')  # wypisuje to co w () | print out content

    if guess > number:  # jeżeli zmienna guess > od zmiennej number | if guess = number
        print('Your guess is too high.') # wypisuje to co w () | print out content

    if guess == number:  # jeżeli zmienna guess = zmiennej number | if guess > number
        break  # przerwanie działania pętli while | breake while loop

if guess == number:  # jeżeli zmienna guess = zmiennej number | if guess = number
    guesses_taken = str(guesses_taken)  # ustawia zmienną guesses_taken jako string | set variable as string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')  # wypisuje to co w () oraz w odpowiednich miejscach zmienne myName oraz guesses_taken | print out content and variables in correct place

if guess != number:   # jeżeli zmienna guess nie = zmiennej number | if guess not = number
    number = str(number)  # zmienia zmienną number na string | set variable as string
    print('Nope. The number I was thinking of was ' + number)  # wypisuje to co w () oraz w odpowiednich miejscach zmienną number | print out content and variable in correct place
