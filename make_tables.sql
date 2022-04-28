create table animal_types (
    id integer primary key autoincrement,
    animal_type varchar(20)
    );

create table animal_breeds (
    id integer primary key autoincrement,
    breed varchar(40)
    );


create table appearance (
    id integer primary key autoincrement,
    animal_type_id integer,
    breed_id integer,
    color1 varchar(20) NOT NULL,
    color2 varchar(20),
    FOREIGN KEY (animal_type_id) REFERENCES animal_types(id),
    FOREIGN KEY (breed_id) REFERENCES animal_breeds(id)
   );

create table outcome_date(
    id integer primary key autoincrement,
    outcome_month integer,
    outcome_year integer
);

create table outcome_program(
    id integer primary key autoincrement,
    outcome_subtype varchar(20),
    outcome_type varchar(20)
);

create table animals_task (
    id integer primary key autoincrement,
    age_upon_outcome varchar(20),
    animal_id varchar(20) NOT NULL ,
    name varchar(20),
    appearance_id integer,
    date_of_birth date,
    outcome_program_id integer,
    outcome_date_id integer,
    FOREIGN KEY (appearance_id) REFERENCES appearance(id),
    FOREIGN KEY (outcome_date_id) REFERENCES  outcome_date(id),
    FOREIGN KEY (outcome_program_id) REFERENCES outcome_program(id)
)
