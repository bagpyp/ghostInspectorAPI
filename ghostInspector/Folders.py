
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:35:12 2020
@author: Robbie Cunningham

Here are the available calls for this resource:
['list_folders', 'get_folder', 'create_folder', 'update_folder', 'list_folder_suites']
"""

apiKey = '5ddf30aae9f01cae849e738479727c2dfd42b072'
import requests

# Folders, List Folders
def list_folders():
    """
    Fetch an array of the folders in your account
    """
    res = requests.get('https://api.ghostinspector.com/v1/folders/?apiKey='+apiKey)
    return res


# Folders, Get Folder
def get_folder(folderId):
    """
    Fetch a single folder by folderId
    """
    res = requests.get('https://api.ghostinspector.com/v1/folders/'+folderId+'/?apiKey='+apiKey)
    return res


# Folders, Create Folder
def create_folder():
    """
    name
Name for the new folder
organization
The ID of the organization this folder should be within


curl example:
POST Request with JSON body:
curl -H 'Content-Type: application/json' -X POST -d "{"name":"Fancy Fresh Folder", organization: "5a1b419ae40144279f9ac680"}" 'https://api.ghostinspector.com/v1/folders/?apiKey=<apiKey>"'

example Response
{
  "code": "SUCCESS",
  "data": {
    "_id": "5aed177226a8722dad009e39",
    "organization": "547fb82d92423992d52a4fea",
    "name": "Fancy Fresh Folder"    
  }
}
    """
    res = requests.post('https://api.ghostinspector.com/v1/folders/?apiKey='+apiKey)
    return res


# Folders, Update Folder
def update_folder(folderId):
    """
    JSON Body

name: Name of the folder
    """
    res = requests.post('https://api.ghostinspector.com/v1/folders/'+folderId+'/?apiKey='+apiKey)
    return res


# Folders, List Folder Suites
def list_folder_suites(folderId):
    """
    Fetch an array of all the suites in a folder
    """
    res = requests.get('https://api.ghostinspector.com/v1/folders/'+folderId+'/suites/?apiKey='+apiKey)
    return res

