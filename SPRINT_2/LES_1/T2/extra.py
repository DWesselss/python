print(ord("A"))  # 65
print(ord("a"))  # 97
print(ord("Z"))  # 90
print(ord("z"))  # 122

print("Zebra" < "appel")  # True
print("ZEBRA" < "appel")  # True

# Case-insensitief vergelijken:
print("Zebra".lower() < "appel".lower())  # False
print("ZEBRA".lower() < "appel".lower())  # False