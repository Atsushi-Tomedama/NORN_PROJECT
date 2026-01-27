# NORN: Neural Oncology Risk Network 

**A Deep Learning Framework for Pan-Cancer Survival Prediction using Genomic Data.**

## Overview
NORN is a Deep Cox Proportional Hazards model developed to predict patient survival based on **Tumor Mutational Burden (TMB)** and basic histological features. 
Developed as part of a Medical Thesis at the **University of Bologna**, this project demonstrates the "Strategic Blindness" approach: the model achieves significant risk stratification (C-Index: 0.67) **without** using TNM staging data, highlighting the independent prognostic power of genomic instability.

## Key Features
* **Deep Cox Architecture:** Multi-layer perceptron tailored for survival analysis.
* **Stage-Agnostic:** Intentionally excludes clinical staging to isolate biological signals.
* **Stratified Validation:** Uses a rigorous 70/15/15 split strategy.
* **Explainable Metrics:** Includes C-Index, Brier Score, and Kaplan-Meier risk stratification.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/NORN-Thesis.git](https://github.com/YOUR_USERNAME/NORN-Thesis.git)
   cd NORN-Thesis5Y
