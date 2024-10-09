"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import Person
from models import Mundos
from models import Favorite_People
from models import Favorite_Planet

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    results = [{
        'id': user.id,
        'username': user.username} for user in users]
    return jsonify(results), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites(user_id):
    user = User.query.get(user_id)
    if not usert:
        return jsonify({'msg': 'User not found'}), 404

@app.route('/people', methods=['GET'])
def get_people():
    people = Person.query.all()
    return jsonify(people), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def get_person_by_id(people_id):
    result = Person.query.get(people_id)
    if result is None:
        return jsonify({ "msg": f"People with id {people_id} not found" }), 404
    return jsonify(result), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Mundos.query.all()
    return jsonify(planets), 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planets_by_id(planets_id):
    result = Mundos.query.get(planets_id)
    if result is None:
        return jsonify({ "msg": f"People with id {planets_id} not found" }), 404
    return jsonify(result), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
