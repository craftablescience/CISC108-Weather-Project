from openweathermap import *
from flask import *
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html", form_data={})
    if request.method == 'POST':
        form_data = request.form
        return render_template('index.html', form_data=make_request(q=request.form["location"]))
