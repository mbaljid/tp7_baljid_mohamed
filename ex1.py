# ex1.py
from datetime import datetime

# --- MIXINS ---

class Horodatable:
    """Mixin fournissant une fonctionnalité d'horodatage."""
    def horodatage(self):
        print(f"[LOG] Action à {datetime.now()}")

class Validable:
    """Mixin fournissant une validation de base pour les entités."""
    def valider(self):
        # Vérifie si l'attribut 'titre' existe et n'est pas vide
        if not getattr(self, "titre", None):
            raise ValueError("Erreur : Titre manquant")
        print("Validation OK")

# --- CLASSE PRINCIPALE ---

class Document(Horodatable, Validable):
    """
    Classe métier enrichie par les Mixins Horodatable et Validable.
    L'héritage multiple ici permet d'injecter des comportements transversaux.
    """
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu

    def sauvegarder(self):
        # Utilisation des méthodes injectées par les Mixins
        self.horodatage()
        self.valider()
        print(f"Document '{self.titre}' sauvegardé.")

# --- EXEMPLE D'UTILISATION ---

if __name__ == "__main__":
    try:
        # Création d'une instance de Document
        doc = Document("Rapport", "Contenu important")
        
        # Appel de la méthode qui déclenche les comportements des Mixins
        doc.sauvegarder()
        
    except ValueError as e:
        print(f"Erreur de validation : {e}")