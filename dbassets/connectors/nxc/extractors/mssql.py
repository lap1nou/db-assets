import sqlite3
from dbassets.db_api.creds import add_credential

class NXC_MSSQL_Extractor:
    def __init__(self, db_file_path, kp):
        self.db_file_path = db_file_path
        self.kp = kp

    def extract_and_add_credentials(self):
        try:
            conn = sqlite3.connect(self.db_file_path)
            cursor = conn.cursor()

            query = "SELECT domain, username, password, credtype FROM users"
            cursor.execute(query)
            rows = cursor.fetchall()
            counter = 0

            for row in rows:
                domain, username, password, credtype = row
                if credtype == 'plaintext':
                    add_credential(self.kp, username=username, password=password, domain=domain)
                    counter = counter + 1
                elif credtype == 'hash':
                    if ':' in password:
                        password = password.split(':')[1]
                    add_credential(self.kp, username=username, hash=password, domain=domain)
                    counter = counter + 1
            
            print(f"Synced {counter} MSSQL credentials")

            conn.close()
        except Exception as e:
            print(f"Error extracting from {self.db_file_path}: {e}")
