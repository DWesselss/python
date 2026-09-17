# len(80) geeft een TypeError, omdat een int geen lengte heeft.
# print(len(80))

print(round(2.5))  # 2
print(round(3.5))  # 4

# int(1.9) wordt 1. Python verwijdert de decimalen en rondt niet af.
print(int(1.9))

# type(type(80)) geeft <class 'type'>.
print(type(type(80)))

# Banker's rounding rondt een getal dat precies op .5 eindigt af naar
# het dichtstbijzijnde even getal. Dit voorkomt dat veel afrondingen
# steeds dezelfde kant op gaan.