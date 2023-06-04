from database import DBManager
from generator import Generator
from tools import *
from desc_db import *

config = {
    "host" : "localhost",
    "user" : "root",
    "password" : "z9Cx",
    "database" : "sandbox"
}


def copy_database():
    with DBManager(config) as manager:

        manager.create_table(schema_table_persons())
        manager.create_table(schema_table_employees())
        manager.create_table(schema_table_positions())
        manager.create_table(schema_table_PositionsOfEmployees())
        manager.create_table(schema_table_companies())
        manager.create_table(schema_table_projects())
        manager.create_table(schema_table_tasks())

        manager.dump()


if __name__ == "__main__":

    # copy_database()

    generator = Generator()

    with DBManager(config) as manager:
        # manager.insert('Persons', ['first_name', 'last_name', "gender", 'address_location', 'email', 'number'], generator.generate_persons())

        # with Timer() as timer:
        #     manager.insert('Companies', ['name_company', 'description', 'representative', 'location_company'], generator.generate_companies(n = 2))
        # print(timer.elapsed)

        # print(manager.select('Persons'))

        data = []

        for i in range(1, 50):
            with Timer() as timer:
                manager.update('Companies', ['name_company', 'description', 'representative', 'location_company'], generator.generate_companies(n = i))
            data.append(timer.elapsed)

        plotter = Plotter()
        plotter.plot(data)
        #plotter.save()
        plotter.show()