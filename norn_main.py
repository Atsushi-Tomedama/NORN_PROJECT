# ==============================================================================
# PROGETTO NORN: NEURAL ONCOLOGY RISK NETWORK
# Autore: Dany Marcel Toukam Megaptche
# Tesi di Laurea in Medicina e Chirurgia - Università di Bologna
# ==============================================================================

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Imports bibliothèques spécifiques
try:
    import torchtuples as tt
    from pycox.models import CoxPH
    from pycox.evaluation import EvalSurv
except ImportError:
    print("❌ Errore: Librerie mancanti. Esegui: pip install -r requirements.txt")
    sys.exit(1)

# Configurazione Hardware
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"🚀 NORN SYSTEM STARTUP | DEVICE: {device}")

# ------------------------------------------------------------------------------
# 1. GENERATORE DATI SINTETICI (Per Demo Pubblica)
# ------------------------------------------------------------------------------
def generate_synthetic_data(n_samples=1000):
    """Genera dati finti se il dataset reale MSK-CHORD non è presente."""
    print("\n⚠️  ATTENZIONE: Dataset MSK-CHORD non trovato.")
    print("⚙️  Avvio generazione dati SINTETICI per dimostrazione...")
    
    np.random.seed(42)
    data = {
        'TMB_NONSYNONYMOUS': np.random.lognormal(mean=2, sigma=1, size=n_samples),
        'SAMPLE_TYPE': np.random.choice(['Primary', 'Metastasis'], n_samples),
        'GENDER': np.random.choice(['Male', 'Female'], n_samples),
        'CANCER_TYPE': np.random.choice(['Lung', 'Melanoma', 'Breast', 'Colorectal', 'Other'], n_samples),
        'OS_MONTHS': np.random.exponential(scale=24, size=n_samples), # Sopravvivenza simulata
        'Event': np.random.choice([0, 1], n_samples, p=[0.3, 0.7]) # 0=Vivo, 1=Deceduto
    }
    
    df = pd.DataFrame(data)
    # Creiamo OS_STATUS solo per compatibilità col formato originale
    df['OS_STATUS'] = df['Event'].apply(lambda x: '1:DECEASED' if x==1 else '0:LIVING')
    
    print(f"✅ Dati sintetici generati: {n_samples} pazienti simulati.\n")
    return df

# ------------------------------------------------------------------------------
# 2. DATA LOADING
# ------------------------------------------------------------------------------
def load_data(patient_file, sample_file):
    # Se i file non esistono, usa il generatore sintetico
    if not os.path.exists(patient_file) or not os.path.exists(sample_file):
        return generate_synthetic_data()

    print("📥 Caricamento Dataset Reale MSK-CHORD...")
    df_pat = pd.read_csv(patient_file, sep='\t', comment='#', low_memory=False)
    df_sam = pd.read_csv(sample_file, sep='\t', comment='#', low_memory=False)
    df = pd.merge(df_pat, df_sam, on='PATIENT_ID')
    
    # Preprocessing
    features = ['TMB_NONSYNONYMOUS', 'SAMPLE_TYPE', 'GENDER', 'CANCER_TYPE']
    df_clean = df.dropna(subset=features + ['OS_MONTHS', 'OS_STATUS']).copy()
    
    # Target Transformation
    df_clean['Event'] = df_clean['OS_STATUS'].str.contains("DECEASED|1").astype(int)
    
    # Group rare cancers
    top_cancers = df_clean['CANCER_TYPE'].value_counts().nlargest(15).index
    df_clean.loc[~df_clean['CANCER_TYPE'].isin(top_cancers), 'CANCER_TYPE'] = 'Other'
    
    return df_clean

# ------------------------------------------------------------------------------
# 3. NORN MODEL ARCHITECTURE
# ------------------------------------------------------------------------------
class NORN_Net(nn.Module):
    def __init__(self, in_features):
        super(NORN_Net, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(in_features, 64), nn.SELU(), nn.BatchNorm1d(64), nn.Dropout(0.3),
            nn.Linear(64, 32), nn.SELU(), nn.BatchNorm1d(32), nn.Dropout(0.3),
            nn.Linear(32, 16), nn.SELU(),
            nn.Linear(16, 1)
        )

    def forward(self, input):
        return self.net(input)

# ------------------------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Nomi file attesi
    PATIENT_FILE = 'data_clinical_patient.txt'
    SAMPLE_FILE = 'data_clinical_sample.txt'

    # Caricamento (o generazione)
    df = load_data(PATIENT_FILE, SAMPLE_FILE)
    
    # Feature Engineering
    print("🛠  Preprocessing e Feature Engineering...")
    ct = ColumnTransformer([
        ('num', StandardScaler(), ['TMB_NONSYNONYMOUS']),
        ('cat', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), ['SAMPLE_TYPE', 'GENDER', 'CANCER_TYPE'])
    ])
    
    X_cols = ['TMB_NONSYNONYMOUS', 'SAMPLE_TYPE', 'GENDER', 'CANCER_TYPE']
    
    # Assicuriamo che le colonne esistano (in caso di dati sintetici)
    df = df[df['OS_MONTHS'] > 0] # Rimuove tempi negativi o zero
    
    get_target = lambda df: (df['OS_MONTHS'].values.astype('float32'), df['Event'].values.astype('float32'))
    
    df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)
    X_train = ct.fit_transform(df_train[X_cols]).astype('float32')
    y_train = get_target(df_train)
    
    # Model Init
    input_nodes = X_train.shape[1]
    net = NORN_Net(input_nodes).to(device)
    model = CoxPH(net, tt.optim.Adam(lr=0.001))
    
    # Training
    print(f"🧠 Avvio Training NORN su {len(df_train)} pazienti...")
    model.fit(X_train, y_train, batch_size=256, epochs=50, verbose=True)
    
    print("\n✅ SUCCESS: Modello addestrato e pronto.")
    print("   (Nota: Se hai usato dati sintetici, le curve di sopravvivenza sono simulate)")
