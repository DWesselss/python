print("Dit werkt nog")
print = "Tello"
print("Dit werkt niet meer")

# TypeError: 'str' object is not callable

list = [1, 2, 3]
list()

# TypeError: 'list' object is not callable

str = "Tello"
str(10)

# TypeError: 'str' object is not callable

# De TypeError komt pas bij het aanroepen, omdat het maken van de
# variabele wel mag. Python probeert daarna tekst of een lijst aan te roepen.
# In een groot script zoek ik naar "print =", "list =" of "str =".