from flask import Flask, render_template , jsonify

app = Flask(__name__)
JOBS = [
  {
    "id":"1",
    "title":"Data Analyst",
    "location":"Banglore",
    "salary":"$12,000"
  },
  {
    "id":"2",
    "title":"Data scientist",
    "location":"Riverdale",
    "salary":"$13,200"
  },
  {
    "id":"3",
    "title":"front-end develpor",
    "location":"new york",
    "salary":"$22,200"
  },
  {
    "id":"4",
    "title":"python develpor",
    "location":"los angels",
    "salary":"$19,200"
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS , company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':

  app.run(host="0.0.0.0", debug=True)
