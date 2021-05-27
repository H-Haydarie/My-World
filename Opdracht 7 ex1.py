# Exercise 1

# Create a variable that contains a list of five names.
# Loop over the list using a for loop. Print every individual name in the list on a new line

list = ["Haydar", "Doreen", "Rene", "Raäfet", "Oalid"]
for x in list:
   print(x)


# Exercise 2
# Create a list of five integers.
# Use a for loop to do the following for every item in the list:
# Print the value of that item added to the value of the next item in the list. If it is the last item, add it to the value of the first item instead (since there is no next item).

numbers = [5, 10, 15, 20, 25]
for i in range(len(numbers)):
    try:
        print (numbers[i]+numbers[i+1])
    except:
        print (numbers[-1]+numbers[0])
    