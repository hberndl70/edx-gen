import os
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from __AWS__ import aws_access_key_id, aws_secret_access_key
import __CONSTS__

#--------------------------------------------------------------------------------------------------
# get all the sub folders in a folder
# return the folder names and folder paths, like this 
# [[folder_name, folder_path], [folder_name, folder_path], [folder_name, folder_path]...]
def getSubFolders(folder_path):
    folders = []
    files_and_folders = os.listdir(folder_path)
    for file_or_folder in files_and_folders:
        path = os.path.join(folder_path, file_or_folder)
        if (not os.path.isfile(path)):
            folders.append([file_or_folder, path])
    folders.sort()
    return folders
    
#--------------------------------------------------------------------------------------------------
# get all the files in a folder
# return a list of file names and file paths, as a pair
# [[file_name, file_path], [file_name, file_path], [file_name, file_path] ...]
def getFiles(folder_path):
    files = []
    files_and_folders = os.listdir(folder_path)
    for file_or_folder in files_and_folders:
        path = os.path.join(folder_path, file_or_folder)
        if (os.path.isfile(path)):
            files.append([file_or_folder, path])
    files.sort()
    return files

#--------------------------------------------------------------------------------------------------
# upload a file to the s3 answers bucket
def upload_s3_answer(file_name, object_name=None):
    upload_s3(file_name, __CONSTS__.S3_ANSWERS_BUCKET, object_name)
    
# upload a file to the s3 examples bucket
def upload_s3_example(file_name, object_name=None):
    upload_s3(file_name, __CONSTS__.S3_EXAMPLES_BUCKET, object_name, {'ACL': 'public-read'})

# upload a file to an s3 answers bucket
def upload_s3(file_name, bucket, object_name=None, extra=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    session = Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3_client = session.client('s3')
    try:
        if extra == None:
            response = s3_client.upload_file(file_name, bucket, object_name)

        else:
            response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=extra)

    except ClientError as e:
        print(e)
        return False
        
    return True
    
#--------------------------------------------------------------------------------------------------
