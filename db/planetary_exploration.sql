DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS planets;

CREATE TABLE planets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  planet_class VARCHAR(255),
  native_species VARCHAR(255),
  rating INT
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  rating INT,
  comments TEXT,
  explored BOOLEAN,
  planet_id INT REFERENCES planets(id) ON DELETE CASCADE
);