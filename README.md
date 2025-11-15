# Ticket Triage – Classificazione Automatica dei Ticket Aziendali

Questo progetto implementa un prototipo di sistema di **triage automatico dei ticket aziendali** basato su tecniche di *Machine Learning* e *Natural Language Processing (NLP)*.  
L’obiettivo è classificare automaticamente i ticket in base al loro contenuto testuale, assegnando:

- **Categoria**: Amministrativa, Tecnica, Commerciale  
- **Priorità stimata**: Bassa, Media, Alta  

Il sistema è pensato come supporto agli operatori che gestiscono richieste interne o segnalazioni clienti, riducendo i tempi di smistamento e aumentando la coerenza nelle decisioni.

---

## Funzionalità principali

### Generazione del dataset sintetico
Non essendo disponibili ticket reali, il dataset viene generato in modo artificiale tramite lo script:



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

