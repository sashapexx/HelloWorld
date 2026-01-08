import os

# Dossiers
os.makedirs("src", exist_ok=True)
os.makedirs("tests", exist_ok=True)
os.makedirs(".github/workflows", exist_ok=True)

# Contenu des fichiers
files = {
    "README.md": """# Hello World Project

![Python](https://img.shields.io/badge/python-3.11-blue)
![Tests](https://github.com/sashapexx/helloworld/actions/workflows/python-app.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/sashapexx/helloworld)

**Auteur** : Sasha  
**Date** : 2026-01-08  

## Description
Ce projet est une démonstration structurée d'un programme Hello World en Python, conçu pour GitHub.  
Il montre comment créer :
- Une fonction réutilisable (hello_world)
- Un code testable avec des tests unitaires
- Une structure de projet professionnelle avec src/ et tests/

## Structure du projet

hello_world_project/
│
├── README.md
├── requirements.txt
├── src/
│   └── main.py
└── tests/
    └── test_main.py

## Installation

git clone https://github.com/sashapexx/helloworld.git
cd helloworld
pip install -r requirements.txt

## Utilisation

python src/main.py

Entrez votre nom : Alice
Hello Alice!

## Tests

python -m unittest discover tests

## Objectifs pédagogiques

- Apprendre à structurer un projet Python
- Comprendre l’importance des tests unitaires
- Préparer un projet prêt à être partagé sur GitHub
""",

    "requirements.txt": """# requirements.txt
# Aucune dépendance externe pour le moment
""",

    "src/main.py": """\"\"\"
hello_world_project
Auteur : Sasha
Date : 2026-01-08
Description : Programme Hello World structuré pour GitHub.
\"\"\"

def hello_world(name: str = "World") -> str:
    return f"Hello {name}!"

if __name__ == "__main__":
    user_name = input("Entrez votre nom : ")
    print(hello_world(user_name))
""",

    "tests/test_main.py": """import unittest
from src.main import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_default(self):
        self.assertEqual(hello_world(), "Hello World!")

    def test_custom_name(self):
        self.assertEqual(hello_world("Alice"), "Hello Alice!")

if __name__ == "__main__":
    unittest.main()
""",

    ".github/workflows/python-app.yml": """name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Run tests
      run: python -m unittest discover tests
"""
}

# Création des fichiers
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Tous les fichiers ont été créés avec succès !")
