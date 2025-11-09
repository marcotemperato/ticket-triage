# Dashboard Streamlit, Classificazione Ticket Aziendali
# Importo le librerie che utilizzeremo per la creazione della Dashboard
import streamlit as st
import pandas as pd
import joblib

# Carico il modello e il vettorizzatore salvati
model = joblib.load("model/modello_ticket.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Imposto il titolo e la descrizione della pagina
st.set_page_config(page_title="Classificazione Ticket Aziendali", layout="centered")
st.title("Classificazione Ticket Aziendali")
st.write("Inserisci i dettagli di un ticket per prevederne la categoria e la priorità.")

# Creo i campi di input
titolo = st.text_input("Titolo del ticket")
descrizione = st.text_area("Descrizione del ticket")

# Quando l’utente preme il pulsante, elaboro il testo
if st.button("Classifica ticket"):
    if titolo.strip() == "" or descrizione.strip() == "":
        st.warning("Inserisci sia il titolo che la descrizione.")
    else:
        # Combino titolo e descrizione
        testo = titolo + ". " + descrizione
        testo_vec = vectorizer.transform([testo])

        # Predizione della categoria
        categoria_pred = model.predict(testo_vec)[0]

        # Stima della priorità (semplice logica simulata)
        if "errore" in testo.lower() or "problema" in testo.lower():
            priorita = "Alta"
        elif "richiesta" in testo.lower() or "info" in testo.lower():
            priorita = "Media"
        else:
            priorita = "Bassa"

        # Mostro i risultati
        st.success(f"**Categoria prevista:** {categoria_pred}")
        st.info(f"**Priorità stimata:** {priorita}")
