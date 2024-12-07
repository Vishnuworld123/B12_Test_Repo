import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://root:root@localhost/emp_db_b12"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
