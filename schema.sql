DROP TABLE IF EXISTS fruit;

CREATE TABLE fruit (
  id SERIAL PRIMARY KEY,
  genus VARCHAR(255),
  name VARCHAR(255),
  family VARCHAR(255),
  order_name VARCHAR(255),
  carbohydrate INTEGER,
  protein INTEGER,
  fat INTEGER,
  calories INTEGER,
  sugar INTEGER
);