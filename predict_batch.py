# Script batch per generare predizioni su più ticket
# Importo le librerie che utilizzeremo
import pandas as pd
import joblib

# Carico modello e vettorizzatore
model = joblib.load("model/modello_ticket.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Carico il dataset di input
# Può essere lo stesso synthetic_tickets.csv o un altro file
df = pd.read_csv("data/synthetic_tickets.csv", encoding="utf-8")

# Creo una colonna testo combinando titolo e descrizione
df["testo"] = df["titolo"] + ". " + df["descrizione"]

# Trasformo i testi in vettori numerici
X_vec = vectorizer.transform(df["testo"])

# Prevedo la categoria
df["categoria_prevista"] = model.predict(X_vec)

# Stimo la priorità in base a parole chiave
def stima_priorita(testo):
    testo = testo.lower()
    if any(word in testo for word in ["errore", "problema", "blocco", "non funziona", "guasto"]):
        return "Alta"
    elif any(word in testo for word in ["richiesta", "informazione", "supporto"]):
        return "Media"
    else:
        return "Bassa"

df["priorita_stimata"] = df["testo"].apply(stima_priorita)

# Salvo il file con le predizioni
output_path = "data/predizioni_ticket.csv"
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"File salvato con successo: {output_path}")
