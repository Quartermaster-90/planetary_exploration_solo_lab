class Planet:

    def __init__(self, name, planet_class, native_species, rating, id = None):
        self.name = name
        self.planet_class = planet_class
        self.native_species = native_species
        self.rating = rating
        self.id = id


    def __repr__(self):
        return self.name
    