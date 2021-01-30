def add_numbers(number1, number2):
    print ("Main do numbers ko add karunga.")
    print (number1 + number2)
add_numbers(120, 50)
num_x = 134
name = 12
add_numbers(num_x, name) 

print("**********************************************")

def say_hello_people(name_x, name_y, name_z, name_a):
    print ("Namaste ", name_x) # hindi mein
    print ("Alah hafiz ", name_y) # urdu mein
    print ("Bonjour ", name_z) # french mein
    print ("Hello ", name_a) # english mein
say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev") 



print("*****************************************************")

def icecream(*flavours):
    for flavour in flavours:
        print("i love"+flavour)

icecream("chocolate", "butterscotch","vanilla","strawberry") 


print("****************************************************")

def attendance(name,status="absent"):
    print(name,"is",status," today")

attendance("kartik","present")
attendance("sonu")
attendance("vishal","present")
attendance("umesh") 


print("**************************************************************")



def add_numbers(number_x, number_y):
    number_sum = number_x + number_y
    return number_sum

sum1=add_numbers(20, 40)
print (sum1)
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print (sum2)
print (sum3)
number_a = add_numbers(20, 40) // add_numbers(5, 1)
print (number_a) 


print("*****************************************************")


def add_numbers_print(number_x, number_y):
    number_sum = number_x + number_y
    print (number_sum)
sum4 = add_numbers_print(4, 5)
print (sum4)
print (type(sum4)) 
