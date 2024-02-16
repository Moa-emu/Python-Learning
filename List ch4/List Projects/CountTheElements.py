#This is Exercise 121

# Python’s standard library includes a method named count that determines how
# many times a specific value occurs in a list. In this exercise, you will create a new
# function named countRange which determines and returns the number of elements
# within a list that are greater than or equal to some minimum value and less than some
# maximum value. Your function will take three parameters: the list, the minimum
# value and the maximum value. It will return an integer result greater than or equal to
# 0. Include a main program that demonstrates your function for several different lists,
# minimum values and maximum values. Ensure that your program works correctly
# for both lists of integers and lists of floating point numbers.


def countRange(minValue,maxValue,list):
    #Below I will have to initialize the counter to 0 before we use it
    #if we do not initailize it, it will be undefined
    numCounted = 0
    for e in list:
        if e >= minValue and e < maxValue:
            #Below will increment the counter by the amount of times an item e meets the if statement
            numCounted += list.count(e)

    return(numCounted)
     



def main():
    usersList = []
    while True:
        print('Type 0 when you are done')
        userAdd = int(input('Type numbers that you will add to a list: '))
        
        #Below will be the condition to break the loop
        if userAdd == 0:
            break
        else:
            usersList.append(userAdd)
    print(f'Here is your list: {usersList}')
    minValue = int(input('now type a min Value: '))
    maxValue = int(input('now type a max value: '))

    countNumber = countRange(minValue, maxValue, usersList)

    print(f'Here is the count of items:\n-These items are greater or equal to the min value\n-The items are also less than the max value:{countNumber}')





if __name__ == "__main__":
    main()
