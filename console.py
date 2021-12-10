from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository

manufacturer_repository.delete_all()

manufacturer1 = Manufacturer('Fender', True)
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer('Gibson', True)
manufacturer_repository.save(manufacturer2)

# print(manufacturer1.name, manufacturer1.is_active, manufacturer1.id)

# print(manufacturer2.name, manufacturer2.is_active, manufacturer2.id)

manufacturers = manufacturer_repository.select_all()
for manufacturer in manufacturers:
    print(manufacturer.name, manufacturer.is_active, manufacturer.id)
