#!/usr/bin/python3
"""
    Just a routine practice: unzip a .zip file.
"""
import shutil

output_dir = '/tmp/os_logs'
zip_filename = 'os_logs.zip'

shutil.unpack_archive(zip_filename,output_dir, 'zip')
