# ex3_squelette.py
from datetime import datetime
import copy

# --- 1. LES MIXINS ---

class JournalisationMixin:
    """
    Responsabilité : Afficher des logs dans la console avec horodatage.
    """
    def journaliser(self, message):
        # TODO: Implémenter l'affichage du message avec datetime.now()
        # Format attendu : [LOG - {date}] : {message}
        pass

class ValidationMixin:
    """
    Responsabilité : Garantir l'intégrité des données (ici, le titre).
    """
    def valider_titre(self, titre):
        # TODO: Vérifier si le titre est None ou une chaîne vide ("")
        # Si c'est le cas, lever une ValueError("Le titre ne peut pas être vide")
        # Sinon, ne rien faire (validation réussie)
        pass

class HistoriqueMixin:
    """
    Responsabilité : Garder une trace des anciennes versions de la description.
    """
    def __init__(self):
        # TODO: Initialiser une liste vide pour l'historique
        self.historique = []

    def sauvegarder_ancienne_description(self, description_actuelle):
        # TODO: Ajouter un dictionnaire ou un tuple dans self.historique
        # Contenant : la date de l'archive et la valeur de la description AVANT modif
        pass

# --- 2. LA CLASSE PRINCIPALE ---

class Tâche(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    """
    Classe métier représentant une tâche professionnelle.
    """
    def __init__(self, titre, description):
        # TODO: Appeler le constructeur de HistoriqueMixin (important pour la liste !)
        
        # TODO: Utiliser valider_titre() pour vérifier le titre reçu
        
        # Initialisation des attributs
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()
        
        # TODO: Utiliser journaliser() pour annoncer la création de la tâche
        pass

    def mettre_a_jour(self, nouvelle_description):
        """
        Met à jour la description en archivant l'ancienne version.
        """
        # 1. Logger l'action de modification
        # 2. Sauvegarder l'ancienne description (via HistoriqueMixin)
        # 3. Mettre à jour self.description
        pass

    def afficher_historique(self):
        """
        Affiche toutes les anciennes versions stockées.
        """
        print(f"--- Historique de la tâche '{self.titre}' ---")
        # TODO: Parcourir self.historique et afficher chaque version
        pass

# --- 3. TESTS (SCÉNARIO) ---

if __name__ == "__main__":
    try:
        print("=== Test 1: Création et Modification ===")
        # 1. Créer une tâche "Rédiger rapport"
        t = Tâche("Rédiger rapport", "Brouillon initial")
        
        # 2. Faire une mise à jour
        t.mettre_a_jour("Version relue par le chef")
        
        # 3. Faire une deuxième mise à jour
        t.mettre_a_jour("Version finale validée")

        # 4. Afficher l'historique
        t.afficher_historique()

        print("\n=== Test 2: Validation ===")
        # TODO: Décommenter la ligne suivante pour tester la validation
        # t_erreur = Tâche("", "Ceci devrait échouer")

    except ValueError as e:
        print(f"Erreur attrapée : {e}")