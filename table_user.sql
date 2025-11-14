CREATE TABLE users (
  id serial primary key,
  name VARCHAR(100)
);


-- DROP TABLE users_log;
CREATE TABLE users_log (
  id serial primary key,
  user_id INT,
  user_name VARCHAR(100),
  action TEXT,
  time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
)

INSERT INTO TABLE users
