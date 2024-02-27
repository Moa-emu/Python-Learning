# NESTED DICTIONARIES AND LIST

#   - As you model more and more complicated things,you may find you need
#dictionaires  and list that contain other dictionaries and lists.Below will
#Be an example of how you can use this concept.

PartyGuest = {
    'Alice': {'jellof Rice': 4, 'Chips':3},
    'Roger': {'Brownies':5, 'hotdogs':20},
    'Muiz': {'Burgers':30, 'sodas': 20}
}

#Below will be a function that we will make to acsess everything within the dictionary
def totalBrought(guest, item):
    numBrought = 0
    #this for loop will get every item
    for k, v in guest.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought')
print('-Jellof Rice ' + str(totalBrought(PartyGuest, 'jellof Rice')))
print('-Brownies ' + str(totalBrought(PartyGuest, 'Brownies')))
print('-Burgers ' + str(totalBrought(PartyGuest, 'Burgers')))
