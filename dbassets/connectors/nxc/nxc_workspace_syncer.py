import os
from dbassets.db_api.creds import add_credential
from dbassets.connectors.nxc.extractors.smb import NXC_SMB_Extractor
from dbassets.connectors.nxc.extractors.ftp import NXC_FTP_Extractor
from dbassets.connectors.nxc.extractors.mssql import NXC_MSSQL_Extractor
from dbassets.connectors.nxc.extractors.ssh import NXC_SSH_Extractor
from dbassets.connectors.nxc.extractors.winrm import NXC_WINRM_Extractor
from dbassets.connectors.nxc.extractors.ldap import NXC_LDAP_Extractor
from dbassets.connectors.nxc.extractors.rdp import NXC_RDP_Extractor
from dbassets.connectors.nxc.extractors.nfs import NXC_NFS_Extractor
from dbassets.connectors.nxc.extractors.vnc import NXC_VNC_Extractor

class NXCWorkspaceSyncer:
    def __init__(self, kp, workspaces_dir='~/.nxc/workspaces/'):
        self.workspaces_dir = os.path.expanduser(workspaces_dir)
        self.kp = kp
        self.db_files = {
            'smb.db': NXC_SMB_Extractor,
            'ftp.db': NXC_FTP_Extractor,
            'mssql.db': NXC_MSSQL_Extractor,
            'ssh.db': NXC_SSH_Extractor,
            'winrm.db': NXC_WINRM_Extractor,
            'ldap.db': NXC_LDAP_Extractor,
            'rdp.db': NXC_RDP_Extractor,
            'nfs.db': NXC_NFS_Extractor,
            'vnc.db': NXC_VNC_Extractor
        }
        # self.db_files = [
        #     
        #     'vnc.db', 'wmi.db'
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