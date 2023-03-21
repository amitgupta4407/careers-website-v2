from flask import Flask,render_template,jsonify,request

from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

# JOBS=[
# 	{
# 		"id": 1,
# 		"title": "Data Analyst",
# 		"location": "Bengaluru, India",
# 		"salary": "Rs. 10,00,000"
# 	},
# 	{
# 		"id": 2,
# 		"title": "Data Scientist",
# 		"location": "Delhi, India",
# 		"salary": "Rs. 15,00,000"
# 	},
# 	{
# 		"id": 3,
# 		"title": "Frontend Engineer",
# 		"location": "Remote",
# 		"salary": "Rs. 12,00,000"
# 	}
# ]




@app.route("/")
def hello_world():
	jobs = load_jobs_from_db()
	return render_template(
		'home.html',
	   jobs =jobs)


@app.route("/api/jobs")
def list_jobs():
	jobs = load_jobs_from_db()
	return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
	job = load_job_from_db(id)
	# return jsonify(job)
	
	if not job:
		return "NOT FOUND", 404
	
	return render_template('jobpage.html',job = job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
	# data = request.args #expect data from url 
	data = request.form #expect data from form
	job = load_job_from_db(id)
	# return jsonify(data)
	add_application_to_db(id, data)
	return render_template('application_submitted.html', 
						 application=data,
						 job=job)


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug = True)


