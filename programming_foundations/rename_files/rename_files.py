import os

#directory="C:\Downloads"
directory=r"C:\git\python-projects\programming_foundations\rename_files\prank"

def rename_files():
    #1 get file names from a folder
    #file_list = os.listdir(r"C:\git\python-projects\programming_foundations\rename_files\prank") #take string as a raw path and don't interpret it
    file_list = os.listdir(directory)  # take string as a raw path and don't interpret it
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    # make sure program's working directory is looking at the correct folder.
    #os.chdir(r"C:\git\python-projects\programming_foundations\rename_files\prank")
    os.chdir(directory)

    #2 for each file, rename filename
    translator = str.maketrans('','',"0123456789") #replace all numbers with nothing
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(translator))
        os.rename(file_name, file_name.translate(translator)) #rename the actual file
    os.chdir(saved_path) #change program working directory back to original directory

rename_files()