# ex2.py corrigé
import json
from datetime import datetime

# --- MIXINS ---

class Serializable:
    def to_json(self):
        # On crée une copie pour ne pas modifier l'objet original
        donnees = self.__dict__.copy()
        # On retire l'historique de la sérialisation JSON pour éviter la boucle
        if "historique" in donnees:
            del donnees["historique"]
        return json.dumps(donnees, indent=4, default=str)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        # On capture l'état actuel en excluant l'historique lui-même
        etat_actuel = self.__dict__.copy()
        if "historique" in etat_actuel:
            del etat_actuel["historique"]
            
        self.historique.append({
            "date": datetime.now(),
            "etat": etat_actuel
        })
        print("[Système] État enregistré (hors historique).")

class Journalisable:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")

# --- CLASSE MÉTIER ---

class Contrat(Serializable, Historisable, Journalisable):
    def __init__(self, id, description):
        Historisable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat() 
        self.description = nouvelle_desc
        print(f"Contrat {self.id} mis à jour.")

# --- DÉMONSTRATION ---

if __name__ == "__main__":
    c = Contrat(1, "Initial")
    c.modifier("Révisé")
    
    print("-" * 30)
    print("Représentation JSON (propre) :")
    print(c.to_json())