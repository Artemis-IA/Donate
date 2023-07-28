#data.py
import re
from models.connexion import Connexion


class Data: 

    @staticmethod
    def is_valid_text(input_text):
        pattern = b"^[A-Za-z ]+$"  # Encode the pattern to bytes
        return re.match(pattern, input_text)
    
    @staticmethod
    def set_form(nom, prenom, adresse, code_postal, ville, email, somme_recoltee, latitude, longitude):
        cursor = Connexion.connexion()

        request = "INSERT INTO donateurs(nom, prenom, adresse, code_postal, ville, email, somme_recoltee, latitude, longitude) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, adresse, code_postal, ville, email, somme_recoltee, latitude, longitude)

        cursor.execute(request, values)
        Connexion.deconnexion()

    @staticmethod
    def get_donators():
        cursor =  Connexion.connexion()
        query = "SELECT * FROM donateurs"
        cursor.execute(query)
        results = cursor.fetchall()
        donators = []
        for enregistrement in results:
            liste = []
            liste.append(enregistrement[1]) #nom
            liste.append(enregistrement[2]) #prenom
            liste.append(enregistrement[3]) #adresse
            liste.append(enregistrement[4]) #code_postal
            liste.append(enregistrement[5]) #ville
            liste.append(enregistrement[6]) #email
            liste.append(enregistrement[7]) #somme_recoltee
            donators.append(liste)
        Connexion.deconnexion()
        return donators

    @staticmethod
    def get_total_sum():
        cursor = Connexion.connexion()

        request = "SELECT SUM(somme_recoltee) FROM donateurs"
        cursor.execute(request)

        total_sum = cursor.fetchone()[0]
        Connexion.deconnexion()

        return total_sum




    # @staticmethod
    # def get_top_10_cities():
    #     cursor = Connexion.connexion()

    #     request = """
    #         SELECT ville, SUM(somme_recoltee) as total_donation, latitude, longitude
    #         FROM donateurs
    #         GROUP BY ville, latitude, longitude
    #         ORDER BY total_donation DESC
    #         LIMIT 10
    #     """
    #     cursor.execute(request)

    #     top_10_cities = []
    #     for row in cursor:
    #         city_data = {
    #             'city': row[0],
    #             'total_donation': row[1],
    #             'latitude': float(row[2]),
    #             'longitude': float(row[3]),
    #         }
    #         top_10_cities.append(city_data)

    