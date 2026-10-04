import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Student Management System")
DEBUG = os.getenv("DEBUG", "True")
MAX_STUDENTS = os.getenv("MAX_STUDENTS", "100")