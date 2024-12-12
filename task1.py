################################BASIC ARITHMETIC OPERATION################################
num1 = 10
num2 = 5

print("ARITHMETIC OPERATION : \n")
print(f"Addition : {num1+num2}")
print(f"Subtraction : {num1-num2}")
print(f"Division : {num1/num2}")
print(f"Multiplication : {num1*num2}\n\n")

#####################STRING MANUPULATION#################################

text = "Hello, Python!"

print("TEXT MANUPULATION : \n")
print(f"Original text: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Reversed: {text[::-1]}")
print(f"Substring (first 5 characters): {text[:5]}\n\n")


###########################CONDITIONAL STATEMENT#############################
print("CONDITIONAL STATEMENT : \n")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")
print("\n\n")

######################DATA STRUCTURES######################################
print("DATA STRUCTURES : \n")
my_list=[1,2,3,4,5]

my_list.append(6)
my_list.remove(3)
my_list[0]=10
my_list.insert(2, "hi")

print(f"updated list : {my_list}\n")


my_dict={"name":"john", "age":25, "city":"delhi"}

my_dict["gender"]="male"
del my_dict["age"]
my_dict["city"]="mumbai"

print(f"updated my_dict : {my_dict}\n")


my_tuple = (10, 20, 30, 40, 50)

print(f"Tuple Length : {len(my_tuple)}")
print(f"Tuple Maximum value : {max(my_tuple)}")
print(f"Tuple Minimum value : {min(my_tuple)}")