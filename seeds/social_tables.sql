DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text,
  email text
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  view_count int,
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

-- Sample data
INSERT INTO users (name, email) VALUES ('Bill', 'bill@mail.com');
INSERT INTO users (name, email) VALUES ('Ben', 'ben@mail.com');

INSERT INTO posts (title, content, view_count, user_id) VALUES ('Bill Post 1', 'some post 1 content', 5, 1);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Ben Post 1', 'some post 1 content', 7, 2);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Bill Post 2', 'some post 2 content', 24, 1);
INSERT INTO posts (title, content, view_count, user_id) VALUES ('Ben Post 2', 'some post 2 content', 0, 2);