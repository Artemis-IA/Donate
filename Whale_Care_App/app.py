from flask import Flask, render_template, request
from models.data import Data
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def fill_form():
    return render_template('form.html')

@app.route('/greeting', methods=['POST'])
def form_collect():
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        adresse = request.form.get('adresse')
        code_postal = request.form.get('code_postal')
        ville = request.form.get('ville')
        email = request.form.get('email')
        somme_recoltee = request.form.get('somme_recoltee')

        # Géocodage de la ville saisie par l'utilisateur
        geocoded_data = geocode_city(ville)
        latitude = geocoded_data['lat'] if geocoded_data else None
        longitude = geocoded_data['lon'] if geocoded_data else None

        data = Data()
        try:
            donator = data.set_form(nom, prenom, adresse, code_postal, ville, email, somme_recoltee, latitude, longitude)
            return render_template('greeting.html', donator=donator)
        except ValueError as e:
            return render_template('form.html', error_message=str(e))
    else:
        return render_template('index.html')  # Rediriger vers la page d'accueil en cas de requête non autorisée
    
@app.route('/thank_you/<int:donator_id>')
def thank_you(donator_id):
    # Récupérer les détails du donateur depuis la base de données
    data = Data()
    donator = data.get_donator_by_id(donator_id)
    if donator:
        return render_template('thank_you.html', donator=donator)
    else:
        # Gérer le cas où le donateur n'a pas été trouvé dans la base de données
        return render_template('error_page.html', error_message="Donateur non trouvé.")

# Fonction pour géocoder la ville en utilisant l'API Nominatim
def geocode_city(city):
    base_url = 'https://nominatim.openstreetmap.org/search'
    params = {'q': city, 'format': 'json', 'limit': 1}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]
    return None

@app.route('/view')
def view_collect():
    data = Data()
    donators = data.get_donators()
    total_sum = data.get_total_sum()

    return render_template('view.html', donators=donators, total_sum=total_sum)

@app.route('/conditions_generales')
def conditions_generales():
    return render_template('conditions_generales.html')

if __name__ == "__main__":
    app.run(debug=True)
