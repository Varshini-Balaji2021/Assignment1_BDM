import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL loaded:", DATABASE_URL is not None)

connection = psycopg2.connect(DATABASE_URL)

print("Connected successfully!")

connection.close()

print("Connection closed.")