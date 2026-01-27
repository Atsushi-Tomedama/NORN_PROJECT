# NORN PROJECT - Neural Oncology Risk Network

> 🏥 Projet de thèse de médecine sur l'Intelligence Artificielle en oncologie

## 🔒 Sécurité et Protection des Données

⚠️ **IMPORTANT**: Ce projet contient des outils pour l'analyse de données médicales. La protection des données patients est **PRIMORDIALE**.

### Protection des fichiers sensibles

Le fichier `.gitignore` est configuré pour bloquer **automatiquement**:
- ✅ **Fichiers CSV** (*.csv, *.CSV) - Données patients
- ✅ **Fichiers Excel** (*.xls, *.xlsx, *.xlsm, etc.)
- ✅ **Bases de données** (*.db, *.sqlite, *.sql)
- ✅ **Dossiers de données** (data/, patients/, donnees/, etc.)
- ✅ **Fichiers temporaires Python** (*.tmp, *.pyc, __pycache__, etc.)
- ✅ **Fichiers pickle** (*.pkl, *.pickle)

### Commandes de vérification

Avant chaque commit, vérifiez qu'aucune donnée sensible n'est trackée:

```bash
# Vérifier le statut (aucun CSV ne doit apparaître)
git status

# Rechercher spécifiquement les CSV trackés
git ls-files | grep -i "\.csv$"
```

## 📋 Configuration du dépôt distant

Pour lier ce projet à un nouveau dépôt GitHub nommé **NORN-Thesis**, consultez le fichier:
- [`GIT_SETUP_COMMANDS.md`](./GIT_SETUP_COMMANDS.md) - Guide complet des commandes Git

### Commandes rapides

```bash
# 1. Créer le dépôt sur GitHub: https://github.com/new
# 2. Lier au dépôt distant (remplacez <VOTRE_USERNAME> par votre nom d'utilisateur)
git remote add origin https://github.com/<VOTRE_USERNAME>/NORN-Thesis.git

# 3. Pousser le code
git branch -M main
git push -u origin main
```

## 🛡️ Conformité RGPD/HIPAA

Ce projet est configuré pour respecter:
- **RGPD** (Règlement Général sur la Protection des Données)
- **HIPAA** (Health Insurance Portability and Accountability Act)

**Ne jamais**:
- ❌ Committer des fichiers CSV contenant des données patients
- ❌ Utiliser `git add -f` pour forcer l'ajout de fichiers ignorés
- ❌ Pousser des données identifiables vers un dépôt public

## 📚 À propos du projet NORN

**NORN** - Neural Oncology Risk Network est un projet de recherche utilisant l'intelligence artificielle pour l'analyse des risques en oncologie.

---

Pour plus d'informations sur la configuration Git, consultez [`GIT_SETUP_COMMANDS.md`](./GIT_SETUP_COMMANDS.md)