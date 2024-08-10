import os
from .config import FILE_TYPES


def scan_files(directory):
    files_to_upload = {
        'images': [],
        'media': [],
        'documents': []
    }

    for root, dirs, files in os.walk(directory):
        for file in files:
            ext = file.split('.')[-1].lower()
            if ext in FILE_TYPES['images']:
                files_to_upload['images'].append(os.path.join(root, file))
            elif ext in FILE_TYPES['media']:
                files_to_upload['media'].append(os.path.join(root, file))
            elif ext in FILE_TYPES['documents']:
                files_to_upload['documents'].append(os.path.join(root, file))

    return files_to_upload
