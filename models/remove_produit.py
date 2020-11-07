import pyodbc


def remove_client(reference_id):
     conn = pyodbc.connect('DRIVER={/opt/microsoft/msodbcsql/lib64/libmsodbcsql-17.6.so.1.1}; SERVER=127.0.0.1; PORT=1433; DATABASE=VENTEDB; UID=SA; PWD=root18**; Trusted_Domain=domain.local;') 
     cursor = conn.cursor()
     cursor.execute("""
                    DELETE FROM Produit WHERE id_produit = %sreference_id
			""")
     cursor.commit()