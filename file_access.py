import zipfile
import os


def list_files_in_archive(archive):
    with zipfile.ZipFile(os.path.expanduser(archive)) as archive:
        return archive.namelist()
    

def read_single_file(archive, inner_file_name):
    with zipfile.ZipFile(os.path.expanduser(archive)) as archive:
        return archive.read(inner_file_name)