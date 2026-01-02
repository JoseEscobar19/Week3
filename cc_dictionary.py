inches_snow = {"Monday": 2, "Tuesday": 4, "Wednessday": 5}

# obj1: You will write code to get the inches of snow value for Thursday from user input, 
#obj2:  as well as a function to print out the number of total snowfall inches for a given dictionary.  
 
def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
        print(f"Total snowfall inches {total_inches}")

print_total_snowfall(inches_snow)

#in the dictionary, the values are integers, and the input is 
# always string, so we have to convert to integer to add
inches_snow["Thursday"] = int(input("How many inches of snow fell on Thursday?"))

print_total_snowfall(inches_snow)
