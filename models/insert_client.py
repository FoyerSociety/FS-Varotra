import pyodbc


def insert_client(nom, cin, adresse, password):
     conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
     cursor = conn.cursor()
     cursor.execute("""
                    INSERT INTO Client(nom_client, cin_client, adresse_client, Password) 
                    VALUES
                    (%snom,%scin,%sadresse,%spassword)
			""")
     cursor.commit()