# NORN: Neural Oncology Risk Network 

**A Deep Learning Framework for Pan-Cancer Survival Prediction using Genomic Data.**

## Overview
NORN is a Deep Cox Proportional Hazards model developed to predict patient survival based on **Tumor Mutational Burden (TMB)** and basic histological features. 
Developed as part of a Medical Thesis at the **University of Bologna**, this project demonstrates the "Strategic Blindness" approach: the model achieves significant risk stratification (C-Index: 0.67) and could be the face of early data-driven oncology medicine by exposing the non-linear interaction between tumor activity and intrinsic biological factors such as Histology (Cancer Type) and Sample Type.

## Key Features
* **Deep Cox Architecture:** Multi-layer perceptron tailored for survival analysis.
* **Stage-Agnostic:** Intentionally excludes clinical staging to isolate biological signals.
* **Stratified Validation:** Uses a rigorous 70/15/15 split strategy.
* **Explainable Metrics:** Includes C-Index, Brier Score, and Kaplan-Meier risk stratification.

  

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Atsushi-Tomedama/NORN_PROJECT.git
   cd NORN_PROJECT
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script to train the model and generate survival curves:
```bash
python src/norn_model.py
```
. Data Preparation

Due to privacy and licensing, the MSK-CHORD dataset cannot be hosted directly here.

Download **_data_clinical_patient.txt_** and **_data_clinical_sample.txt_** from cBioPortal or the supplementary material of the MSK-CHORD Nature 2024 paper.

Place them in the root directory.

Note: The repository includes a synthetic data generator for demonstration purposes. To reproduce thesis results, use the secured MSK-CHORD dataset (access under conditions).

## The "Doctor-in-the-Loop"
This project advocates for the "Doctor-in-the-Loop" paradigm. NORN is not a replacement for the clinician but a decision-support tool.

Input: Genomic Data (TMB) + Histology + Gender + Sample type. (HARD DATA)

Output: Risk Score & Survival Probability.

## Action: The physician integrates this biological risk score with clinical findings to personalize follow-up intensity and treatment strategies.

## Medical Disclaimer
This software is for research and educational purposes only. It is not a certified medical device (SaMD) and has not received FDA/CE clearance. It should not be used for clinical decision-making without clearance by the authorities nor authorised use by the author.

## Citation
If you find this work useful, please cite:

> **Dany Marcel Toukam Megaptche**, "INTELLIGENZA ARTIFICIALE IN MEDICINA: FORMAZIONE, APPLICAZIONE CLINICA E SVILUPPO DI UN MODELLO PREDITTIVO IA-BASED", MD Thesis, University of Bologna, 2026.

## License
Distributed under the MIT License. See LICENSE for more information.
