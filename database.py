from sqlalchemy import create_engine,text
import os

connection_string = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for u in result.all():
      p = u._asdict()
      jobs.append(p)
    return jobs

