#!/usr/bin/python3
"""
    Just a routine practice: tar the logs folder for the Linux OS.
"""
import shutil

dir_to_tar = '/var/log'
output_filename = 'os_logs'

shutil.make_archive(output_filename, 'tar', dir_to_tar)
