import os
import argparse
from tqdm import tqdm
class rename:
    def __init__(self):
        pass
    def renamed(self, args):
        i=1
        self.path = args.path
        self.extension = args.extension.split(",")
        if self.extension[0] == "":
            raise ValueError('No extension specified')
        self.Name = args.Name
        self.log  = args.log
        if self.log:
            f = open(self.path + self.Name+"_log.txt", 'w')
        for filename in tqdm(os.listdir(self.path)):
            if filename == os.path.basename(f.name):
                continue
            for exten in self.extension:
                if exten not in filename:
                    continue
                else:
                    while True:
                        try:
                            new_name = self.Name+str(i)+exten
                            source = self.path + filename
                            new_name = self.path + new_name
                            os.rename(source,new_name)
                            break
                        except Exception as e :
                            print(f"Renamed File already exists: {new_name} , {e}")
                            print("incrementing index by 1")
                            i+=1
                    if self.log:
                        f.write(f'{filename}:{os.path.basename(new_name)} \n')    
                    
                i += 1
            else:      
                continue
        if self.log:
            f.close()
        print("Completed")
        return os.listdir(self.path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="BulkFileRename",description="Rename all the files of a given extension in format <Name><index>.<extension>")
    parser.add_argument('path',help="path of the folder")
    parser.add_argument("-n","--Name",default="",help="Custom filename to add before the index. Ex: file.txt -> my_file_1.txt, other.txt -> my_file_2.txt, here Name == 'my_file_'")
    parser.add_argument("-e","--extension",help="Only renames the specified extension files. Ex: jpg, png,..", type=str,default="")
    parser.add_argument("-l","--log",help="To log changes of file names. Creates a txt file", action='store_true')
    args = parser.parse_args()
    rename().renamed(args)


