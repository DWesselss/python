# Testverslag – Veilige takeoff

De 14 basisgevallen zijn lokaal uitgevoerd met simulatieconstanten en een minimale importstub voor djitellopy, zonder echte drone. De echte vlucht en de vijf mutatietests zijn nog niet uitgevoerd.

## Acht vaste gevallen
| Test | Afstand | Batterij | Hoogte | Temp | Wifi | Tijd | Verwacht | Werkelijk (simulatie) |
|---|---:|---:|---:|---:|---:|---:|---|---|
| T1 | 100 | 80 | 0 | 30 | 90 | 0 | GO FULL | GO FULL — geslaagd |
| T2 | 100 | 20 | 0 | 30 | 90 | 0 | Batterijguard | Batterijguard — geslaagd |
| T3 | 50 | 21 | 0 | 30 | 90 | 0 | GO ECO | GO ECO — geslaagd |
| T4 | 100 | 80 | 10 | 30 | 90 | 0 | Hoogteguard | Hoogteguard — geslaagd |
| T5 | 100 | 80 | 0 | 60 | 90 | 0 | Temperatuurguard | Temperatuurguard — geslaagd |
| T6 | 100 | 80 | 0 | 30 | 69 | 0 | Wifiguard | Wifiguard — geslaagd |
| T7 | 50 | 30 | 0 | 50 | 90 | 0 | Warm-en-bijna-leegguard | Combinatieguard — geslaagd |
| T8 | 400 | 60 | 0 | 30 | 90 | 0 | Modusafstandguard NORMAL | Modusafstandguard — geslaagd |

## Zes eigen testgevallen
| Test | Afstand | Batterij | Hoogte | Temp | Wifi | Tijd | Verwacht | Werkelijk (simulatie) | Waarom |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| E1 | 50 | 19 | 0 | 30 | 90 | 0 | Batterijguard | Batterijguard — geslaagd | Onder grens 20 |
| E2 | 50 | 20 | 0 | 30 | 90 | 0 | Batterijguard | Batterijguard — geslaagd | Precies grens 20 |
| E3 | 50 | 21 | 0 | 30 | 90 | 0 | GO ECO | GO ECO — geslaagd | Boven grens 20 |
| E4 | 100 | 35 | 0 | 30 | 90 | 0 | GO ECO | GO ECO — geslaagd | Modusgrens 35 |
| E5 | 100 | 36 | 0 | 30 | 90 | 0 | GO NORMAL | GO NORMAL — geslaagd | Modusovergang 35/36 |
| E6 | abc | 80 | 0 | 30 | 90 | 0 | Ongeldige afstand | Ongeldige afstand — geslaagd | Geen getal in invoer |

## Vijf ingebouwde fouten – zelf uitvoeren
Maak eerst een kopie van de werkende code. Breng iedere fout **apart** aan, voer tests opnieuw uit, en zet de werkende code terug.

| Fout | Gefaalde testnummers | Crash of verkeerde uitvoer? | Beste vangtest |
|---|---|---|---|
| 1. Afstand als tekst vergelijken | Nog testen | Nog testen | E6 + twee geldige afstanden in omgekeerde tekstvolgorde |
| 2. `<=` veranderen in `<` bij batterij | Nog testen | Verwacht: stille grensfout | T2/E2 |
| 3. `is None` vervangen door controle op nul | Nog testen | Nog testen | Meting `None` vs hoogte 0 |
| 4. Guard vóór benodigde berekening plaatsen | Nog testen | Nog testen | T8 |
| 5. Happy path onder een `else` zetten | Nog testen | Kan ongewijzigde uitkomst geven | Structuurcheck, geen gedragstest |

Let op: `else` onder de laatste guard is vaak **gedragsmatig gelijk** wanneer de guard altijd `exit()` doet. De structuurcheck is dan nodig om de fout te vangen. Welke fouten in jouw uitvoering stil blijven, moet je na de mutatietests vaststellen.

## Echte drone
**Nog niet uitgevoerd.** Noteer na een begeleide vlucht: datum, gemeten batterij/hoogte/temperatuur/wifi/vliegtijd, ingestelde afstand, gekozen modus, wat er echt gebeurde en of dat met de simulatie overeenkwam. Test alleen in een geschikte ruimte en met begeleiding.

## Extra – tests met invoer
Controleer ook ` 100 `, `YES `, `-50`, `1,5`, `2.5` en lege invoer op alle drie vragen. Spaties worden met `.strip()` verwijderd; de overige ongeldige afstanden worden door `.isdigit()` geweigerd.

## Uitwisseling met klasgenoot
- Wat ik bij een ander vond: nog in te vullen na uitwisseling.
- Wat een ander bij mij vond: nog in te vullen na uitwisseling.
