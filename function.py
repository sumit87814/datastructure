#declaring function
def sum(a,b):
    return a+b
my_sum=sum(5,7)
print(my_sum)

#local scope

def my_fun():
    var=10
    print(var)

my_fun()  # 10
# print(var)  # NameError: var is not defined

#You can also use the (global) keyword to modify a global variable:

my_var=10

def change_var():
    global my_var   # Allows modification of a global variable
    my_var=20

change_var()  #20
print(my_var)


#Another type of loop you can use in Python is the while loop. This type of loop will repeat a block of code until the condition is False. Here is an example of using a while loop for a guessing game:

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

#The continue statement is used to skip the current iteration of a loop and move onto the next iteration. Let's modify the example from earlier to use the continue statement instead of break:

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

    developer_names = ['Jess', 'Naomi', 'Tom']


#The break statement is used to stop the execution of a loop. Here is an example of using the break statement for a list of developer_names

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

#Both for and while loops can be combined with an else clause, which is executed only when the loop is not terminated by a break statement. Here is an example of using multiple for loops:

words=['sky','sumit', 'fly','orange','aeiou']

for word in words:
    for letter in word:
        if letter.lower() in 'aeious':
            print(f'{word} contain the vowel {letter}')
            break
    else:
        print(f'{word} has no vowel')
