# README for Planetary Exploration app.

## Installation, testing and initialisation instructions

To install, download ZIP from repo and expand at your desired location. Then, in terminal, `cd` to the folder for `planetary_exploration`, and type `code .` to then open up in VSCode (or equivalent).

First, check database doesn't exist by typing `dropdb planetary_exploration`. Secondly, `createdb planetary_explortion` to create the database. Thirdly, to check contents are present in the database, run `psql -d planetary_exploration -f db/planetary_exploration.sql`. If successful, it'll show `DROP TABLE`/`CREATE TABLE`.

Unittesting is availble for the two class tyoes: **City** and **Planet**. To run the tests, type `python3 run_tests.py` which should return OK.

Run the `console.py` file to check the Python can detect information from the database.

To run the full app on a browswer, type the command `flask run`, at which point a local host address will appear which you can **COMMAND + click** onto which will automatically open the address up in your default browser. From here, you can use the functionaily currently availble in the app.

## Brief

The idea behind this app is to allow a user to track and log their adventures across the galaxy. This includes, but not limited to, planets they have explored or wish to explore, and cities within those planets they have either explored or wish to explore.

The user can log data such as the planet/city name, a rating for each, comments, and check whether they've been there or not, amongst other features (some to be implemented in a future version).

## Technology Used

* Python
* Flask with Jinja template render
* PostgreSQL with psycopg
* HTML
* CSS

## Screenshot Example

<img width="1336" alt="Screenshot 2023-06-28 at 16 24 33" src="https://github.com/Quartermaster-90/planetary_exploration_solo_lab/assets/132846070/b90da1bb-83f1-419a-aac7-ee537e4de9ba">
