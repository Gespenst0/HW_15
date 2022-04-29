import sqlite3

data = []


def fill_animals_task():
    for i in range(len(data)):
        query = f"""
            INSERT INTO animals_task (age_upon_outcome, animal_id, name, appearance_id, 
                                    date_of_birth, outcome_program_id, outcome_date_id) 
            VALUES ('{data[i][0]}', '{data[i][1]}', "{data[i][3]}", '{i+1}', '{data[i][7]}', '{i+1}', '{i+1}')
            """
        cursor.execute(query)


def fill_animal_breeds():
    for i in range(len(data)):
        query = f"""INSERT INTO animal_breeds (breed) VALUES ('{data[i][4]}')
        """
        cursor.execute(query)


def fill_animal_types():
    for i in range(len(data)):
        query = f"""
            INSERT INTO animal_types (animal_type)
            VALUES ('{data[i][2]}')
            """
        cursor.execute(query)


def fill_apperance():
    for i in range(len(data)):
        query = f"""
            INSERT INTO appearance (animal_type_id, breed_id, color1, color2)
            VALUES ('{i+1}' ,'{i+1}', '{data[i][5]}', '{data[i][6]}')
            """
        cursor.execute(query)


def fill_outcome_program():
    for i in range(len(data)):
        query = f"""
            INSERT INTO outcome_program (outcome_subtype, outcome_type)
            VALUES ('{data[i][8]}', '{data[i][9]}')
            """
        cursor.execute(query)


def fill_outcome_date():
    for i in range(len(data)):
        query = f"""
                    INSERT INTO outcome_date (outcome_month, outcome_year)
                    VALUES ('{data[i][10]}', '{data[i][11]}')
                    """
        cursor.execute(query)


with sqlite3.connect("animal1.db") as connection:
    cursor = connection.cursor()
    query = """
            SELECT * FROM animals
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        age_upon = row[1]
        animal_id = row[2]
        animal_type = row[3]
        name = row[4]
        breed = str(row[5])
        first = row[6]
        second = row[7]
        date_of_birth = row[8]
        sub_type = row[9]
        type_ = row[10]
        month = row[11]
        year = row[12]
        tuple_ = (age_upon, animal_id, animal_type, name, breed, first, second, date_of_birth, sub_type,
                  type_, month, year)
        data.append(tuple_)
    fill_apperance()
    fill_outcome_date()
    fill_outcome_program()
    fill_animal_types()
    fill_animals_task()
    fill_animal_breeds()
