from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.city import City
from models.planet import Planet

import repositories.city_repository as city_repository
import repositories.planet_repository as planet_repository

cities_blueprint = Blueprint("cities", __name__)


@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("/cities/index.html", all_cities = cities)


@cities_blueprint.route("/cities/new", methods =['GET'])
def new_city():
    return render_template("cities/new.html")


@cities_blueprint.route("/cities", methods=['POST'])
def create_city():
    name      = request.form['name']
    planet_id = request.form['planet_id']
    rating    = request.form['rating']
    comments  = request.form['comments']
    explored  = request.form['explored']
    planet    = planet_repository.select(planet_id)
    city      = city(name, planet, rating, comments, explored)
    city_repository.save(city)
    return redirect("/cities")


@cities_blueprint.route("cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template("cities.show.html", city = city)


@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city    = city_repository.select(id)
    planets = planet_repository.select_all()
    return render_template("/cities/edit.html", city = city, all_planets = planets)


@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name      = request.form['name']
    planet_id = request.form['planet_id']
    rating    = request.form['rating']
    comments  = request.form['comments']
    explored  = request.form['explored']
    planet    = planet_repository.select(planet_id)
    city      = city(name, planet, rating, comments, explored)
    city_repository.update(city)
    return redirect("/cities")


@cities_blueprint.route("/cities/<id>/delete", methods=['POST]'])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")