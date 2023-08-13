from sqlalchemy import create_engine
from sqlalchemy.sql import text
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


def single_job(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id= {id}")
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
