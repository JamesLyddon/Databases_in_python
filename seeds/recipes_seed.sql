-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;

-- Then, we recreate them
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name text,
  avg_cooking_time int,
  rating int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (name, avg_cooking_time, rating) VALUES ('Pasta', 10, 4);
INSERT INTO recipes (name, avg_cooking_time, rating) VALUES ('Sandwich', 2, 3);
INSERT INTO recipes (name, avg_cooking_time, rating) VALUES ('Soup', 15, 2);


