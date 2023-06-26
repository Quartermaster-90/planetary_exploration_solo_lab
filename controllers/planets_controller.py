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
    return render_template("/planets/index.html", all_planets = planets)