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

query_string = """
CREATE TABLE applications(
	id INT NOT NULL AUTO_INCREMENT,
 	job_id INT NOT NULL,
	full_name VARCHAR(250) NOT NULL,
	email VARCHAR(250) NOT NULL,
	linkedin_url VARCHAR(500),
	education VARCHAR(2000),
	work_experience VARCHAR(2000),
	resume_url VARCHAR(500),
 	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY(id)
)
"""
query_string = """SHOW TABLES"""
query_string = """SELECT * FROM applications"""
def execute_query():
	with engine.connect() as conn:
		result = conn.execute(text(query_string))
		print(result.all())
execute_query()