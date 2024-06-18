""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/company/create", methods=['POST'])
def post_job():
    """ recieves post requests to add new task """
    data = request.get_json()
    try:
        db_helper.post_job(data['job_title'], data['salary'], data['location'], data['job_type'], data['company_id'], data["skill_names"])
        result = {'success': True, 'response': 'Done'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/company/postings", methods=['GET'])
def fetch_job_postings():
    company_id = request.args.get('company_id')
    count = request.args.get('count')
    items = db_helper.fetch_job_postings(company_id, count)
    return jsonify(items)

@app.route("/recruiter/login", methods=['POST'])
def recruiter_login():
    """ returns login status """
    data = request.get_json()
    try:
        result = db_helper.recruiter_login(data["recruiter_id"], data["pwd"])
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return result
    
@app.route("/company/view_applications", methods=['GET'])
def fetch_company_applications():
    company_id = request.args.get('company_id')
    count = request.args.get('count')
    try:
        result = db_helper.fetch_company_applications(company_id, count)
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return result

@app.route("/company/decide", methods=['PUT'])
def decide():
    data = request.get_json()
    try:
        db_helper.decide(data["student_id"], data["job_id"], data["status"])
        result = {'success': True, 'response': 'Status updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/student/job_openings", methods=['GET'])
def fetch_job_openings():
    student_id = request.args.get('student_id')
    count = request.args.get('count')
    try:
        result = db_helper.fetch_job_openings(student_id, count)
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return result

@app.route("/student/job_openings_by_name", methods=['GET'])
def fetch_job_openings_by_name():
    student_id = request.args.get('student_id')
    company_name = request.args.get('company_name')
    try:
        result = db_helper.fetch_job_openings_by_name(student_id,company_name)
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return result

@app.route("/student/applied", methods=['GET'])
def fetch_jobs_applied():
    student_id = request.args.get('student_id')
    count = request.args.get('count')
    try:
        result = db_helper.fetch_jobs_applied(student_id, count)
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return result

@app.route("/student/login",  methods=['POST'])
def student_login():
    """ returns login status """
    data = request.get_json()
    try:
        result = db_helper.student_login(data["student_id"], data["pwd"])
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)


@app.route("/student/apply", methods=['POST'])
def apply():
    data = request.get_json()
    try:
        db_helper.apply(data["student_id"], data["job_id"])
        result = {'success': True, 'response': 'Application added'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/company/delete/<int:job_id>", methods=['DELETE'])
def delete_job_posting(job_id):
    data = request.get_json()
    try:
        db_helper.delete_job_posting(job_id)
        result = {'success': True, 'response': 'Removed job_role'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/company/close", methods=['PUT'])
def close_job():
    data = request.get_json()
    try:
        db_helper.close_job(data["job_id"])
        result = {'success': True, 'response': 'Job posting closed'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/company/stats/<int:company_id>", methods=['GET'])
def stats(company_id):
    try:
        result = db_helper.stats(company_id)
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/student/jobs_by_skills/<int:student_id>", methods=['GET'])
def fetch_job_by_skills(student_id):
    try:
        result = db_helper.fetch_job_by_skills(student_id)
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return result

@app.route("/company/students_by_skills/<int:job_id>", methods=['GET'])
def fetch_student_by_skills(job_id):
    try:
        result = db_helper.fetch_student_by_skills(job_id)
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return result