import pyodbc

class requeste():
     
     def insert_client(self, nom, cin, adresse, password):
          self.conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          self.cursor = self.conn.cursor()
          self.cursor.execute("""
                        INSERT INTO Client(nom_client, cin_client, adresse_client, Password) 
                         VALUES
                         (%snom,%scin,%sadresse,%spassword)
                    """)
          self.cursor.commit()
     
     
     def remove_client(self, reference_id):
          self.conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          self.cursor = self.conn.cursor()
          self.cursor.execute("""
                         DELETE FROM Client WHERE id_client = %sreference_id
                    """)
          self.cursor.commit()
     
     
     def insert_produit(self, nom, prix, nombre):
          self.conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          self.cursor = self.conn.cursor()
          self.cursor.execute("""
                         INSERT INTO Produit(nom_produit, prix_produit, nombre_produit) 
                         VALUES
                         (%snom, %sprix, %snombre)
                    """)
          self.cursor.commit()
     
     
     def remove_produit(self, reference_id):
          self.conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          self.cursor = self.conn.cursor()
          self.cursor.execute("""
                         DELETE FROM Produit WHERE id_produit = %sreference_id
                    """)
          self.cursor.commit()
     
     
     def update_produit(self, nombre):
          self.conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          self.cursor = self.conn.cursor()
          self.cursor.execute("""
                         UPDATE Produit SET nombre_produit = %snombre
                    """)
          self.cursor.commit()