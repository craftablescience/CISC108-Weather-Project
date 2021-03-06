from main import *
from flask import *
app = Flask(__name__)


def get_background_filename(data):
    background_filename = "backgrounds/"
    background_filename += "daytime" if data["sys"]["sunrise"] < data["dt"] < data["sys"]["sunset"] else "nighttime"
    background_filename += "_"
    if if_snowing(data):
        background_filename += "snowy"
    elif if_raining(data):
        background_filename += "rainy"
    elif if_cloudy(data):
        background_filename += "cloudy"
    else:
        background_filename += "default"
    background_filename += ".jpg"
    return background_filename


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html",
                               clothes=[],
                               background="backgrounds/default.jpg",
                               display_clothing="display: none;")

    if request.method == 'POST':
        data = find_weather_location(request.form["location"])
        return render_template('index.html',
                               clothes=clothes_for_location(request.form["location"]),
                               background=get_background_filename(data),
                               display_clothing="")

app.run()