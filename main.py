from database import DBManager
from generator import *
from tools import *
from desc_db import *

config = {
    "host": "localhost",
    "user": "root",
    "password": "z9Cx",
    "database": "Management"
}


def create_sandbox():
    global config
    config['database'] = 'sandbox'
    with DBManager(config) as manager:
        manager.restore("sandbox.sql")



def task2():
    generator = Generator()
    plt = Plotter()
    data = []
    number_of_table = 0
    number_of_rows = 100
    print("Выберите таблицу. Persons, Employees, Positions, Companies, PositionsOfEmployees, Projects, Tasks.")
    try:
        number_of_table = int(input())
    except:
        ...
    
    generate_time = []
    for i in range(1, number_of_rows):
        with Timer() as timer:
            if number_of_table == 0:
                data.append(generator.generate_persons(i))

            if number_of_table == 1:
                data.append(generator.generate_employees(i))

            if number_of_table == 2:
                data.append(generator.generate_positions(i))

            if number_of_table == 3:
                data.append(generator.generate_companies(i))

            if number_of_table == 4:
                data.append(generator._generate_positionsOfEmployees(i))

            if number_of_table == 5:
                data.append(generator.generate_projects(i))

            if number_of_table == 6:
                data.append(generator.generate_tasks(i))
        generate_time.append(timer.elapsed)

    plt.set_title("график времени генерации данных")
    plt.set_xlabel("количество генерируемых строк")
    plt.set_ylabel("время")
    plt.plot(generate_time)
    plt.show()
    return number_of_table, data

def task3(number_of_table, data):
    plt = Plotter()
    insert_time = []
    select_time = []
    delete_time = []

    number_of_rows = len(data)

    with DBManager(config) as manager:

        if number_of_table == 0:
            manager.delete('Persons')
        if number_of_table == 1:
            manager.delete('Employees')
        if number_of_table == 2:
            manager.delete('Positions')
        if number_of_table == 3:
            manager.delete('Companies')
        if number_of_table == 4:
            manager.delete('PositionsOfEmployees')
        if number_of_table == 5:
            manager.delete('Projects')
        if number_of_table == 6:
            manager.delete('Tasks')

        for i in range(1, number_of_rows):
            
            with Timer() as timer:
                if number_of_table == 0:
                    manager.insert('Persons', ['first_name', 'last_name', 'gender', 'address_location', 'email', 'number'], data[i-1])
                if number_of_table == 1:
                    manager.insert('Employees', ['date_of_employment', 'salary', 'number_of_tasks'], data[i-1])
                if number_of_table == 2:
                    manager.insert('Positions', ['title', 'description'], data[i-1])
                if number_of_table == 3:
                    manager.insert('Companies', ['name_company', 'description', 'representative', 'location_company'], data[i-1])
                if number_of_table == 4:
                    manager.insert('PositionsOfEmployees', None, [1,1].extend(data[i-1]))
                if number_of_table == 5:
                    manager.insert('Projects', 
                        ['id_company', 'type_project', 'technical_specification', 'number_of_tasks', 'summary', 'dead_line', 'responsible_person'],
                        data[i-1])
                if number_of_table == 6:
                    manager.insert('Tasks', ['id_project', 'title', 'description_', 'dead_line_time', 'dead_line', 'responsible_person'], data[i-1])

            insert_time.append(timer.elapsed)

            with Timer() as timer:
                if number_of_table == 0:
                    manager.select('Persons')
                if number_of_table == 1:
                    manager.select('Employees')
                if number_of_table == 2:
                    manager.select('Positions')
                if number_of_table == 3:
                    manager.select('Companies')
                if number_of_table == 4:
                    manager.select('PositionsOfEmployees')
                if number_of_table == 5:
                    manager.select('Projects')
                if number_of_table == 6:
                    manager.select('Tasks')

            select_time.append(timer.elapsed)

            with Timer() as timer:
                if number_of_table == 0:
                    manager.delete('Persons')
                if number_of_table == 1:
                    manager.delete('Employees')
                if number_of_table == 2:
                    manager.delete('Positions')
                if number_of_table == 3:
                    manager.delete('Companies')
                if number_of_table == 4:
                    manager.delete('PositionsOfEmployees')
                if number_of_table == 5:
                    manager.delete('Projects')
                if number_of_table == 6:
                    manager.delete('Tasks')
            delete_time.append(timer.elapsed)
    
    plt.set_title("SELECT *")
    plt.set_xlabel("количество запрашиваемых строк")
    plt.set_ylabel("время")
    plt.plot(select_time)
    plt.show()

    plt.set_title("INSERT")
    plt.set_xlabel("количество вставляемых строк")
    plt.set_ylabel("время")
    plt.plot(insert_time)
    plt.show()

    plt.set_title("DELETE")
    plt.set_xlabel("количество удаляемых строк")
    plt.set_ylabel("время")
    plt.plot(delete_time)
    plt.show()

