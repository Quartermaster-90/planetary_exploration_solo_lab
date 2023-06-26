class City:

    def __init__(self, name, planet, rating, comments, explored = False, id = None):
        self.name = name
        self.planet = planet
        self.rating = rating
        self.comments = comments
        self.explored = explored
        self.id = id

    def mark_explored(self):
        self.explored = True