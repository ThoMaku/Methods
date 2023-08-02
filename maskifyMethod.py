def maskify(ID_num):
    #create and return the string for the masking of ID number
    return ID_num[:6] + "*" * len(ID_num[6:])

#add details to a dictionary
customer_details = {"THOBILE": "9905181002081",
                    "SICELO": "0811181004087",
                    "MARIA": "8110101081089",
                    "JOSEPH": "7909291008081"}

#ask for user input
name = input("Please enter your name: ")

#use a loop to heck if user input is in the dictionary
for key, value in customer_details.items():
    if key == name.upper():
        print(f"Your name is {key} with ID number {maskify(value)}")