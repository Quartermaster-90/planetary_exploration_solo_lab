import pdb
from models.planet import Planet
from models.city import City

import repositories.planet_repository as planet_repository
import repositories.city_repository as city_repository

planet_repository.delete_all()
city_repository.delete_all()



pdb.set_trace()