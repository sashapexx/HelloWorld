"""
hello_world_project
Auteur : Sasha
Date : 2026-01-08
Description : Programme Hello World structuré pour GitHub.
"""

def hello_world(name: str = "World") -> str:
    return f"Hello {name}!"

if __name__ == "__main__":
    user_name = input("Entrez votre nom : ")
    print(hello_world(user_name))
