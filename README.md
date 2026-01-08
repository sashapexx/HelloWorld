# Hello World Project

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
