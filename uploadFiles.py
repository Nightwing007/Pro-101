import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                   
                path = os.path.join(root, filename)

                file_path = os.path.relpath(path, file_from)
                file_to = os.path.join(file_to, file_path)
    
                f = open(path, 'rb') 
                dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))

def main():
    access_token = 'oxfL7MshiJ0AAAAAAAAAAeDtJksQOaX_liUKO4lgrJlbUZ4cRIFWEHeJohR01oZD'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path: "))
    file_to = input("enter the dropbox path:- ") 

    transferData.upload_file(file_from,file_to)

main()