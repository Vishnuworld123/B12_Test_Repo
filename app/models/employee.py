from app import db


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(200))
    salary = db.Column(db.Float)
    address = db.Column(db.String(250))
    is_deleted = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "salary": self.salary,
            "address": self.address,
            "is_deleted": self.is_deleted,
        }
