from app.models.employee import Employee
from app import db


class EmployeeDAO:
    @staticmethod
    def get_all_employees():
        return Employee.query.filter_by(is_deleted=False).all()

    @staticmethod
    def create_employee(nm, rol, sal, addr):
        new_emp = Employee(name=nm, role=rol, salary=sal, address=addr)
        db.session.add(new_emp)
        db.session.commit()
        return new_emp

    @staticmethod
    def get_employee_by_id(emp_id):
        # emp = Employee.query.get(emp_id) # True
        # if emp.is_deleted:
        #     return None
        return Employee.query.filter_by(
            id=emp_id, is_deleted=False
        ).first()  # record or None

    @staticmethod
    def update_employee(emp_id, nm=None, role=None, sal=None, addr=None):
        emp = Employee.query.filter_by(id=emp_id, is_deleted=False).first()
        if not emp:
            return None
        if nm:
            emp.name = nm
        if role:
            emp.role = role
        if sal:
            emp.salary = sal
        if addr:
            emp.address = addr
        db.session.commit()
        return emp

    # delete
    # fetch emp
    # if emp none: return none
    # emp.is_deleted=True
    # commit
