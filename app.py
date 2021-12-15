from openweathermap import *
from main import clothes_for_location
from flask import *
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html", form_data={"clothes": []})
    if request.method == 'POST':
        form_data = request.form
        return render_template('index.html', form_data={"clothes": clothes_for_location(request.form["location"])})
