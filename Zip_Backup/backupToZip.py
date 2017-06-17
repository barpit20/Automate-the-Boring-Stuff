import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    Exis=True
    num=1
    while Exis:
        zipName=os.path.basename(folder)+'_'+num
        if not os.path.exists(zipName):
            break
        num+=1
    backupZip = zipfile.ZipFile(zipName, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip')
                continue   
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()