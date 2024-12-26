import os
import requests
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de la URL de la API de Amadeus
BASE_URL = "https://test.api.amadeus.com/v2"

# Función para obtener un token de acceso
def get_access_token():
    auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("AMADEUS_API_KEY"),
        "client_secret": os.getenv("AMADEUS_API_SECRET")
    }
    try:
        response = requests.post(auth_url, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()["access_token"]
    except requests.exceptions.RequestException as e:
        print(f"Error getting access token: {str(e)}")
        print(f"Response content: {response.text}")
        raise Exception("Error al autenticar con la API de Amadeus") from e

# Función para consultar vuelos
def search_flights(origin, destination, departure_date, return_date=None):
    try:
        # Convert airport codes to uppercase
        origin = origin.upper()
        destination = destination.upper()
        
        access_token = get_access_token()
        search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "adults": 1,
            "max": 5
        }
        
        # Add return date for round-trip flights
        if return_date:
            params["returnDate"] = return_date
            params["nonStop"] = "false"  # Allow connections for better results
        
        print(f"Searching flights with params: {params}")  # Debug log
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error searching flights: {str(e)}")
        if 'response' in locals():
            print(f"Response content: {response.text}")
        raise

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search_flights', methods=['POST'])
def search():
    try:
        origin = request.form.get('origin', '').strip()
        destination = request.form.get('destination', '').strip()
        departure_date = request.form.get('departure_date', '').strip()
        return_date = request.form.get('return_date', '').strip()

        # Validaciones
        if not origin or not destination:
            return jsonify({"error": "El origen y destino son requeridos"}), 400
        if not departure_date:
            return jsonify({"error": "La fecha de salida es requerida"}), 400
        if len(origin) != 3 or len(destination) != 3:
            return jsonify({"error": "Los códigos de aeropuerto deben tener 3 letras"}), 400
        if origin == destination:
            return jsonify({"error": "El origen y destino no pueden ser iguales"}), 400

        results = search_flights(origin, destination, departure_date, return_date)
        return jsonify(results)
    except Exception as e:
        print(f"Error in search endpoint: {str(e)}")
        return jsonify({"error": "Error al buscar vuelos. Por favor, verifica los datos e intenta nuevamente."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5005)
