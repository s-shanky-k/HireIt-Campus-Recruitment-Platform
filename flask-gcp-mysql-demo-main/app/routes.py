""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/company/delete/<int:job_id>", methods=['POST'])
def delete_job_posting(job_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.delete_job_posting(job_id)
        result = {'success': True, 'response': 'Removed job_role'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


# @app.route("/edit/<int:task_id>", methods=['POST'])
# def update(task_id):
#     """ recieved post requests for entry updates """

#     data = request.get_json()

#     try:
#         if "status" in data:
#             db_helper.update_status_entry(task_id, data["status"])
#             result = {'success': True, 'response': 'Status Updated'}
#         elif "description" in data:
#             db_helper.update_task_entry(task_id, data["description"])
#             result = {'success': True, 'response': 'Task Updated'}
#         else:
#             result = {'success': True, 'response': 'Nothing Updated'}
#     except:
#         result = {'success': False, 'response': 'Something went wrong'}

#     return jsonify(result)


@app.route("/company/create", methods=['POST'])
def post_job():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.post_job(data['job_id'], data['job_title'], data['salary'], data['location'], data['job_type'], data['company_id'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/company/postings")
def homepage():
    """ returns rendered homepage """
    data = request.get_json()
    items = db_helper.fetch_job_postings(data["company_id"])
    return render_template("index.html", items=items)

@app.route("/student/job_openings")
def fetch_job_openings():
    """ returns available job openings """
    jobs = db_helper.fetch_job_openings()
    return jobs

@app.route("/student/job_openings_by_name")
def fetch_job_openings_by_name():
    """ returns available job openings """
    data = request.get_json()
    jobs = db_helper.fetch_job_openings_by_name(data["company_name"])
    return jobs

@app.route("/student/applied")
def fetch_jobs_applied():
    data = request.get_json()
    jobs = db_helper.fetch_jobs_applied(data["student_id"])
    return jobs