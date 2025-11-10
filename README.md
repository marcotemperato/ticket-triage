# Ticket-Triage Project Work - Marco Temperato

**Titolo:** Sviluppo di un modello di Machine Learning per la gestione dei ticket aziendali  
**Autore:** Marco Temperato (Matricola 0312301980)

## Descrizione
Prototipo per il triage automatico dei ticket aziendali: dataset sintetico, modello di classificazione, script batch per predizioni e dashboard interattiva (Streamlit).

## Contenuto del repository
- `data/`
  - `synthetic_tickets.csv` : dataset sintetico (300 ticket)
  - `predizioni_ticket.csv` : esempi di output batch
- `model/`
  - `modello_ticket.pkl` : modello addestrato
  - `vectorizer.pkl` : TF-IDF vectorizer
- `notebooks/`
  - `model_training.ipynb` : notebook di training e valutazione
- `dashboard/`
  - `app.py` : Streamlit app per test manuale dei ticket
- `data_gen.py` : script per generare il dataset sintetico
- `predict_batch.py` : script per predizioni in batch
- `README.md` : questo file

## Strumenti
Python 3.9+, pacchetti: pandas, scikit-learn, streamlit, joblib, matplotlib, nltk

## Come eseguire
1. Addestrare (opzionale): eseguire `notebooks/model_training.ipynb` in Colab/VSCode.
2. Eseguire batch: `python predict_batch.py` → genera `data/predizioni_ticket.csv`.
3. Eseguire dashboard: `streamlit run dashboard/app.py` → apre `http://localhost:8501`.

