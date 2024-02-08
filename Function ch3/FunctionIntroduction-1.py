# Functions are like a mini-program that you can create to do a specific job. It's a way to group together code that you want to use over and over again. Functions make your code cleaner and easier to understand.

# to make a function make sure the first line is a def statement followed by your functions name and then indent next line and write your functions code
# ex:
def usersName():
    nameUser = input('what is your name: ')
    print(f'Hello {nameUser}')
#bellow is how you call a function, you can call a function as many times as you want
usersName()



#def statements with Parameters
# a parameter is an argument stored in a function inbetween the perenthesis()
# ex below:
def hello(name):
    print(f'hello {name}')

#below now when calling hello I have to fill in the parameter
hello('Megan') #it will print hello Megan
#REMEMBER that the parameter you put is forgoten after execution so if you type print(name) after hello('megan') it would give you an error





