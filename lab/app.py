from databases import *
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')
	else:
		add_student(request.form['student_name'],
			request.form['student_year'], request.form['finishedlab'])
		return render_template('add.html')

@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_stu(student_id):
	if request.method == 'POST':
		delete_student_id(student_id)
		return(redirect(url_for('home')))


@app.route('/edit/<int:student_id>',methods=['POST','GET'])
def edit_stu(student_id):
	if request.method=='POST':
		student=query_by_id(student_id)
		update_lab_status(student.name,request.form['finishedlab'])
		return(redirect(url_for('display_student', student_id=student_id)))
	if request.method=='GET':
		return render_template('edit.html')

app.run(debug=True)