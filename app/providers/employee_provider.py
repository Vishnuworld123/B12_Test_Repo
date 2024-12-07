from app.dao.employee_dao import EmployeeDAO
import csv
from io import StringIO


class EmployeeProvider:
    @staticmethod
    def get_all_employees_p():
        return [
            emp.to_dict() for emp in EmployeeDAO.get_all_employees()
        ]  # list comprehension

    @staticmethod
    def create_employee_p(input_data):
        return EmployeeDAO.create_employee(
            input_data["name"],
            input_data["role"],
            input_data["salary"],
            input_data["address"],
        )

    @staticmethod
    def get_employee_by_id_p(emp_id):
        emp = EmployeeDAO.get_employee_by_id(emp_id)
        return emp.to_dict() if emp else None

    @staticmethod
    def update_employee_p(emp_id, input_data):
        emp = EmployeeDAO.update_employee(
            emp_id,
            nm=input_data.get("name"),
            role=input_data.get("role"),
            sal=input_data.get("salary"),
            addr=input_data.get("address"),
        )
        return emp.to_dict() if emp else None

    @staticmethod
    def get_employees_csv():
        """Generate CSV data for employees."""
        employees = EmployeeDAO.get_all_employees()
        output = StringIO()
        writer = csv.writer(output)

        # Write header
        writer.writerow(['ID', 'Name', 'Role', 'Salary', 'Is Deleted'])

        # Write employee records
        for emp in employees:
            writer.writerow([emp.id, emp.name, emp.role, emp.salary, emp.is_deleted])

        output.seek(0)
        return output