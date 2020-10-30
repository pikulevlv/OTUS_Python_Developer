from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from werkzeug.exceptions import BadRequest
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

employee_blueprint_app = Blueprint("employee_app", __name__)

STAFF = {
    1: ['Sveta', 'senior developer'],
    2: ['Igor', 'PM'],
    3: ['Andrey', 'consultant'],
    4: ['Radj', 'developer'],
    5: ['Jacob', 'middle developer'],
}

@employee_blueprint_app.route("/")
def employee_list():
    return render_template("employees/employee_index.html", staff=STAFF)

@employee_blueprint_app.route("/<int:employee_id>/", methods=['GET', 'DELETE'])
def staff_info(employee_id: int):
    try:
        staff_name = STAFF[employee_id][0]
        staff_role = STAFF[employee_id][1]
    except KeyError:
        raise BadRequest(f"Invalid staff id #{employee_id}")
    if request.method == 'DELETE':
        STAFF.pop(employee_id)
        return jsonify(ok=True)
    return render_template(
        'employees/staff_info.html',
        employee_id=employee_id,
        staff_name=staff_name,
        staff_role=staff_role
    )

class NameRoleForm(FlaskForm):
    name = StringField('Enter name: ', validators=[Required()])
    role = StringField('Enter role: ', validators=[Required()])
    submit = SubmitField('Hair')

@employee_blueprint_app.route("/add_staff/", methods=['POST', 'GET'])
def add_staff():
    form = NameRoleForm()
    if form.validate_on_submit():
        try:
            staff_num = max(STAFF.keys()) + 1
        except:
            staff_num = 1
        data = [form.name.data, form.role.data]
        STAFF[staff_num]= data
        return redirect(url_for("employee_app.employee_list"))
    return render_template("employees/add_staff.html", form=form)

