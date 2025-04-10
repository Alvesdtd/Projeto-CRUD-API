from src.DatabaseTools import DatabaseConnector


class InsertRecords(DatabaseConnector):

    def insert_data(self,empname,department,salary):
        cursor = self.connection.cursor()
        sql = "INSERT INTO tblemployee (empname,department,salary) VALUES (%s, %s, %s)"
        val = (empname, department,salary)
        cursor.execute(sql, val)
        self.connection.commit()