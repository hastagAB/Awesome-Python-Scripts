import os
import binascii

# var: jpeg signature header
# var: jpeg signature footer
header = "\\xff\\xd8\\xff"
footer = "\\xff\\xd9"

global file_cnt
file_cnt = 0
global dir_cnt
dir_cnt = 0

# dir read
def fileSearch(dir_path, cnt):
	global file_cnt
	global dir_cnt
	filelist = []

	for _ in range(cnt):
		print("\t", end=" ")
	print("[>] Directory: %s" % dir_path)
	for files in os.listdir(dir_path):
		if os.path.isfile(dir_path+files):
			filelist.append(dir_path+files)
			for _ in range(cnt):
				print("\t", end=" ")
			print("[+] File Name: %s" % files)
			file_cnt+=1
		elif os.path.isdir(dir_path+files):
			for i in range(cnt):
				print("\t", end=" ")
			print("[!] SubDirectory: \"%s\" found. Start file search in this directory." % files)
			filelist.extend(fileSearch(dir_path+files+"/", cnt+1))
			dir_cnt+=1

	return filelist

# file open and store carved file
def Carving(file_list):
	cnt = 0
	carv_list = []
	print("====================Carving Start====================")
	for i in range(len(file_list)):
		file = open(file_list[i], 'rb')
		carv_cont = findSignature(file)
		print("[-] ", file_list[i], " File passed")

		if (len(carv_cont) != 0):
			carv = open('carv'+str(cnt)+'.jpeg', 'wb')
			for j in range(len(carv_cont)):
				carv.write(carv_cont[j])
			print('[*] carv',str(cnt),'.jpeg is created!')
			carv_list.append('carv'+str(cnt)+'.jpeg')
			cnt+=1
			carv.close

		file.close
	return carv_list
		
# find signature
def findSignature(file):
	flag = 0
	contents = []

	while(1):
		buf = file.read(0x200)
		file.tell()
		if(len(buf)==0): break
		if(flag != 1):
			ishead = (str(buf[:3]).split('\'')[1])
			if (header == ishead) and (flag == 0):
				contents.append(buf)
				flag = 1
		else:
			if(footer in (str(buf[-2:]).split('\'')[1])):
				contents.append(buf)
				return contents
			else:
				contents.append(buf)
	return contents


# main
if __name__ == "__main__":
	print("==================File Search Start==================")
	fl = fileSearch("./", 0)
	print(f'\nSEARCH RESULT: %d Files. %d Directory.' % (file_cnt, dir_cnt))
	print("Filelist: %s\n" % fl)
	c1 = Carving(fl)
	print("Carvlist: %s\n" % c1)

	print("Exit...")