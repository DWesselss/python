x = True
y = False

# Versie A
if not (x and y):
    print("Conditie A voldaan")

# Versie B met De Morgan
if not x or not y:
    print("Conditie B voldaan")