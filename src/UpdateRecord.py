from src.DatabaseTools import DatabaseConnector


class UpdateRecord(DatabaseConnector):

    def update_record(self,newsalary,employee_id):
        cursor = self.connection.cursor()
        sql = "UPDATE tblemployee SET salary = %s WHERE employee_id = %s"
        val = (newsalary,employee_id)
        cursor.execute(sql,val)
        self.connection.commit()
        print(cursor.rowcount, "record(s) affected")