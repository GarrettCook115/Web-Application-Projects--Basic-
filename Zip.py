from zipfile import ZipFile, ZIP_DEFLATED

zip_path = './TkinterApp1 Executable.zip'
file_to_zip = './TkinterApp1 Executable.py'

with ZipFile(zip_path, 'w', ZIP_DEFLATED )as zip:
    zip.write(file_to_zip) 
