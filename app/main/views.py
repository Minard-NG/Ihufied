from datetime import datetime
from flask import render_template
from flask_login import login_required
from . import main


###################
#### ALL-VIEWS ####
###################
@main.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


