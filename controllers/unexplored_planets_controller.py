# from flask import Flask, render_template, request, redirect
# from flask import Blueprint

# from models.planet import Planet
# from models.city import City

# import repositories.planet_repository as planet_repository
# import repositories.city_repository as city_repository

# unexplored_planets_blueprint = Blueprint("unexplored_planets", __name__)

# @unexplored_planets_blueprint.route("/unexplored_planets")
# def planets():
#     planets = planet_repository.select_all()
#     return render_template("/uneplored_planets/index.html", all_planets = planets)