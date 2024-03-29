from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 20,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  },
  {
    'id': 5,
    'title': 'Software Engineer',
    'location': 'San Francisco, USA',
    'salary': '$200,000'
  }
]


@app.route('/')
def index():
  return render_template("home.html", jobs=JOBS)

@app.route('/api/jobs/')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=808080, debug=True)