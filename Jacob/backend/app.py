from flask import Flask, jsonify, request
from flask_cors import CORS
from pokemons_data import POKEMONS_DB

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "Pokedex API"}), 200


@app.route('/api/pokemon/<string:nombre>', methods=['GET'])
def obtener_pokemon(nombre):
    pokemon = next((p for p in POKEMONS_DB if p["name"].lower() == nombre.lower()), None)
    if pokemon:
        return jsonify(pokemon), 200
    return jsonify({"error": "Pokemon no encontrado"}), 404


@app.route('/api/pokemon', methods=['GET'])
def listar_pokemon():
    return jsonify(POKEMONS_DB), 200


@app.route('/api/pokemon', methods=['POST'])
def crear_pokemon():
    datos = request.get_json()

    if not datos or "name" not in datos or "type" not in datos:
        return jsonify({"error": "Datos invalidos"}), 400

    nuevo_pokemon = {
        "id": len(POKEMONS_DB) + 1,
        "name": datos["name"],
        "type": datos["type"],
        "level": datos.get("level", 1),
        "hp": datos.get("hp", 50),
    }

    POKEMONS_DB.append(nuevo_pokemon)
    return jsonify(nuevo_pokemon), 201


if __name__ == '__main__':
    app.run(port=5000)
