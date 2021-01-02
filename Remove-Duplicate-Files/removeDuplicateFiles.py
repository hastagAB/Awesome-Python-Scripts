import os
import hashlib

# function to compute SHA-1 hash of a file
def computeFileHash(fileName):
    genHash = hashlib.sha1()
    with open(fileName, 'rb') as file:
        block = 0
        while block!=b'':
            block = file.read(1024)
            genHash.update(block)
    file.close()
    return genHash.hexdigest()

#function to get list of files present in a directory
def getFileList(dirPath):
    listOfFiles=list()
    for(dirpath, dirnames, filenames) in os.walk(dirPath):
        listOfFiles+=[os.path.join(dirpath, file) for file in filenames]
    return listOfFiles

def main():
    dirPath = input("Enter relative path to directory: ")
    if not os.path.exists(dirPath):
        print("Invalid path.")
        exit()
    listOfFiles = getFileList(dirPath)
    duplicateFileSizes={}
    duplicateFileHashes={}
    """ grouping files according to their size, so that hashes have to be
        computed only for files having the same size"""
    for file in listOfFiles:
        fileSize = os.path.getsize(file)
        if fileSize in duplicateFileSizes:
            duplicateFileSizes[fileSize].append(file)
        else:
            duplicateFileSizes[fileSize] = [file]
    for List in duplicateFileSizes.values():
        if len(List)>1:
            for path in List:
                fileHash = computeFileHash(path)
                if fileHash in duplicateFileHashes.keys():
                    duplicateFileHashes[fileHash].append(path)
                else:
                    duplicateFileHashes[fileHash]=[path]
    print("Duplicates in the directory are:")
    for files in duplicateFileHashes.values():
        print("(", end='')
        for fileName in files:
            print(fileName, end=', ')
        print(")")
    delete = input('Enter Y to delete duplicate files: ')
    if delete=='Y' or delete=='y':
        for files in duplicateFileHashes.values():
            for fileName in files[1:]:
                os.remove(fileName)
if __name__=='__main__':
    main()
    
