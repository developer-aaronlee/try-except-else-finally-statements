# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error:
#     print(f"{error} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file closed")

# raise TypeError("not an error")

height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("invalid height")

bmi = weight / height ** 2
print(bmi)