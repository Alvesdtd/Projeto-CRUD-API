from src.DatabaseTools import DatabaseConnector

class ReadData(DatabaseConnector):

    def read_data(self,empid):
        cursor = self.connection.cursor(buffered=True)
        sql = "select * from tblemployee where employee_id = %s"
        val = empid
        cursor.execute(sql, (val,))
        self.connection.commit()
        return cursor.fetchone()