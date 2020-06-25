#!/usr/bin/python3
"""
    Just a routine practice: zip the logs folder for the Linux OS.
"""
import shutil

dir_to_zip = '/var/log'
output_filename = 'os_logs'

shutil.make_archive(output_filename, 'zip', dir_to_zip)
