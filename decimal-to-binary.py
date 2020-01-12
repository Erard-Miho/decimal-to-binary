#def decimal_to_binary(number):
binary_list = [] #make empty list
number = int(input('add number '))
    #old_number = number  # reference number
    
while (number > .5):   # Loop
    if number % 2 != 0:  # if the number is a .5
        binary_list.append(1)  # this will append 1 at the list
    else:
        binary_list.append(0)  # this will append 0 at the list
    
    number /= 2 # set the variablle to the new number
    number = int(number)
    print(binary_list)
    print()
print("The binary from for " + str(number) + " is: ")
print(*binary_list[::-1]) # print the list to show correctly.
    
