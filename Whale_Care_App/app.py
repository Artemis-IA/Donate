# app.py
from flask import Flask, render_template, request
from models.data_manager import DataManager
from models.validators import Validators
app = Flask(__name__)

class AppController:
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/form')
    def fill_form():
        return render_template('form.html')

    @app.route('/greeting', methods=['POST'])
    def form_collect():
        if request.method == 'POST':
            form_data = request.form
            data_handler = DataManager()
            validators = Validators()
            try:
                if validators.validate_form_data(form_data):
                    donator = data_handler.handle_form_data(form_data)
                    return render_template('greeting.html', donator=donator)
                else:
                    raise ValueError("Les données du formulaire ne sont pas valides.")
            except ValueError as e:
                return render_template('form.html', error_message=str(e))
        else:
            return render_template('index.html')  # Rediriger vers la page d'accueil en cas de requête non autorisée

    @app.route('/thank_you/<int:donator_id>')
    def thank_you(donator_id):
        data_handler = DataManager()
        donator = data_handler.get_donator_by_id(donator_id)
        if donator:
            return render_template('thank_you.html', donator=donator)
        else:
            return render_template('error_page.html', error_message="Donateur non trouvé.")

    @app.route('/view')
    def view_collect():
        data_handler = DataManager()
        donators, total_sum = data_handler.get_donators_and_total_sum()

        return render_template('view.html', donators=donators, total_sum=total_sum)

    @app.route('/conditions_generales')
    def conditions_generales():
        return render_template('conditions_generales.html')


if __name__ == "__main__":
    app.run(debug=True)