# Projectplan – Veilige takeoff

## Planning
| Stap | Werk | Tijd |
|---|---|---|
| 1 | Regels en constanten bepalen | 15 min |
| 2 | Ontwerp en guards uitwerken | 35 min |
| 3 | Invoer en invoervalidatie | 35 min |
| 4 | Simulatie en sensoren | 15 min |
| 5 | Sensor-guards | 20 min |
| 6 | Modus, checklist en vlucht | 15 min |
| 7 | Testgevallen en fouten inbouwen | 55 min |
| 8 | Echte drone controleren, reflectie, opleveren | 50 min |

Mogelijke problemen: een sensor kan `None` teruggeven, wifi kan als tekst terugkomen, of een echte verbinding kan wegvallen. Ik test daarom eerst zonder drone en vang mislukte metingen af. De bibliotheek is `djitellopy`, met `Tello`, `connect`, `get_battery`, `get_height`, `get_temperature`, `query_wifi_signal_noise_ratio`, `get_flight_time`, `takeoff`, `move_forward`, `land` en `end`.

## Ontwerptabel
| # | Check | Meting/invoer | Constante(n) | Foutconditie | Melding |
|---|---|---|---|---|---|
| 1 | Naam | `name` | Niet-leeg | `not name` | Naam is leeg |
| 2 | Geheel getal | `distance_text` | `MIN_DISTANCE`, `MAX_DISTANCE` | `not distance_text.isdigit()` | Geen geldig geheel getal |
| 3 | Afstand geldig | `distance` | `MIN_DISTANCE`, `MAX_DISTANCE` | `not MIN_DISTANCE <= distance <= MAX_DISTANCE` | Afstand buiten bereik |
| 4 | Bevestiging | `confirmation` | `CONFIRM_WORD` | `confirmation != CONFIRM_WORD` | Bevestiging ongeldig |
| 5 | Sensors gelezen | alle vijf | `None` | één waarde `is None` | Meting mislukt |
| 6 | Batterij | `battery` | `MIN_BATTERY` | `battery <= MIN_BATTERY` | Batterij te laag |
| 7 | Hoogte | `height` | `MAX_HEIGHT` | `height > MAX_HEIGHT` | Niet op de grond |
| 8 | Temperatuur | `temperature` | `MAX_TEMP` | `temperature >= MAX_TEMP` | Te heet |
| 9 | Wifi | `wifi` | `MIN_WIFI` | `wifi < MIN_WIFI` | Wifi te zwak |
| 10 | Vliegtijd | `flight_time` | `MAX_FLIGHT_TIME` | `flight_time > MAX_FLIGHT_TIME` | Te lang gevlogen |
| 11 | Warm en bijna leeg | `temperature`, `battery` | `WARM_TEMP`, `LOW_BATTERY` | `temperature >= WARM_TEMP and battery <= LOW_BATTERY` | Warm en bijna leeg |
| 12 | Modusafstand | `distance`, `max_mode_distance` | `ECO_DISTANCE`, `NORMAL_DISTANCE`, `FULL_DISTANCE` | `distance > max_mode_distance` | Afstand te groot |

## Ontwerpvragen
1. `None` kun je niet met een getal vergelijken. De metingscheck voorkomt een `TypeError` bij de batterijcheck.
2. De maximale afstand hangt af van de gekozen modus. Die moet dus eerst bekend zijn.
3. Ongeldige invoer kan direct geweigerd worden, zonder onnodig verbinding met de drone te maken.
4. Eerst de losse temperatuurcheck en daarna de gecombineerde check. Vanaf 60 C stopt hij meteen; tussen 45 en 59 C kan de combinatie nog stoppen.

## Simulatiekeuze
`tello` begint als `None`. Er wordt pas een drone-object aangemaakt wanneer `SIMULATION` uit staat. Iedere guard roept dezelfde `close_connection()` aan, die alleen bij een bestaande drone `end()` uitvoert. Zo blijven de guards plat.

## Reflectie (na echte uitvoering bijwerken)
1. In de voorgestelde code is geen grens bijgesteld na testen. Een grensfout zou zichtbaar worden door een test precies op de grens (bijvoorbeeld 20% batterij).
2. Met twaalf geneste checks zou de code telkens verder naar rechts gaan en moeilijk leesbaar worden.
3. Een nieuwe regel vraagt een constante, 1 extra guard, een checklistregel en bijbehorende tests. De bestaande guards hoeven niet opnieuw ingesprongen te worden.
