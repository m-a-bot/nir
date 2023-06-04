def schema_table_persons():

    string = """CREATE TABLE Persons(
        id_person INT NOT NULL AUTO_INCREMENT,
        first_name VARCHAR(60) NOT NULL,
        last_name VARCHAR(60) NOT NULL,
        gender VARCHAR(6) NOT NULL,
        address_location VARCHAR(100) NOT NULL,
        email VARCHAR(150) DEFAULT 'test@test.ru',
        number VARCHAR(20) NOT NULL,
        PRIMARY KEY(id_person)
    );"""

    return string


def schema_table_employees():

    string = """CREATE TABLE Employees(
        id INT NOT NULL,
        date_of_employment DATE NOT NULL,
        salary NUMERIC NOT NULL,
        number_of_tasks INT DEFAULT 0 NOT NULL,
        FOREIGN KEY (id) REFERENCES Persons (id_person)
    );"""

    return string


def schema_table_positions():

    return """
        CREATE TABLE Positions (
            id INT NOT NULL AUTO_INCREMENT,
            title VARCHAR(100) NOT NULL,
            description VARCHAR(160) NOT NULL,
            PRIMARY KEY(id)
        );
    """


def schema_table_PositionsOfEmployees():
    
    return """
        create table PositionsOfEmployees(
            id_employee INT NOT NULL, 
            id_position INT NOT NULL,
            bet NUMERIC NOT NULL,
            FOREIGN KEY (id_employee) REFERENCES Persons (id_person),
            FOREIGN KEY (id_position) REFERENCES Positions (id)
        );
    """


def schema_table_companies():
    
    return """
        create table Companies(
            id INT NOT NULL AUTO_INCREMENT,
            name_company VARCHAR(100) NOT NULL,
            description VARCHAR(500) NOT NULL,
            representative VARCHAR(100) NOT NULL,
            location_company VARCHAR(300) NOT NULL,
            PRIMARY KEY (id)
        );
    """




def schema_table_projects():
    
    return """
    CREATE TABLE Projects (
        id INT NOT NULL,
        id_company INT NOT NULL,
        type_project VARCHAR (300) NOT NULL,
        technical_specification VARCHAR (300) NOT NULL,
        number_of_tasks INT NOT NULL,
        summary NUMERIC NOT NULL,
        dead_line DATE NOT NULL,
        responsible_person INT,
        PRIMARY KEY(id, id_company),
        FOREIGN KEY (responsible_person) REFERENCES Employees (id)
    );
"""


def schema_table_tasks():
    
    return """
    CREATE TABLE Tasks (
        id_task INT NOT NULL,
        id_project INT NOT NULL,
        title VARCHAR(100) NOT NULL,
        description_ VARCHAR(300) NOT NULL,
        dead_line_time time NOT NULL,
        dead_line date NOT NULL,
        responsible_person INT,
        PRIMARY KEY(id_task, id_project),
        FOREIGN KEY (responsible_person) REFERENCES Employees (id)
    ); """