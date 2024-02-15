DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS students;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  start_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

-- Sample data
INSERT INTO cohorts (name, start_date) VALUES ('Red', '01/01/2022');
INSERT INTO cohorts (name, start_date) VALUES ('Blue', '01/04/2022');
INSERT INTO cohorts (name, start_date) VALUES ('Green', '01/07/2022');

INSERT INTO students (name, cohort_id) VALUES ('Bill', 1);
INSERT INTO students (name, cohort_id) VALUES ('Jill', 3);
INSERT INTO students (name, cohort_id) VALUES ('Ted', 2);
INSERT INTO students (name, cohort_id) VALUES ('Phil', 2);
INSERT INTO students (name, cohort_id) VALUES ('Wendy', 1);
INSERT INTO students (name, cohort_id) VALUES ('Amos', 3);