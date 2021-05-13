###Problem1###
##Multiples of 3 and 5##

new = 0 
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        new += i
print(new)
    
