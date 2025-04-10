# Employee Management API

This project is a simple RESTful API built using FastAPI for managing employee records. 
It supports operations to Create, Read, Update, and Delete (CRUD) employee data. 
The actual database operations are abstracted into separate modules for better code organization and reusability.

All data will be stored locally in a MySQL database.

## Features

- **Retrieve Employee (GET /get/{employee_id}):** Fetches employee details by ID.
- **Insert Employee (POST /insert):** Adds a new employee to the database.
- **Delete Employee (DELETE /delete/{employee_id}):** Removes an employee using their ID.
- **Update Salary (PUT /put):** Updates the salary of an existing employee.
