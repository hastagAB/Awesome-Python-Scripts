p

# Better CSV Storage

-> For User / Programmer who don't want to use databases and want to use csv instead, this script will help manage that csv file (storage)



### What you Can Do ?

-> Filter Data Based On Certain Conditions that you provide,

-> Update Certain Value in particular row.



### How to use ?

-> It's OOP based Script so just import that in you Regular Script.

-> For Example,

​	-> I want to check and download_status of files.

​	-> csv file i have used -> `dummy_data.csv`

```python
csv_path = 'dummy_data.csv'

#init class and get the object
csv_obj = BetterCSVStorage(csv_path)

#Now user that object as storage

#Filter Data Based on Different parameters
#This List will contain additional ( update_index ) which is row index of each row in csv.
#This update_index will be use to update value of certain index.
filtered_data = csv_obj.get_filtered_data('download_status', '==', '')

#Change Data Based on Different parameters
csv_obj.update_data(10,'download_status', 'done')
```
