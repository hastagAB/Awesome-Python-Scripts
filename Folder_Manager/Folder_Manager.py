# Imports
import os
import json
import shutil


# Main
if __name__ == "__main__":
    ext = 0
    def folder_manager(path,exception_file,extensions):
        global ext
# Doing intial checks whether  all inputs are valid or not.
#----------------------------------------------------------------------------------------------------------------
        # Importing content of Exception file into a set.
        with open(exception_file,'r',encoding='utf-8') as exct_file:
            execptions = exct_file.read()
        execptions = set(execptions.split('\n'))

        # Changing directory to give path.
        if os.path.isdir(path):
            os.chdir(path)

        # Checking if input  extension is list or not.
        if type( extensions) is not list:
            raise Exception('Expected a list object.')
        extensions = set( extensions)

# Capitalizing all files except the Exceptions. (Folders remains untouched)
#----------------------------------------------------------------------------------------------------------------
        # Generating a list of all files in path folder except Exceptions.
        all_files = {file.lower() for file in os.listdir(path) if os.path.isfile(file)}
        all_files = all_files - execptions

        # Capitalizing all file names in all_files list.
        for file in all_files:
            _name, _ext = os.path.splitext(file)
            os.rename(os.path.join(path,file),('.'.join([_name.title(),_ext[1:]])))


#----------------------------------------------------------------------------------------------------------------
        # Generating a list of files which needs to be renamed as numbers. (i.e. is input  extensions)
        rename_files = {file for file in all_files if file.split('.')[1] in  extensions}

        # Creating a folder named according to the file  extensions and dumping the files in the folder.
        for file_ in rename_files:
            # Needed Variables
            name, ext = os.path.splitext(file_)
            ext = ext[1:]
            folder_name = ext 


            # Code that creates a folder and dump the files in it.
            if ext == '':
                continue

            if os.path.exists(os.path.join(path,ext)):
                os.rename(os.path.join(path,ext),os.path.join(path,ext))
                shutil.move(os.path.join(path,file_),os.path.join(path,ext,file_))
                
            else:
                if os.path.exists(os.path.join(path,folder_name)):
                    shutil.move(os.path.join(path,file_),os.path.join(path,folder_name,file_))

                else:
                    os.makedirs(os.path.join(path,folder_name))
                    shutil.move(os.path.join(path,file_),os.path.join(path,folder_name,file_))

# Deleting Empty Folders, Non-empty Folders are untouched and clearing up some mess created earlier.
#----------------------------------------------------------------------------------------------------------------------

        for folder in os.listdir(path):
            # Deleted Empty folders
            if os.path.isdir(folder):
                if len(os.listdir(os.path.join(path,folder))) == 0:
                    os.rmdir(os.path.join(path,folder))
                    continue


#----------------------------------------------------------------------------------------------------------------------


    def code_runner():

    # Taking user input for Path.
    #----------------------------------------------------------------------------------------------------------------------
        path = input('\nEnter the Path of folder you want to Manage.\nPlease make sure what this script does by reading the Readme.md file.\nEnter Here : ')
        while os.path.isdir(path) == False:
            print('The given path is not valid! Please enter a correct Path.')
            path = input('\nEnter the Path of folder you want to Manage.\nPlease make sure what this script does by reading the Readme.md\nEnter Here : ')
            if os.path.isdir(path) == True:
                break

    # Taking user input for Exception file.
    #----------------------------------------------------------------------------------------------------------------------
        exception_file = input('\nEnter the path of Exception file.\nEnter here : ')
        while os.path.isfile(exception_file) == False:
            print('The given path is not valid! Please enter a correct Path.')
            exception_file = input('\nEnter the path of Exception file.\nEnter here : ')
            if os.path.isfile(exception_file) == True:
                break

    # Taking user input for  extensions.
    #----------------------------------------------------------------------------------------------------------------------
        with open('all-file-extensions.json','r') as json_pointer:
            json_file_exts = json.load(json_pointer)

        extensions = input('\nEnter  extensions of files you want to dump.\nExample - \"dll,exe,txt\" .Don\'t enclose in Inverted commas and seperate  extensions with comma.\nEnter here : ')
        extensions =  extensions.replace(' ','')
        extensions =  extensions.split(',')

        for ext in  extensions:
            ext_json = ext.upper()
            while ext_json not in json_file_exts:
                print(f'{ext} is a Invalid  extension! Please Enter a valid  extension.')
                extensions = input('\nEnter  extensions of files you want to dump.\nExample - \"dll,exe,txt\" .Don\'t enclose in Inverted commas and seperate  extensions with comma.\nEnter here : ')
                extensions =  extensions.replace(' ','')
                extensions =  extensions.split(',')
                for ext in  extensions:
                    ext_json = ext.upper()
                    if ext_json in json_file_exts:
                        break


        folder_manager(path=path,exception_file=exception_file, extensions= extensions)
        print('\nCompleted! Thanks for using this script.')

    code_runner()
