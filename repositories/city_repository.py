from db.run_sql import run_sql

from models.city import City
from models.planet import Planet

import repositories.planet_repository as planet_repository

def save(city):
    sql     = """INSERT INTO cities (name, planet_id, rating, comments, explored)
                 VALUES (%s, %s, %s, %s, %s)
                 RETURNING *"""
    values  = [city.name, city.planet.id, city.rating, city.comments, city.explored]
    results = run_sql(sql, values)
    id      = results[0]['id']
    city.id = id
    
    return city


def select_all():
    cities = []

    sql     = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        planet = planet_repository.select(row['planet_id'])
        city   = City(row['name'], planet, row['rating'], row['comments'], row['explored'], row['id'])
        cities.append(city)
    
    return cities


def select(id):
    city   = None
    sql    = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        planet = planet_repository.select(result['planet_id'])
        city   = City(result['name'], planet, result['rating'], result['comments'], result['explored'], result['id'])
    
    return city


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(city):
    sql    = """UPDATE cities SET (name, planet_id, rating, comments, explored) = (%s, %s, %s, %s, %s)
                WHERE id = %s"""
    values = [city.name, city.planet.id, city.rating, city.comments, city.explored]
    run_sql(sql, values)


def cities_for_planet(planet):
    cities = []

    sql     = "SELECT * FROM cities WHERE planet_id = %s"
    values  = [planet.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['planet_id'], row['rating'], row['comments'], row['explored'], row['id'])
        cities.append(city)

    return cities


# def city_names_for_planet(planet):
#     cities = []

#     sql     = "SELECT name FROM cities WHERE planet_id = %s"
#     values  = [planet.id]
#     results = run_sql(sql, values)

#     for row in results:
#         city = City(row['name'])
#         cities.append(city)

#     return cities