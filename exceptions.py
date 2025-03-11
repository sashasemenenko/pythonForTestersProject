# try:
#     total = 5 + "10" # TypeError
# except (TypeError, ValueError):
#     print("You can't add string to an int")
#
# # raise ValueError("Custom error message")
#
# class CustomError(Exception):
#     pass
#
# raise CustomError("Our custom error")
#
#
# # int_value = int("Hello") # ValueError
#
# # list = [1, 2, 3]
# # print(list[3]) # IndexError
#

try:
    print(5 + "10")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")
