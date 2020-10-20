from flask import Blueprint, render_template
from werkzeug.exceptions import BadRequest

employee_blueprint_app = Blueprint("employee_app", __name__)

STAFF = {
    1: ['Sveta', 'developer'],
    2: ['Igor', 'PM'],
    3: ['Andrey', 'consultant'],
    4: ['Radj', 'developer'],
}

@employee_blueprint_app.route("/")
def employee_list():
    return render_template("employees/employee_index.html", staff=STAFF)

@employee_blueprint_app.route("/<int:employee_id>/")
def staff_info(employee_id: int):
    try:
        staff_name = STAFF[employee_id][0]
        staff_role = STAFF[employee_id][1]
    except KeyError:
        raise BadRequest(f"Invalid product id #{employee_id}")
    return render_template(
        'employees/staff_info.html',
        employee_id=employee_id,
        staff_name=staff_name,
        staff_role=staff_role
    )