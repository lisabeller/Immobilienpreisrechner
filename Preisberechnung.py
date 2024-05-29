# Preisberechnung
import datetime

def preis_rechner(grundstuecksflaeche, wohnflaeche, architektenhaus, makler, denkmalschutz, baujahr, lage, ausstattung, hausart, bundesland):

    # 01 BASIS: Berechnung des Grundpreises
    immobilienpreis = (grundstuecksflaeche * 160) + (wohnflaeche * 2500)
    print(f"Grundpreis: {immobilienpreis:.2f}")

    # 02 BUNDESLAND: Faktor auf Grundpreis anwenden
    bundesland_faktoren = {
        "Baden-Württemberg": 1.5,
        "Bayern": 1.7,
        "Berlin": 2.1,
        "Brandenburg": 1.1,
        "Bremen": 1.2,
        "Hamburg": 2.5,
        "Hessen": 1.3,
        "Mecklenburg-Vorpommern": 0.9,
        "Niedersachsen": 1.0,
        "Nordrhein-Westfalen": 1.1,
        "Rheinland-Pfalz": 1.0,
        "Saarland": 0.7,
        "Sachsen": 0.7,
        "Sachsen-Anhalt": 0.6,
        "Schleswig-Holstein": 1.4,
        "Thüringen": 0.6
    }
    immobilienpreis *= bundesland_faktoren.get(bundesland, 1.0)

    # 03 LAGE: Aufschlag für städtische Lage
    if lage.lower() == "stadt":
        immobilienpreis *= 2.0

    # 04 HAUSART: Faktoren abhängig von der Hausart
    hausart_faktoren = {
        "Einfamilienhaus": 1.0,
        "Doppelhaushälfte": 0.8,
        "Mehrfamilienhaus": 0.7
    }
    immobilienpreis *= hausart_faktoren.get(hausart, 1.0)

    # 05 AUSSTATTUNG: Faktoren abhängig von der Ausstattung
    ausstattung_faktoren = {
        "Rohbau": 0.5,
        "Sanierungsbedarf": 0.8,
        "Renovierungsbedarf": 0.9,
        "Einfach": 1.0,
        "Gehoben": 2.0
    }
    immobilienpreis *= ausstattung_faktoren.get(ausstattung, 1.0)

    # 06 WEITERE FAKTOREN: Einfluss auf den Immobilienpreis
    if architektenhaus.lower() == "ja":
        immobilienpreis *= 1.2
    if makler.lower() == "ja":
        immobilienpreis *= 1.2
    if denkmalschutz.lower() == "ja":
        immobilienpreis *= 0.8
    if baujahr < 2024:
        immobilienpreis *= 1 - 0.001 * (datetime.datetime.now().year - baujahr)
    return immobilienpreis

