import streamlit as st
from datetime import datetime
import pickle
import Preisberechnung

# Titel für die Webanwendung
st.title("Immobilien-Daten-Erfassung")

# Sammeln der Eingaben mit den interaktiven Widgets von Streamlit
grundstuecksflaeche = st.number_input(
    "Bitte geben Sie die Grundstücksfläche in Quadratmetern ein:", 
    min_value=0, step=1, format='%d'
)
wohnflaeche = st.number_input(
    "Bitte geben Sie die Wohnfläche in Quadratmetern ein:", 
    min_value=0, step=1, format='%d'
)

bundesland_options = [
    "Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Bremen", 
    "Hamburg", "Hessen", "Mecklenburg-Vorpommern", "Niedersachsen", 
    "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland", "Sachsen", 
    "Sachsen-Anhalt", "Schleswig-Holstein", "Thüringen"
]
bundesland = st.selectbox(
    "In welchem Bundesland steht das Haus?", 
    bundesland_options
)

lage = st.radio(
    "Ist das Haus in der Stadt oder auf dem Land?", 
    ("Stadt", "Land")
)

hausart_options = ["Einfamilienhaus", "Doppelhaushälfte", "Mehrfamilienhaus"]
hausart = st.radio("Was für eine Art Haus ist es?", hausart_options)

ausstattung_options = [
    "Rohbau", "Sanierungsbedarf", "Renovierungsbedarf", "Einfach", "Gehoben"
]
ausstattung = st.selectbox("Wie ist die Ausstattung?", ausstattung_options)

architektenhaus = st.radio("Ist es ein Architektenhaus?", ["Ja", "Nein"]).lower()
makler = st.radio("Soll ein Makler das Haus verkaufen?", ["Ja", "Nein"]).lower()
denkmalschutz = st.radio(
    "Steht das Haus oder Teile davon unter Denkmalschutz?", 
    ["Ja", "Nein"]
).lower()

baujahr = st.number_input(
    "In welchem Jahr wurde das Haus erbaut?", 
    min_value=1800, max_value=datetime.now().year, format='%d'
)

if st.button("Daten speichern"):
    ur_variablen = [
        grundstuecksflaeche, wohnflaeche, architektenhaus, makler, 
        denkmalschutz, baujahr, lage, ausstattung, hausart, bundesland
    ]
    
    immobilienpreis = Preisberechnung.preis_rechner(*ur_variablen)
    dateiname = datetime.now().strftime("%Y%m%d_%H%M%S") + "_ur_variablen.pickle"

    try:
        with open(dateiname, "wb") as datei:
            pickle.dump(ur_variablen, datei)
        st.success("Daten erfolgreich gespeichert!")
    except Exception as e:
        st.error(f"Fehler beim Speichern der Daten: {e}")

    st.title("Ihr Immobilienpreis")

    st.text(
        f"Ihre Immobilie hat folgende Daten:\n"
        f"Grundstücksfläche:  {grundstuecksflaeche}\n"
        f"Wohnfläche:         {wohnflaeche}\n"
        f"Bundesland:         {bundesland}\n"
        f"Lage:               {lage}\n"
        f"Hausart:            {hausart}\n"
        f"Ausstattung:        {ausstattung}\n"
        f"Architektenhaus:    {architektenhaus}\n"
        f"Makler:             {makler}\n"
        f"Denkmalschutz:      {denkmalschutz}\n"
        f"Baujahr:            {baujahr}"
    )
    
    st.info(f"Der geschätzte Immobilienpreis beträgt: {immobilienpreis:.2f} Euro")

    # Ausführen des Skripts mit `streamlit run "Pfad"` in Kommandozeile (Miniconda)