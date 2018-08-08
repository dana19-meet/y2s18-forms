from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/add', methods=['GET', 'POST'])
def add_stu_route():
	if request.method=='GET':
		return render_template('add.html')
	elif request.method=='POST':
		# add_student('dana',2,True)
		n=request.form['student_name']
		y=int(request.form['student_year'])
		add_student(n,y,False)
		return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

app.run(debug=True)
