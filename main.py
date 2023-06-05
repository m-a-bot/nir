from database import DBManager
from generator import Generator
from tools import *
from desc_db import *

config = {
    "host": "localhost",
    "user": "root",
    "password": "z9Cx",
    "database": "sandbox"
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


def schemes_1nf():
    ...

def schemes_2nf():
    ...

def schemes_3nf():
    ...

def schemes_4nf():
    ...

def schemes_5nf():
    ...


if __name__ == "__main__":

    # copy_database()

    generator = Generator()

    # with DBManager(config) as manager:
    #     # manager.insert('Persons',
    #     # ['first_name', 'last_name', "gender", 'address_location', 'email', 'number'], generator.generate_persons())

    #     # with Timer() as timer:
    #     #     manager.insert('Companies',
    #     #     ['name_company', 'description', 'representative', 'location_company'],
    #     #     generator.generate_companies(n = 2))
    #     # print(timer.elapsed)

    #     # print(manager.select('Persons'))

    #     generation_time = []
    #     data = []
    #     update_db_time = []

    #     for i in range(1, 50):
    #         with Timer() as timer:
    #             data.append(generator.generate_companies(n=i))
    #         generation_time.append(timer.elapsed)

    #     for i in range(49):
    #         with Timer() as timer:
    #             manager.update('Companies',
    #                            ['name_company', 'description', 'representative', 'location_company'], data[i])
    #         update_db_time.append(timer.elapsed)

    #     plotter = Plotter()
    #     plotter.plot(generation_time)
    #     plotter.show()

    #     plotter.plot(update_db_time)
    #     plotter.show()

    with DBManager(config) as organizer:

        insert_time = []
        select_time = []
        db_sizes = []
        average_table_size = []

        organizer.switch_database('1nf')

        for schema in schemes_1nf():
            organizer.create_table(schema)

        with Timer() as timer:
            organizer.insert()
        insert_time.append(timer.elapsed)

        with Timer() as timer:
            organizer.select()
        select_time.append(timer.elapsed)
        
        db_sizes.append(organizer.get_size_database())
        average_table_size.append(organizer.get_average_table_size())

        organizer.switch_database('2nf')

        for schema in schemes_2nf():
            organizer.create_table(schema)

        with Timer() as timer:
            organizer.insert()
        insert_time.append(timer.elapsed)

        with Timer() as timer:
            organizer.select()
        select_time.append(timer.elapsed)
        
        db_sizes.append(organizer.get_size_database())
        average_table_size.append(organizer.get_average_table_size())

        organizer.switch_database('3nf')

        for schema in schemes_3nf():
            organizer.create_table(schema)

        with Timer() as timer:
            organizer.insert()
        insert_time.append(timer.elapsed)

        with Timer() as timer:
            organizer.select()
        select_time.append(timer.elapsed)
        
        db_sizes.append(organizer.get_size_database())
        average_table_size.append(organizer.get_average_table_size())

        organizer.switch_database('4nf')

        for schema in schemes_4nf():
            organizer.create_table(schema)

        with Timer() as timer:
            organizer.insert()
        insert_time.append(timer.elapsed)

        with Timer() as timer:
            organizer.select()
        select_time.append(timer.elapsed)
        
        db_sizes.append(organizer.get_size_database())
        average_table_size.append(organizer.get_average_table_size())

        organizer.switch_database('5nf')

        for schema in schemes_5nf():
            organizer.create_table(schema)

        with Timer() as timer:
            organizer.insert()
        insert_time.append(timer.elapsed)

        with Timer() as timer:
            organizer.select()
        select_time.append(timer.elapsed)
        
        db_sizes.append(organizer.get_size_database())
        average_table_size.append(organizer.get_average_table_size())

        plt = Plotter()

        plt.plot(insert_time)
        plt.set_title('Insert')
        plt.show()

        plt.plot(select_time)
        plt.set_title('Select')
        plt.show()

        plt.plot(db_sizes)
        plt.set_title('Database sizes')
        plt.show()

        plt.plot(average_table_size)
        plt.set_title('Average table size')
        plt.show()