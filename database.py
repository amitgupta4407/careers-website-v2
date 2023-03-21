
import os
from sqlalchemy import create_engine, text
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(
	db_connection_string,
	connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)


def load_jobs_from_db():
	with engine.connect() as conn:
		result = conn.execute(text("select * from jobs"))
		jobs = []
		for row in result.all():
			jobs.append(dict(row._mapping))
		return jobs

def load_job_from_db(val):
	with engine.connect() as conn:
		result = conn.execute(text(
			f"select * from jobs where id = {val}"
		))
	rows = result.all()
	if len(rows)==0:
		return None
	return dict(rows[0]._mapping)

def add_application_to_db(id, data):
  with engine.connect() as conn:
    query = text(f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ('{id}', '{data['full_name']}',' {str(data['email'])}', '{data['linkedin_url']}','{data['education']}' ,'{data['work_experience']}','{data['resume_url']}')")

    conn.execute(query)
# with engine.connect() as conn:
# 	result = conn.execute(text("select * from jobs"))
# 	print("type(result): ", type(result))
# 	result_all = result.all()
# 	print("type(result_all()): ", type(result.all()))
# 	first_result = result_all[0]
# 	print("type(first_result): ", type(first_result))
# 	first_result_dict = (result_all[0]._mapping)
# 	print(type(first_result_dict))
# 	print(dict(first_result_dict))
	