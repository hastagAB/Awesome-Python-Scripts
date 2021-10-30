
# Automated Google Meet Joiner

An automated google meet joiner the auto-joins meetings according to schedule.




## Setup

1. To run this project, download the files and run the following command to install all the necessary files.

```bash
pip install -r requirements.txt
```

2. Then open the `meeting_ids.txt` file and add your meeting ids for the day in order on each line.

E.g. 
```bash 
meeting_id_1
meeting_id_2
meeting_id_3
```

3. Then open the `meeting_times.txt` file and add your meeting time (in the 24-hour format, e.g. 16:00) for the day in order on each line.

E.g. 
```bash 
16:00
17:30
18:50
```
4. The run the python file either normally or using the `pythonw` version to avoid a dialog box.

```bash
pythonw main.py
```


## Additional Setup

5. To add more than the default 3 meetings setup by the program, simply add your meeting ids and time to the respective file and copy the following line and paste it in the program for as many ids that you add.

```bash
schedule.every().day.at(time[x]).do(joinGoogleMeet(ids[x]))
```
- Remember to replace the 'x' with the number on which the meeting id and time is located. 

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@JohanSanSebastian](https://www.github.com/johansansebastian)

