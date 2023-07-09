import sqlite3 as sql

def conect_db(name):
    try:
        con = sql.connect(f"{name}.db")
        return con,"Database connection established"
    except Exception as e:
        return None, f"Error connecting to database: {str(e)}"    

def create_cursor(con):
    try:
        c = con.cursor()
        return c, "Cursor created"
    except Exception as e:
        return None, f"Error creating cursor: {str(e)}"

class tabla:
    
    def __init__(self, name, campos):
        self.name = name
        self.campos = campos
        con, _ = conect_db("DataBase")
        cur, _ = create_cursor(con)
        fields_str = ', '.join(f'{campo} text' for campo in self.campos)
        cur.execute(f"CREATE TABLE IF NOT EXISTS {self.name} ({fields_str});")
        con.commit()
        con.close()

    def print(self):
        con, _ = conect_db("DataBase")
        cur, _ = create_cursor(con)
        try:
            cur.execute(f"""SELECT * FROM {self.name}""")
            data = cur.fetchall()
            for row in data:
                print(row)
            con.commit()
        except sql.Error as e:
            print(f"Error printing SQLite table: {e}")
        finally:
            if con:
                con.close()

    def consult(self, campo0):
        con, _ = conect_db("DataBase")
        cur, _ = create_cursor(con)
        try:
            cur.execute(f"""SELECT * FROM {self.name} WHERE {self.campos[0]} = ?""", (campo0,))
            data = cur.fetchall()
            return data,"Data consulted correctly"
        except sql.Error as e:
            return None,"Error consulting SQLite table: {e}"
        finally:
            if con:
                con.commit()
                con.close()

    def insert(self, data):
        existing_data = self.consult(data[self.campos[0]])
        if existing_data:
            print(f"El usuario {data['user']} ya existe en la base de datos. No se insertará el dato.")
            return
        fields_str = ', '.join(data.keys())
        values_str = ', '.join('?' for _ in data.values())
        con, _ = conect_db("DataBase")
        cur, _ = create_cursor(con)
        try:
            cur.execute(f"""INSERT INTO {self.name} ({fields_str}) VALUES ({values_str});""", tuple(data.values()))
            con.commit()
        except sql.Error as e:
            return None, f"Error inserting data into SQLite table: {e}"
        finally:
            if con:
                con.close()

    def delet(self,campo0):
        con, _ = conect_db("DataBase")
        cur, _ = create_cursor(con)
        try:
            cur.execute(f"""DELETE FROM {self.name} WHERE {self.campos[0]} = ?""", (campo0,))
            con.commit()
        except sql.Error as e:
            return None, f"Error deleting from SQLite table: {e}"
        finally:
            if con:
                con.close()
    
    def update(self, campo0, data):
        con, _ = conect_db("DataBase")
        cur, _ = create_cursor(con)
        try:
            for key, value in data.items():
                cur.execute(f"""UPDATE {self.name} SET {key} = ? WHERE {self.campos[0]} = ?""", (value, campo0))
            con.commit()
        except sql.Error as e:
            return None, f"Error updating SQLite table: {e}"
        finally:
            if con:
                con.close()

    def get_data(self):
        con, _ = conect_db("DataBase")
        cur, _ = create_cursor(con)
        try:
            cur.execute(f"""SELECT * FROM {self.name}""")
            data = cur.fetchall()
            return data,"Data consulted correctly"
        except sql.Error as e:
            return None,"Error consulting SQLite table: {e}"
        finally:
            if con:
                con.commit()
                con.close()
    
    def delet_duplicated(self):
        con, _ = conect_db("DataBase")
        cur, _ = create_cursor(con)
        try:
            cur.execute(f"""DELETE FROM {self.name} WHERE rowid NOT IN (SELECT min(rowid) FROM {self.name} GROUP BY {self.campos[0]});""")
            con.commit()
        except sql.Error as e:
            return None, f"Error deleting duplicated from SQLite table: {e}"
        finally:
            if con:
                con.close()