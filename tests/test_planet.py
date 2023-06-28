import unittest

from models.planet import Planet

class TestPlanet(unittest.TestCase):
    
    def setUp(self):
        self.planet_1 = Planet("Pluto", "G", "N/A", 2)
    
    def test_planet_has_name(self):
        self.assertEqual("Pluto", self.planet_1.name)
    
    def test_planet_has_class(self):
        self.assertEqual("G", self.planet_1.planet_class)
    
    def test_planet_has_native_species(self):
        self.assertEqual("N/A", self.planet_1.native_species)

    def test_planet_has_rating(self):
        self.assertEqual(2, self.planet_1.rating)

if __name__ == '__main__':
    unittest.main()