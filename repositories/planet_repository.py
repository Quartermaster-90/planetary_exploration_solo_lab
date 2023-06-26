from db.run_sql import run_sql

from models.planet import Planet

import repositories.city_repository as city_repository

def save(planet):
    sql = """INSERT INTO planets (name, planet_class, native_species, rating)
             VALUES (%s, %s, %s, %s, %s)
             RETURNING *"""
    values = [planet.name, planet.planet_class, planet.native_species, planet.rating]
    results = run_sql(sql, values)
    id = results[0]['id']
    planet.id = id
    return planet

def select_all():
    planets = []

    sql = "SELECT * FROM planets"
    results = run_sql(sql)

    for row in results:
        planet = Planet(row['name'], row['planet_class'], row['native_species'], row['rating'], row['id'])
        planets.append(planet)
    
    return planets

def select(id):
    planet = None
    sql = "SELECT * FROM planets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        planet = Planet(result['name'], result['planet_class'], result['native species'], result['rating'], result['id'])
    
    return planet

def delete_all():
    sql = "DELETE FROM planets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM planets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(planet):
    sql = """UPDATE planets SET (name, planet_class, native species, rating, explored) = (%s, %s, %s, %s, %s)
             WHERE id = %s"""
    values = [planet.name, planet.planet_class, planet.native_species, planet.rating]
    run_sql(sql, values)