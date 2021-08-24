from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(250))
    diameter = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250))
    gravity = db.Column(db.String(250))
    population = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.String(250))
    created = db.Column(db.String(250))
    edited = db.Column(db.String(250))

    def __repr__(self):
        return f'<Planet {self.name}-{self.id}> '

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    homeworld = db.relationship(Planet)
    gender = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    height = db.Column(db.String(250))
    mass = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    created = db.Column(db.String(250)) 
    edited = db.Column(db.String(250))

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "homeworld_id":self.homeworld_id,
            "gender":self.gender,
            "hair_color":self.hair_color,
            "height":self.height,
            "mass":self.mass,
            "skin_color":self.skin_color,
            "created":self.created,
            "edited":self.edited
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    model = db.Column(db.String(250))
    vehicle_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    length = db.Column(db.String(250))
    cost_in_credits = db.Column(db.String(250))
    crew = db.Column(db.String(250))
    passengers = db.Column(db.String(250))
    max_atmosphering_speed = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    consumables = db.Column(db.String(250))
    created = db.Column(db.String(250))
    edited = db.Column(db.String(250))


    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class":self.vehicle_class,
            "manufacturer":self.manufacturer,
            "length":self.length,
            "cost_in_credits":self.cost_in_credits,
            "crew":self.crew,
            "passengers":self.passengers,
            "max_atmosphering_speed":self.max_atmosphering_speed,
            "cargo_capacity":self.cargo_capacity,
            "consumables":self.consumables,
            "created":self.created,
            "edited":self.edited
            # do not serialize the password, its a security breach
        }