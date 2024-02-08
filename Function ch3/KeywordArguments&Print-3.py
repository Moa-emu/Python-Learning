#KEYWORD ARGUMENTS and PRINT
#- these are often used for optional parameters
#ex: if you have not noticed the print parameter as the optional argument of (end = '') whicn can disable the newline feature on print
print('hello ', end='')
print('world') #this will print hello world
# output put on the same line becuse newline disabled
#Another thing that you can do is to for print is to place commas which will automatically seperate them
print('cats', 'dogs', 'mice') #it will print: cats dogs mice
#you can even use the sep keyword argument to change every comma to be looked at as a space
print('cats', 'dogs', 'mice', sep='') #this will output cats,dogs,mice

#REMEMBER that you can add your own optional keyword arguments to your own function but we will look at that much later
