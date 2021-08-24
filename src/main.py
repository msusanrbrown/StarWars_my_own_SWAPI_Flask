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
from models import db, User, People, Planet, Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
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
def handle_hello():
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }
    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def people():
    all_people=People.query.all()
    response_body = [x.serialize() for x in all_people]
    return jsonify(response_body), 200

@app.route('/people/<int:id>', methods=['GET'])
def people_by_id(id):
    people=People.query.filter(People.id==id).first_or_404(description=f'Record with id={id} is not available'.format(id))
    response_body = people.serialize()
    return jsonify(response_body), 200

@app.route('/people', methods=['POST'])
def people_edit():
    args = request.get_json(silent=True)
    people = People(name=args['name'], birth_year=args['birth_year'], eye_color=args['eye_color'],
            homeworld_id=args['homeworld_id'], gender=args['gender'], 
            hair_color=args['hair_color'], height=args['height'], mass=args['mass'], 
            skin_color=args['skin_color'], created=args['created'], edited=args['edited'])
    db.session.add(people)
    db.session.commit()
    return People.serialize(people), 201

@app.route('/people/<int:id>', methods=['DELETE'])
def delete_people_by_id(id):
    record = People.query.filter(People.id==id).first_or_404(description=f'Record with id={id} is not available'.format(id))
    db.session.delete(record)
    db.session.commit()
    return '', 204


@app.route('/planet', methods=['GET'])
def planet():
    all_planet=Planet.query.all()
    response_body = [x.serialize() for x in all_planet]
    return jsonify(response_body), 200

@app.route('/planet/<int:id>', methods=['GET'])
def planet_by_id(id):
    planet=Planet.query.filter(Planet.id==id).first_or_404(description=f'Record with id={id} is not available'.format(id))
    response_body = planet.serialize()
    return jsonify(response_body), 200

@app.route('/planet', methods=['POST'])
def planet_edit():
    args = request.get_json(silent=True)
    planet = Planet(name=args['name'], diameter=args['diameter'], rotation_period=args['rotation_period'],
            orbital_period=args['orbital_period'], gravity=args['gravity'], population=args['population'], 
            climate=args['climate'], terrain=args['terrain'], surface_water=args['surface_water'], 
            created=args['created'], edited=args['edited'])
    db.session.add(planet)
    db.session.commit()
    return Planet.serialize(planet), 201

@app.route('/planet/<int:id>', methods=['DELETE'])
def delete_planet_by_id(id):
    record = Planet.query.filter(Planet.id==id).first_or_404(description=f'Record with id={id} is not available'.format(id))
    db.session.delete(record)
    db.session.commit()
    return '', 204

@app.route('/vehicle', methods=['GET'])
def vehicle():
    all_vehicle=Planet.query.all()
    response_body = [x.serialize() for x in all_vehicle]
    return jsonify(response_body), 200

@app.route('/vehicle/<int:id>', methods=['GET'])
def vehicle_by_id(id):
    vehicle=Vehicle.query.filter(Vehicle.id==id).first_or_404(description=f'Record with id={id} is not available'.format(id))
    response_body = vehicle.serialize()
    return jsonify(response_body), 200

@app.route('/vehicle', methods=['POST'])
def vehicle_edit():
    args = request.get_json(silent=True)
    vehicle = Vehicle(name=args['name'], model=args['model'], vehicle_class=args['vehicle_class'],
            manufacturer=args['manufacturer'], length=args['length'], cost_in_credits=args['cost_in_credits'], 
            crew=args['crew'], passengers=args['passengers'], max_atmosphering_speed=args['max_atmosphering_speed'], 
            cargo_capacity=args['cargo_capacity'], consumables=args['consumables'], created=args['created'], edited=args['edited'])
    db.session.add(vehicle)
    db.session.commit()
    return Vehicle.serialize(vehicle), 201

@app.route('/vehicle/<int:id>', methods=['DELETE'])
def delete_vehicle_by_id(id):
    record = Vehicle.query.filter(Vehicle.id==id).first_or_404(description=f'Record with id={id} is not available'.format(id))
    db.session.delete(record)
    db.session.commit()
    return '', 204

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
