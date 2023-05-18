from flask import Flask, render_template, jsonify

app = Flask(__name__)


print(__name__)

JOBS =[
  {
    'id':1,
     'title': 'Data Analyst',
     'location':'Hyderabad',
    'salary': 'Rs 1'
    
  },
  {
    'id':2,
     'title': 'Data Engineer',
     'location':'Bangalore',
    'salary': 'Rs 2'
  
    
  },
  {
    'id':3,
     'title': 'Data Scientist',
     'location':'Hyderabad',
    'salary': 'Rs 30'
    
  }
  
]

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)

