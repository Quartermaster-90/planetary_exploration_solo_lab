from flask import Flask, render_template

from controllers.planets_controller import planets_blueprint
# from controllers.unexplored_planets_controller import unexplored_planets_blueprint
# from controllers.explored_planets_controller import explored_planets_blueprint
from controllers.cities_controller import cities_blueprint

app = Flask(__name__)

app.register_blueprint(planets_blueprint)
app.register_blueprint(cities_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)