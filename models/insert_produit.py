import pyodbc


def insert_produit(nom, prix, nombre):
     conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
     cursor = conn.cursor()
     cursor.execute("""
                    INSERT INTO Produit(nom_produit, prix_produit, nombre_produit) 
                    VALUES
                    (%snom, %sprix, %snombre)
			""")
     cursor.commit()