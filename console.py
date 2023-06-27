import pdb
from models.planet import Planet
from models.city import City

import repositories.planet_repository as planet_repository
import repositories.city_repository as city_repository

planet_repository.delete_all()
city_repository.delete_all()

planet_1 = Planet("Vulcan", "M", "Vulcan", 4)
planet_repository.save(planet_1)

planet_2 = Planet("Earth", "M", "Humans", 5)
planet_repository.save(planet_2)

planet_3 = Planet("Qo'nos", "M", "Klingon", 2)
planet_repository.save(planet_3)

planet_4 = Planet("Bajor", "M", "Bajoran", 3)
planet_repository.save(planet_4)

planet_repository.select_all()


city_1 = City("Gol", planet_1, 3, "Not much left to see after the war.", True)
city_repository.save(city_1)

city_2 = City("Kir", planet_1, 4, "Interesting ruins to explore.", True)
city_repository.save(city_2)

city_3 = City("Raal", planet_1, 0, "On my 'to visit' list.", False)
city_repository.save(city_3)

city_4 = City("Paris", planet_2, 4, "Fine cuisines available.", True)
city_repository.save(city_4)

city_5 = City("Edinburgh", planet_2, 3, "Interesting sights, but bloody cold!", True)
city_repository.save(city_5)

city_6 = City("Kang's Summit", planet_3, 0, "On my 'to visit' list.", False)
city_repository.save(city_6)

city_7 = City("Vi'chak", planet_3, 0, "Not sure about this destination yet.", False)
city_repository.save(city_7)

city_8 = City("B'hala", planet_4, 4, "Some lovely scenery.", True)
city_repository.save(city_8)

city_9 = City("Hathon", planet_4, 4, "Again, lovely scenery.", True)
city_repository.save(city_9)

city_10 = City("Jalanda City", planet_4, 3, "A bit noisy and too busy for my liking.", True)
city_repository.save(city_10)


pdb.set_trace()