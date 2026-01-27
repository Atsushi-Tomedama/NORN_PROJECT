# Commandes Git pour lier le projet NORN à un dépôt distant

## Configuration du dépôt distant

### Option 1: Créer et lier un nouveau dépôt GitHub nommé NORN-Thesis

```bash
# 1. Créer le dépôt distant sur GitHub
# Allez sur https://github.com/new et créez un nouveau dépôt nommé "NORN-Thesis"
# NE PAS initialiser avec README, .gitignore ou LICENSE (votre projet local existe déjà)

# 2. Lier votre dépôt local au dépôt distant
# Remplacez <VOTRE_USERNAME> par votre nom d'utilisateur GitHub
git remote add origin https://github.com/<VOTRE_USERNAME>/NORN-Thesis.git

# OU si vous utilisez SSH:
git remote add origin git@github.com:<VOTRE_USERNAME>/NORN-Thesis.git

# 3. Vérifier que le remote est bien ajouté
git remote -v

# 4. Pousser votre code vers le dépôt distant
git branch -M main  # S'assurer que la branche principale s'appelle 'main'
git push -u origin main
```

### Option 2: Si le dépôt distant existe déjà

```bash
# Lier le dépôt local au dépôt distant existant
# Remplacez <VOTRE_USERNAME> par votre nom d'utilisateur GitHub
git remote add norn-thesis https://github.com/<VOTRE_USERNAME>/NORN-Thesis.git

# Vérifier la configuration
git remote -v

# Pousser vers le nouveau remote
git push -u norn-thesis main
```

## Commandes utiles après la configuration

```bash
# Pousser vos modifications futures
git add .
git commit -m "Description de vos modifications"
git push origin main

# Vérifier le statut des fichiers (s'assurer qu'aucun CSV n'est en attente)
git status

# Voir les fichiers ignorés par .gitignore
git status --ignored

# Vérifier qu'aucun fichier CSV n'est tracké
git ls-files | grep -i "\.csv$"
```

## ⚠️ IMPORTANT - Sécurité des données patients

### Vérification avant le premier push

Avant de pousser votre code pour la première fois, vérifiez qu'aucun fichier CSV ou données sensibles n'est présent:

```bash
# Lister tous les fichiers qui seront poussés
git ls-files

# Vérifier spécifiquement les CSV (la commande ne doit rien retourner)
git ls-files | grep -i "\.csv$"

# Vérifier les fichiers Excel (la commande ne doit rien retourner)
git ls-files | grep -i "\.\(xls\|xlsx\)$"
```

### Si des fichiers sensibles ont été commités par erreur

Si des fichiers CSV ou données patients ont déjà été commités:

```bash
# Option 1: Supprimer le fichier de l'historique Git (AVANT le push)
git rm --cached fichier_sensible.csv
git commit -m "Suppression fichier sensible du tracking Git"

# Option 2: Si déjà poussé - Utiliser BFG Repo-Cleaner ou git-filter-branch
# ⚠️ Cette opération réécrit l'historique et est complexe
# Consultez: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
```

## Configuration recommandée du dépôt distant

Pour un projet de thèse médicale, il est recommandé de:

1. **Rendre le dépôt PRIVÉ** (Private Repository)
2. Activer la **protection de branche** pour la branche `main`
3. Configurer les **GitHub Secrets** pour toute clé API ou credentials
4. Ajouter un fichier `README.md` détaillé sans données sensibles
5. Ajouter une **LICENCE** appropriée (souvent non applicable pour les thèses)

## Commandes de vérification de sécurité

```bash
# Vérifier la configuration du remote
git remote show origin

# S'assurer que le .gitignore fonctionne correctement
# (créer un fichier test.csv temporaire)
touch test_patient_data.csv
git status  # Le fichier ne doit PAS apparaître dans les untracked files
rm test_patient_data.csv

# Vérifier tous les fichiers ignorés
git check-ignore -v **/*
```

## Notes importantes

- ✅ Le fichier `.gitignore` est configuré pour bloquer **tous** les fichiers CSV
- ✅ Les dossiers `data/`, `patients/`, `donnees/` sont automatiquement ignorés
- ✅ Les fichiers Excel, bases de données, et pickles sont également bloqués
- ⚠️ **TOUJOURS** vérifier avec `git status` avant de faire un `commit`
- ⚠️ Ne **JAMAIS** utiliser `git add -f` (force) pour les fichiers de données
- 🔒 Gardez votre dépôt **PRIVÉ** pour protéger les données médicales

## Contact et support

Pour toute question sur la configuration Git ou la sécurité des données:
- Documentation Git: https://git-scm.com/doc
- Guide GitHub sur la sécurité: https://docs.github.com/en/code-security
- RGPD et gestion des données: https://www.cnil.fr/
