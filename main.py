from src.InsertRecords import InsertRecords
from src.DeleteData import DeleteData
from src.ReadData import ReadData
from src.UpdateRecord import UpdateRecord
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/get/{employee_id}")
def get_employee(employee_id):
    """
    This endpoint receives an employee ID and returns the employee's information.
    The actual database interaction is encapsulated within the EmployeeDBHandler class.
    """
    reader = ReadData()
    reader.connect()
    employee_data = reader.read_data(employee_id)

    if not employee_data:
        raise HTTPException(status_code=404, detail="Employee not found")

    #  Return the employee information
    return employee_data


# To declare a request body, you use Pydantic models
class Employee(BaseModel):
    employee_id: int | None = None
    empname: str | None = None
    department: str | None = None
    salary: float | None = None

@app.post("/insert")
def post_employee(emp: Employee):
    """
    This endpoint receives an employee ID and returns the employee's information.
    The actual database interaction is encapsulated within the EmployeeDBHandler class.
    """
    inserter = InsertRecords()
    inserter.connect()
    inserter.insert_data(emp.empname, emp.department, emp.salary)

    #  Return the employee information
    return {"message": "Employee inserted successfully."}


@app.delete("/delete/{employee_id}")
def delete_employee(employee_id):
    deleter = DeleteData()
    deleter.connect()
    deleter.delete_data(employee_id)

    return {"message": "Employee deleted successfully."}


@app.put("/put")
def update_employee(emp: Employee):
    updater = UpdateRecord()
    updater.connect()
    updater.update_record(emp.salary, emp.employee_id)

    return {"message": "Employee's salary has been updated successfully."}