# validators.py
import re
from .connexion import Connexion
class Validators:
    @staticmethod
    def is_valid_text(input_text):
        pattern = r"^[A-Za-z ]+$"
        return re.match(pattern, input_text)

    def validate_form_data(self, form_data):
        nom = form_data.get('nom')
        prenom = form_data.get('prenom')
        adresse = form_data.get('adresse')
        code_postal = form_data.get('code_postal')
        ville = form_data.get('ville')
        email = form_data.get('email')
        somme_recoltee = form_data.get('somme_recoltee')

        if not all([nom, prenom, adresse, code_postal, ville, email, somme_recoltee]):
            return False

        if not self.is_valid_text(nom) or not self.is_valid_text(prenom) or not self.is_valid_text(ville):
            return False

        return True
