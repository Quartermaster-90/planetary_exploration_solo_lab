from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.planet import Planet
from models.city import City

import repositories.planet_repository as planet_repository
import repositories.city_repository as city_repository

planets_blueprint = Blueprint("planets", __name__)


@planets_blueprint.route("/planets")
def planets():
    planets = planet_repository.select_all()
    return render_template("planets/index.html", all_planets = planets)


@planets_blueprint.route("/planets/new", methods =['GET'])
def new_planet():
    # cities = city_repository.select_all()
    return render_template("planets/new.html")


@planets_blueprint.route("/planets", methods=['POST'])
def create_planet():
    name           = request.form['name']
    planet_class   = request.form['planet_class']
    native_species = request.form['native_species']
    rating         = request.form['rating']
    planet         = Planet(name, planet_class, native_species, rating)
    planet_repository.save(planet)
    return redirect("/planets")


@planets_blueprint.route("/planets/<id>", methods=['GET'])
def show_planet(id):
    planet = planet_repository.select(id)
    cities = city_repository.cities_for_planet(planet)
    return render_template("planets/show.html", planet = planet, cities = cities)


@planets_blueprint.route("/planets/<id>/edit", methods=['GET'])
def edit_planet(id):
    planet = planet_repository.select(id)
    # cities = city_repository.city_for_planet(planet)
    return render_template("planets/edit.html", planet = planet)


@planets_blueprint.route("/planets/<id>", methods=['POST'])
def update_planet(id):
    name           = request.form['name']
    planet_class   = request.form['planet_class']
    native_species = request.form['native_species']
    rating         = request.form['rating']
    planet         = Planet(name, planet_class, native_species, rating)
    planet_repository.update(planet)
    return redirect("/planets")


@planets_blueprint.route("/planets/<id>/delete", methods=['POST]'])
def delete_planet(id):
    planet_repository.delete(id)
    return redirect("/planets")