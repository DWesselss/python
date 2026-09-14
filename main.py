tekst = "3"
getal = 5

print(type(tekst))
print(type(getal))

# In JavaScript wordt "3" + 5 de tekst "35". Omdat een van de waarden
# tekst is, gebruikt JavaScript de + om de waarden aan elkaar te plakken.
#
# In PHP wordt "3" + 5 het getal 8. PHP gebruikt + om op te tellen en
# zet de numerieke tekst "3" daarvoor om naar het getal 3. Voor het aan
# elkaar plakken van tekst gebruikt PHP een punt (.).
#
# Een TypeError ontstaat wanneer een bewerking niet mogelijk is met de
# gebruikte datatypes, zoals het optellen van een str en een int.
# Een ValueError ontstaat wanneer het datatype wel wordt geaccepteerd,
# maar de inhoud van de waarde ongeldig is, bijvoorbeeld int("drie").
#
# Verwachte foutmelding:
# TypeError: can only concatenate str (not "int") to str

resultaat = tekst + getal
