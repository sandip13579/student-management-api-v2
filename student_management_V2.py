from fastapi import FastAPI
from pydantic import BaseModel

import sqlite3

app = FastAPI()

conn = sqlite3.connect("SIT_students.db", check_same_thread=False)

class student(BaseModel):
    SIC:str
    name:str
    roll_no:int

cursor = conn.cursor()


# cursor.execute(
#     """
#     INSERT INTO students("SIC","name","roll_no")
#     VALUES("25BCSA50","vomesh",50)
#     """
# )


@app.post("/students")
def add_students(new_student:student):
    cursor.execute(
        """
          INSERT INTO students(SIC,name,roll_no)
          VALUES(?,?,?)
        """,(
            new_student.SIC,
            new_student.name,
            new_student.roll_no
        )
    )
    conn.commit()

    return {"Message":"Student added successfully"}

@app.get("/students")
def get_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    return rows

@app.put("/students/UPDATE/{student_name}")
def update_name(student_name:str,updated_List:student):
    
    cursor.execute(
        """
        UPDATE students
        SET SIC = ?,name = ?,roll_no = ?
        WHERE name = ?
        """,(
            updated_List.SIC,
            updated_List.name,
            updated_List.roll_no,
            student_name
        )
    )
    conn.commit()

    return {"Message":" Updated student name successfully"}

@app.delete("/students/DELETE/{student_SIC}")
def delete_SIC(student_SIC: str):

    cursor.execute(
        """
        DELETE FROM students
        WHERE SIC = ?
        """,
        (student_SIC,)
    )

    print("Rows deleted:", cursor.rowcount)

    conn.commit()

    return {"Message": "Deleted Student SIC successfully"}