# An online retailer provides express shipping for many of its items at a rate of $10.95
# for the first item, and $2.95 for each subsequent item. Write a function that takes the
# number of items in the order as its only parameter. Return the shipping charge for
# the order as the function’s result. Include a main program that reads the number of
# items purchased from the user and displays the shipping charge.


#below will be our main funtion
def main(numberItems):
    summary = 10.95
    if numberItems >= 1:
        summary += (numberItems * 2.95)
        print(f'Here is your item summary: ${summary}')
    elif numberItems == 0:
        summary = 0
        print(f'here is your Item summary: ${summary}')


customerNum = int(input(('welcome customer put the amount of items that you want to purchase:')))
if __name__ == "__main__":
    main(customerNum)

