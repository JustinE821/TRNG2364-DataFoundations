import pandas as pd
from sqlalchemy import create_engine, text #this creates our database engine
from dotenv import load_dotenv #lets you read from our .env file
import psycopg2


print("hi")
engine = create_engine(
    "postgresql+psycopg2://postgres:1@localhost:5432/postgres",
    
)

#we can execute raw sql queries using the execute method on our engine
query = "SELECT student_id, first_name, last_name FROM student;"
student_df = pd.read_sql(query, engine)
print(student_df)


# new_student = pd.DataFrame(
#     {"first_name": ["Jayden"],
#      "last_name": ["Miller"],
#      "email": ["JMILL@email.com"],
#      "major": ["MB"]
#     }
# )

# #Th
# new_student.to_sql(name="student", con=engine, if_exists="append", index=False)


update_student = text("UPDATE student SET phone = '1236543' WHERE student_id = 7;")
#update statements need to be executed using a connection
with engine.connect() as connection:
    connection.execute(update_student)
    connection.commit()



#delete records 
delete_sql = text("DELETE FROM student WHERE email = 'JMILL@email.com'")

with engine.connect() as connection:
    connection.execute(delete_sql)
    connection.commit()




#Call our stored procedures
student_major = 'CS'
# result = f"CALL selectmajorstudents('{student_major}');"

# result_df = pd.read_sql('selectAllStudents()', engine)
# print(result_df)

# print(pd.read_sql(result, engine))
with engine.begin() as conn:   # begin() auto-commits or rolls back
    conn.execute(text("CALL updatemajorstudents(:major, :student_id)"), {"major": "BI", "student_id": 2})


student_id = 2
course_count_sql = f"SELECT first_name, last_name, get_course_count(student_id) FROM student;"

course_count_df = pd.read_sql(course_count_sql, engine)
print(course_count_df)