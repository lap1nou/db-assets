import sqlite3
from dbassets.db_api.creds import add_credential

class NXC_SSH_Extractor:
    def __init__(self, db_file_path, kp):
        self.db_file_path = db_file_path
        self.kp = kp

    def extract_and_add_credentials(self):
        try:
            conn = sqlite3.connect(self.db_file_path)
            cursor = conn.cursor()

            query = """
                SELECT c.username, c.password, c.credtype, h.host 
                FROM credentials c
                JOIN loggedin_relations lr ON c.id = lr.credid
                JOIN hosts h ON lr.hostid = h.id
            """
            
            cursor.execute(query)
            rows = cursor.fetchall()
            counter = 0

            for row in rows:
                username, password, credtype, host = row
                if credtype == 'plaintext':
                    add_credential(self.kp, username=username, password=password, domain=host)
                    counter = counter + 1
                elif credtype == 'hash':
                    if ':' in password:
                        password = password.split(':')[1]
                    add_credential(self.kp, username=username, hash=password, domain=host)
                    counter = counter + 1
            
            print(f"Synced {counter} SSH credentials")

            conn.close()
        except Exception as e:
            print(f"Error extracting from {self.db_file_path}: {e}")
