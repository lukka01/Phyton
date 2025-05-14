# yourValue = "3424234"
#
# if isinstance (yourValue, str):
#     try:
#         res = int(yourValue)
#         print("The result is: ", res)
#     except ValueError:
#         print("The string doesn't contain integer and can't be converted to integer.")
# elif isinstance(yourValue, int):
#     try:
#         res = str(yourValue)
#         print("The result is: ", res)
#     except ValueError:
#         print("Your input can't be converted to string")
#
#
from warnings import catch_warnings

def convert (val):
    if isinstance(val, str):
        try:
            res = int(val)
            print("Converted val: ", val)
        except ValueError:
            print("Couldn't convert")
    elif isinstance(val, int):
        res = str(val)
        print("The result is: ", res)
    else:
        print("Vajaiaa mogitya dedis muteli! ")




#
# def convert (val):
#     if isinstance(val, str):
#         try:
#             res = int(val)
#             print("Converted value: ", res)
#         except ValueError:
#             print("Can't be converted")
#     elif isinstance(val, int):
#             res = str(val)
#             print("Converted value is: ", res)
#     else:
#         print("Yle xar bidzia? ")
#
# convert(0.5)