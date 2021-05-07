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

@main.route('/getuser/<string:course_title>')
def getuser(course_title):
	try:
		course_title= course_title.upper()
		course = Course.query.filter_by(title=course_title).first()
		users = course.course_subscribers
		students_list = []
		for student in users:
			students = {}
			students['firstname'] = student.firstname
			students['lastname'] = student.lastname
			students['reg_no'] = student.regnumber
			#convert the students image stored in bytes to str so it can be passable with json on line 41
			students['img'] = student.image.decode('utf-8') 
			students_list.append(students)
		if students_list == []:
			return 'No student registered!'
		else:
			return json.dumps(students_list)
	except AttributeError:
		return 'Course not found!'

#getting only students in that department registered can be done by inserting the id into the routing channel


