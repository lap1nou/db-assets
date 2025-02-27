import os
from dbassets.db_api.creds import add_credential
from dbassets.connectors.nxc.nxc_smb_extractor import NXC_SMB_Extractor

class NXCWorkspaceSyncer:
    def __init__(self, kp, workspaces_dir='~/.nxc/workspaces/'):
        self.workspaces_dir = os.path.expanduser(workspaces_dir)
        self.kp = kp
        self.db_files = {
            'smb.db': NXC_SMB_Extractor
        }
        # self.db_files = [
        #     'ftp.db', 'ldap.db', 'mssql.db', 'nfs.db', 'rdp.db',
        #     'smb.db', 'ssh.db', 'vnc.db', 'winrm.db', 'wmi.db'
        # ]

    def sync(self):
        if os.path.exists(self.workspaces_dir):
            for workspace in os.listdir(self.workspaces_dir):
                workspace_path = os.path.join(self.workspaces_dir, workspace)
                if os.path.isdir(workspace_path):
                    self.process_workspace(workspace_path)
        else:
            print('No workspaces directory found at ~/.nxc/workspaces/')

    def process_workspace(self, workspace_path):
        for db_file, extractor_class in self.db_files.items():
            db_file_path = os.path.join(workspace_path, db_file)
            if os.path.isfile(db_file_path):
                extractor = extractor_class(db_file_path, self.kp)
                extractor.extract_and_add_credentials()
            else:
                print(f'Missing: {db_file}')