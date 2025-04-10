from src.DatabaseTools import DatabaseConnector


class DeleteData(DatabaseConnector):

    def delete_data(self,empid):
        cursor = self.connection.cursor()
        try:
            empid = int(empid)  # Garante que seja um número
        except ValueError:
            print("Erro: O Employee ID deve ser um número.")
            return  # Quebra se falhar

        sql = "DELETE FROM tblemployee WHERE employee_id = %s"
        cursor.execute(sql, (empid,))  # Passa empid como tupla
        self.connection.commit()

        print(f"Registro com empid={empid} deletado com sucesso!")