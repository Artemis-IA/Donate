# data_manager.py
import re
from .data import Data

class DataManager:
    def __init__(self):
        self.data = Data()

    def handle_form_data(self, form_data):
        nom = form_data.get('nom')
        prenom = form_data.get('prenom')
        adresse = form_data.get('adresse')
        code_postal = form_data.get('code_postal')
        ville = form_data.get('ville')
        email = form_data.get('email')
        somme_recoltee = form_data.get('somme_recoltee')

        # Géocodage de la ville saisie par l'utilisateur
        latitude, longitude = self.geocode_city(ville)

        donator = self.data.set_form(nom, prenom, adresse, code_postal, ville, email, somme_recoltee, latitude, longitude)
        return donator

    def get_donators_and_total_sum(self):
        donators = self.data.get_donators()
        total_sum = self.data.get_total_sum()
        return donators, total_sum

    def get_donator_by_id(self, donator_id):
        return self.data.get_donator_by_id(donator_id)

    # Fonction pour géocoder la ville en utilisant l'API Nominatim
    def geocode_city(self, city):
        # Your geocoding logic using the Nominatim API here
        return None, None
