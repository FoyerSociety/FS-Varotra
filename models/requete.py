import pyodbc

class requeste():
     
     def insert_client(self, nom, cin, adresse, password):
          conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          cursor = conn.cursor()
          cursor.execute("""
                         INSERT INTO Client(nom_client, cin_client, adresse_client, Password) 
                         VALUES
                         (%snom,%scin,%sadresse,%spassword)
                    """)
          cursor.commit()
     
     
     def remove_client(self, reference_id):
          conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          cursor = conn.cursor()
          cursor.execute("""
                         DELETE FROM Client WHERE id_client = %sreference_id
                    """)
          cursor.commit()
     
     
     def insert_produit(self, nom, prix, nombre):
          conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          cursor = conn.cursor()
          cursor.execute("""
                         INSERT INTO Produit(nom_produit, prix_produit, nombre_produit) 
                         VALUES
                         (%snom, %sprix, %snombre)
                    """)
          cursor.commit()
     
     
     def remove_produit(self, reference_id):
          conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          cursor = conn.cursor()
          cursor.execute("""
                         DELETE FROM Produit WHERE id_produit = %sreference_id
                    """)
          cursor.commit()
     
     
     def update_produit(self, nombre):
          conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
          cursor = conn.cursor()
          cursor.execute("""
                         UPDATE Produit SET nombre_produit = %snombre
                    """)
          cursor.commit()