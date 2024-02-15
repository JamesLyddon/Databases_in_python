DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  author text,
  content text,
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

-- Sample data
INSERT INTO posts (title, content) VALUES ('Hot New Bands', '...a blog post about bands...');
INSERT INTO posts (title, content) VALUES ('My Favourite Films', '...a blog post about films...');


INSERT INTO comments (author, content, post_id) VALUES ('Bill', 'I love that band!', 1);
INSERT INTO comments (author, content, post_id) VALUES ('Jill', 'I hate those films!!11', 2);
INSERT INTO comments (author, content, post_id) VALUES ('Phil', 'Another Triumph!', 1);
INSERT INTO comments (author, content, post_id) VALUES ('Alice', 'Get a load of Roger Ebert over here...', 2);