import sqlite3
from flask import Flask

app = Flask(__name__)
content_heading = ["id", "age_upon_outcome", "animal_id",
                   "animal_type", "name", "breed", "color1", "color2",
                   "date_of_birth", "outcome_subtype", "outcome_type",
                   "outcome_month", "outcome_year"]

def get_info_from_db(id):
    result_list = []
    with sqlite3.connect("animal1.db") as connection:
        cursor = connection.cursor()
        query = (f"""
                SELECT animals_task.id, age_upon_outcome, animal_id, at.animal_type,
                       name, ab.breed, a.color1, a.color2, date_of_birth,
                        op.outcome_subtype, op.outcome_type, od.outcome_month, od.outcome_year
                FROM animals_task
                INNER JOIN appearance a on a.id = animals_task.appearance_id
                INNER JOIN animal_breeds ab on ab.id = a.breed_id
                INNER JOIN animal_types at on a.animal_type_id = at.id
                INNER JOIN outcome_program op on animals_task.outcome_program_id = op.id
                INNER JOIN outcome_date od on animals_task.outcome_date_id = od.id
                WHERE animals_task.id = '{id}'
                  """)
        cursor.execute(query)
        result = cursor.fetchall()
        for item in result:
            result_list.append(item)
        return result_list


@app.route("/<int:id>")
def show_info(id):
    content = ""
    a = get_info_from_db(id)
    for i in range(len(a[0])):
        content = content + str(f"<p><strong>{content_heading[i]}</strong>:  {a[0][i]}</p>")
    return content

app.run()