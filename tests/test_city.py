import unittest

from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city_1 = City("New York", "Bajor", 4, "Great place!", True)
        self.city_2 = City("Beijing", "Vulcan", 3, "Not great", False)
    
    def test_city_has_name(self):
        self.assertEqual("New York", self.city_1.name)
    
    def test_city_has_planet(self):
        self.assertEqual("Bajor", self.city_1.planet)

    def test_city_has_rating(self):
        self.assertEqual(4, self.city_1.rating)

    def test_city_has_comment(self):
        self.assertEqual("Great place!", self.city_1.comments)

    def test_city_was_visited(self):
        explored = True
        self.city_1.mark_explored()
        self.assertEqual(self.city_1.explored, explored)

if __name__ == '__main__':
    unittest.main()