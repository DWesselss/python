x = True
y = False

# Versie A — negeer de gehele expressie
if not (x and y):
    print("Conditie A voldaan")

# TODO: Versie B — herschrijf met De Morgan
# not (A and B) == (not A) or (not B)
if not x or not y:
    print("Conditie B voldaan")

# Test met vier combinaties: (True, True), (True, False), (False, True), (False, False)
# Welke versie is leesbaarder en waarom?