import os
import pysftp

path_to_watch = "C:/Users/nerdmaster/Desktop/PCAP"
print('Your folder path is"',path_to_watch,'"')

old = os.listdir(path_to_watch)
print(old)

while True:
    new = os.listdir(path_to_watch)
    if len(new) > len(old):
        newfile = list(set(new) - set(old))
        print(newfile[0])
        old = new




        extension = os.path.splitext(path_to_watch + "/" + newfile[0])[1]
        if extension == ".pcap":



            
            print("Do somewith with " + extension)
            with pysftp.Connection('hostname', username='me', password='secret') as sftp:

                with sftp.cd('/allcode'):           # temporarily chdir to allcode
                    sftp.put('/pycode/filename')  	# upload file to allcode/pycode on remote
                    sftp.get('remote_file')         # get a remote file


            continue
        else:
            continue            
    else:
        continue
