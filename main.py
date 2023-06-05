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
    
    employees = """
    create table Employees(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    date_of_birth date not null,
    number varchar(20) not null,
    email varchar(255),
    ID_position int,
    ID_department int,
    FOREIGN KEY (ID_position) REFERENCES Positions (ID),
    FOREIGN KEY (ID_department) REFERENCES Departments (ID)
    );
    """
    positions = """
    create table Positions(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    salary numeric not null
    );
    """
    departments = """
    create table Departments(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null
    );
    """
    projects = """
    create table Projects(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    date_of_start datetime not null,
    date_of_end datetime not null
    );
    """
    project_participants = """
    create table ProjectParticipants(
    ID_employee int not null,
    ID_project int not null,
    PRIMARY KEY (ID_employee, ID_project),
    FOREIGN KEY (ID_employee) REFERENCES Employees (ID),
    FOREIGN KEY (ID_project) REFERENCES Projects (ID)
    );
    """
    return [employees, positions, departments, projects, project_participants]

def schemes_2nf():
    
    employees = """
    create table Employees(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    date_of_birth date not null,
    number varchar(20) not null,
    email varchar(255),
    ID_position int,
    FOREIGN KEY (ID_position) REFERENCES Positions (ID)
    );
    """
    positions = """
    create table Positions(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    salary numeric not null,
    ID_department int,
    FOREIGN KEY (ID_department) REFERENCES Departments (ID)
    );
    """
    departments = """
    create table Departments(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null
    );
    """
    projects = """
    create table Projects(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    date_of_start datetime not null,
    date_of_end datetime not null
    );
    """
    project_participants = """
    create table ProjectParticipants(
    ID_employee int not null,
    ID_project int not null,
    PRIMARY KEY (ID_employee, ID_project),
    FOREIGN KEY (ID_employee) REFERENCES Employees (ID),
    FOREIGN KEY (ID_project) REFERENCES Projects (ID)
    );
    """
    return [employees, positions, departments, projects, project_participants]

def schemes_3nf():
    
    employees = """
    create table Employees(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    date_of_birth date not null,
    number varchar(20) not null,
    email varchar(255),
    ID_position int,
    FOREIGN KEY (ID_position) REFERENCES Positions (ID)
    );
    """
    positions = """
    create table Positions(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    salary numeric not null,
    );
    """
    departments = """
    create table Departments(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    ID_director int,
    FOREIGN KEY (ID_director) REFERENCES Employees (ID)
    );
    """
    projects = """
    create table Projects(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    date_of_start datetime not null,
    date_of_end datetime not null,
    ID_department int,
    FOREIGN KEY (ID_department) REFERENCES Departments (ID)
    );
    """
    project_participants = """
    create table ProjectParticipants(
    ID_employee int not null,
    ID_project int not null,
    PRIMARY KEY (ID_employee, ID_project),
    FOREIGN KEY (ID_employee) REFERENCES Employees (ID),
    FOREIGN KEY (ID_project) REFERENCES Projects (ID)
    );
    """
    return [employees, positions, departments, projects, project_participants]

def schemes_4nf():
    
    employees = """
    create table Employees(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    date_of_birth date not null,
    number varchar(20) not null,
    email varchar(255),
    ID_position int,
    FOREIGN KEY (ID_position) REFERENCES Positions (ID),
    ID_department int,
    FOREIGN KEY (ID_department) REFERENCES Departments (ID)
    );
    """
    positions = """
    create table Positions(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    salary numeric not null,
    );
    """
    departments = """
    create table Departments(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    );
    """
    projects = """
    create table Projects(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    date_of_start datetime not null,
    date_of_end datetime not null,
    );
    """
    project_participants = """
    create table ProjectParticipants(
    ID_employee int not null,
    ID_project int not null,
    PRIMARY KEY (ID_employee, ID_project),
    FOREIGN KEY (ID_employee) REFERENCES Employees (ID),
    FOREIGN KEY (ID_project) REFERENCES Projects (ID)
    );
    """
    return [employees, positions, departments, projects, project_participants]

def schemes_5nf():
    
    employees = """
    create table Employees(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    date_of_birth date not null,
    number varchar(20) not null,
    email varchar(255),
    ID_position int,
    FOREIGN KEY (ID_position) REFERENCES Positions (ID),
    ID_department int,
    FOREIGN KEY (ID_department) REFERENCES Departments (ID)
    );
    """
    positions = """
    create table Positions(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    salary numeric not null,
    );
    """
    departments = """
    create table Departments(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    );
    """
    projects = """
    create table Projects(
    ID int not null AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) not null,
    date_of_start datetime not null,
    date_of_end datetime not null,
    );
    """
    project_participants = """
    create table ProjectParticipants(
    ID_employee int not null,
    ID_project int not null,
    start_date datetime not null,
    end_date datetime not null,
    number_of_working_hours int not null,
    PRIMARY KEY (ID_employee, ID_project),
    FOREIGN KEY (ID_employee) REFERENCES Employees (ID),
    FOREIGN KEY (ID_project) REFERENCES Projects (ID)
    );
    """
    return [employees, positions, departments, projects, project_participants]


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
            organizer.insert('Employees', [])
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