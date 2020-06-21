#!/usr/bin/python3
"""
    Just a routine practice: Getting familiar with the os module, specifically listing files with walk.
"""
import os


def list_pwd(current_path):
    for directory, subfolders, files in os.walk(current_path):
        if len(subfolders):
            for subfolder in subfolders:
                print(os.path.join(directory, subfolder))
        if len(files):
            for file in files:
                print(os.path.join(directory, file))


list_pwd(os.getcwd())
