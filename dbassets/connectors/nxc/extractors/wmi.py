import sqlite3
from dbassets.db_api.creds import add_credential

class NXC_WMI_Extractor:
    def __init__(self, db_file_path, kp):
        self.db_file_path = db_file_path
        self.kp = kp

    def extract_and_add_credentials(self):
        try:
            conn = sqlite3.connect(self.db_file_path)
            cursor = conn.cursor()

            query = "SELECT username, password FROM credentials"
            cursor.execute(query)
            rows = cursor.fetchall()
            counter = 0

            for row in rows:
                username, password = row
                add_credential(self.kp, username=username, password=password)
                counter = counter + 1
            
            print(f"Synced {counter} WMI credentials")

            conn.close()
        except Exception as e:
            print(f"Error extracting from {self.db_file_path}: {e}")
