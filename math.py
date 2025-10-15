


f = int(input("Enter a number"))
sec = int(input("Enter a second number"))
choice = int(input("What would you like to do with these two numbers?"))  #This was causing me problems executing,  makes sure to characterize each string/ integer appropriately.
#Me not characterizing this as an int caused my output to not function. Makesure i have them as the appropriate data types. 

sub = int(f - sec)
add = int(f + sec)
div = int(f / sec)


if choice == 2:
    print(sub)
if choice ==3:
    print (div)
if choice == 1:
    print(add)
