import random
import re

ENG = "abcdefghijklmnopqrstuvwxyz"
NUM = "0123456789"


# [0, 1)
def rand() -> float:
    return random.random()


def rand0toB(B: int) -> int:
    return int(rand() * B)


def randAtoB(A: int, B: int, step=1) -> int:
    t = rand()
    t *= B - A
    t += A

    if step != 1:
        h = (B - A) // step

        return int(A + rand0toB(h) * step)

    return int(t)


def shuffle(array):
    for i in range(len(array)-1, 1, -1):
        j = rand0toB(i+1)
        array[i], array[j] = array[j], array[i]


def generate_symbol(symbols=ENG):
    n = len(symbols)

    return symbols[rand0toB(n)]


def generate_string(length: int, symbols=ENG) -> str:

    string_expected = ""

    for i in range(length):
        string_expected += generate_symbol(symbols)

    return string_expected


def generate_string_with_different_length(length_a: int, length_b: int, symbols=ENG) -> str:
    string_expected = ""

    for i in range(length := randAtoB(length_a, length_b)):
        string_expected += generate_symbol(symbols)

    return string_expected


def generate_n_strings(n: int):
    return [generate_string_with_different_length(10, 21) for _ in range(n)]


def get_string_with_capital_symbol(symbs: str) -> str:

    return symbs[0].upper() + symbs[1:]


def get_proposal(string: str) -> str:

    return get_string_with_capital_symbol(string) + "."


def get_text(count_proposals):

    result = " ".join([get_proposal(generate_string_with_different_length(10, 30)) for _ in range(count_proposals)])

    return result


def get_first_name(length_a: int = 4, length_b: int = 31):
    return get_string_with_capital_symbol(
        generate_string_with_different_length(length_a, length_b)
    )


def get_last_name(length_a: int = 4, length_b: int = 31):
    return get_string_with_capital_symbol(
        generate_string_with_different_length(length_a, length_b)
    )


def get_gender():
    data = ["man", "woman"]
    return data[rand0toB(2)]


def get_address():
    return get_string_with_capital_symbol(generate_string_with_different_length(10, 30)) + ", " + str(randAtoB(1, 100))


def get_email(length: int):
    available_length = length - length//2 - 2
    personal_inf = generate_symbol(ENG + ENG.upper())+generate_string(length//2-3, ENG + ENG.upper() + NUM)

    a = generate_string_with_different_length(available_length//3, available_length//2)
    b = generate_string(available_length-len(a))

    return personal_inf + "@" + a + "." + b


def get_number():
    length: int = 10
    string_expected = "7"

    for _ in range(length):
        string_expected += generate_symbol(NUM)
    
    return re.sub(r"(\d)(\d{3})(\d{3})(\d{2})(\d{2})", r"+\1-\2-\3-\4-\5", string_expected)


def get_date():
    dd = randAtoB(1, 32)
    mm = randAtoB(1, 13)
    yy = randAtoB(2010, 2023)

    if mm == 4 or mm == 6 or mm==9 or mm==11:
        dd = randAtoB(1, 31)

    if mm == 2:
        if yy % 4 == 0:
            dd = randAtoB(1, 30)
        else:
            dd = randAtoB(1, 29)

    return f"{yy}-{mm}-{dd}"


def get_time():
    hh = rand0toB(24)
    mm = rand0toB(60)
    sec = rand0toB(60)

    return f"{hh}:{mm}:{sec}"


class Generator:
    
    def __init__(self, seed = None):

        if seed:
            random.seed(seed)


    """
    first_name, last_name, gender, address_location, email, number
    """
    def generate_persons(self, number: int = 1):

        data = []

        for _ in range(number):
            data.append(
                (get_first_name(), get_last_name(), get_gender(), get_address(), get_email(randAtoB(15, 30)), get_number())
            )

        return data


    """
    date_of_employment, salary, number_of_tasks
    """
    def generate_employees(self, number: int = 1):

        data = []

        for _ in range(number):

            data.append((get_date(), randAtoB(25000, 75000, step=1000), rand0toB(10)))

        return data
    
    
    """
    id: INT, title: VARCHAR, description: VARCHAR
    """
    def generate_positions(self, number: int = 1):

        data = []

        for _ in range(number):

            data.append(
                (get_string_with_capital_symbol(generate_string_with_different_length(10, 25)), get_text(randAtoB(5, 10)))
            )

        return data


    """
    id_employee: INT
    id_position: INT
    bet: NUMERIC
    """
    def _generate_positionsOfEmployees(self, n: int = 1):

        data = []

        for _ in range(n):

            data.append(
                (rand())
            )

        return data


    """
    id: INT
    name_company: VARCHAR(100)
    description: VARCHAR(500)
    representative: VARCHAR(100)
    location_company: VARCHAR(300)
    """
    def generate_companies(self, n: int = 1):

        data = []

        for _ in range(n):

            data.append(
                (get_first_name(10, 25), get_text(randAtoB(5, 10)), get_last_name() + " " + get_first_name(), get_address())
            )

        return data


    """
    id_project: INT
    id_company: INT
    type_project: VARCHAR(100)
    technical_specification: VARCHAR
    number_of_tasks: INT
    summary: NUMERIC
    dead_line: DATE
    responsible_person: INT
    """
    def generate_projects(self, n: int = 1):

        data = []

        for _ in range(n):

            data.append(
                (get_first_name(10, 100), get_text(randAtoB(5, 10)), randAtoB(1,6), randAtoB(10000, 150000, 10000), get_date())
            )

        return data


    """
    id_task: INT
    id_project: INT
    title: VARCHAR(100)
    description: VARCHAR
    dead_line_time: TIME
    dead_line: DATE
    responsible_person: INT
    """
    def generate_tasks(self, n: int = 1):

        data = []

        for _ in range(n):

            data.append(
                (get_first_name(10, 100), get_text(randAtoB(5, 10)), randAtoB(1,6), randAtoB(10000, 150000, 10000), get_time(), get_date())
            )

        return data