def task5():
    plt = Plotter()
    # Исследовать эффективность использования индексов
    number_of_rows = 100
    data = []
    data1 = []
    data2 = []
    for _ in range(1, number_of_rows):
        data.append((
            get_first_name(), get_last_name(), get_address(), get_salary()
        ))
        data1.append((
            get_first_name(10), get_text(6), get_first_name(9), get_address(), rand0toB(10)
        ))
        data2.append((
            proposal(), get_text(7), get_date()
        ))

    config['database'] = 'using_indexes'
    insertT1_time = []
    insertT2_time = []
    insertT3_time = []
    insertT4_time = []
    insertT5_time = []
    insertT6_time = []

    selectT1_time = []
    selectT2_time = []
    selectT3_time = []
    selectT4_time = []
    selectT5_time = []
    selectT6_time = []
    with DBManager(config) as manager:
        
        for i in range(1,number_of_rows):
            # T1
            with Timer() as timer:
                manager.insert('T1', ['first_name', 'last_name', 'address_location', 'salary'],
                               data[:i])
            insertT1_time.append(timer.elapsed)

            # T2
            with Timer() as timer:
                manager.insert('T2', ['first_name', 'last_name', 'address_location', 'salary'],
                               data[:i])
            insertT2_time.append(timer.elapsed)

            # T3
            with Timer() as timer:
                manager.insert('T3', None, data1[:i])
            insertT3_time.append(timer.elapsed)
            # T4
            with Timer() as timer:
                manager.insert('T4', None, data1[:i])
            insertT4_time.append(timer.elapsed)
            # T5
            with Timer() as timer:
                manager.insert('T5', None, data2[:i])
            insertT5_time.append(timer.elapsed)
            # T6
            with Timer() as timer:
                manager.insert('T6', None, data2[:i])
            insertT6_time.append(timer.elapsed)

            # T1
            with Timer() as timer:
                manager.select('T1')
            selectT1_time.append(timer.elapsed)
            # T2
            with Timer() as timer:
                manager.select('T2')
            selectT2_time.append(timer.elapsed)
            # T3
            with Timer() as timer:
                manager.select('T3')
            selectT3_time.append(timer.elapsed)
            # T4
            with Timer() as timer:
                manager.select('T4')
            selectT4_time.append(timer.elapsed)
            # T5
            with Timer() as timer:
                manager.select('T5')
            selectT5_time.append(timer.elapsed)
            # T6
            with Timer() as timer:
                manager.select('T6')
            selectT6_time.append(timer.elapsed)

            manager.delete('T1')
            manager.delete('T2')
            manager.delete('T3')
            manager.delete('T4')
            manager.delete('T5')
            manager.delete('T6')

    plt.plot(selectT1_time, _label = "T1")
    plt.plot(selectT2_time, _label = "T2")
    plt.set_title("select")
    plt.set_legend()
    plt.set_xlabel("количество вставляемых строк")
    plt.set_ylabel("время")
    plt.show()

    plt.plot(selectT3_time, _label = "T3")
    plt.plot(selectT4_time, _label = "T4")
    plt.set_title("select")
    plt.set_legend()
    plt.set_xlabel("количество вставляемых строк")
    plt.set_ylabel("время")
    plt.show()

    plt.plot(selectT5_time, _label = "T5")
    plt.plot(selectT6_time, _label = "T6")
    plt.set_title("select")
    plt.set_legend()
    plt.set_xlabel("количество вставляемых строк")
    plt.set_ylabel("время")
    plt.show()

    plt.plot(insertT1_time, _label = "T1")
    plt.plot(insertT2_time, _label = "T2")
    plt.set_title("insert")
    plt.set_xlabel("количество запрашиваемых строк")
    plt.set_ylabel("время")
    plt.set_legend()
    plt.show()

    plt.plot(insertT3_time, _label = "T3")
    plt.plot(insertT4_time, _label = "T4")
    plt.set_title("insert")
    plt.set_legend()
    plt.set_xlabel("количество запрашиваемых строк")
    plt.set_ylabel("время")
    plt.show()

    plt.plot(insertT5_time, _label = "T5")
    plt.plot(insertT6_time, _label = "T6")
    plt.set_title("insert")
    plt.set_legend()
    plt.set_xlabel("количество запрашиваемых строк")
    plt.set_ylabel("время")
    plt.show()


if __name__ == "__main__":

    create_sandbox()

    number_of_table, data = task2()

    task3(number_of_table, data)

    task5()

    