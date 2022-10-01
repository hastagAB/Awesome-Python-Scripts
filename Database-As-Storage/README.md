# Database-As-Storage

### What is it ?

-> Use MySQLite Database as Storage for any kind of python project and standalone scripts, without using any SQL Syntax and Programming,

-> This Script provides CRUD Functionality using MySQLite and Python.

### How to Use ?

-> it's OOP based python Script so you can just called it in your script and use it.

```python
from Database-As-Storage import CustomSqliteAction

db_file_name = 'download_queue.db'
db_table = 'DownloadQueue'
db_fields = [
        ('id','integer','primary key','autoincrement'),
        ('url','text'),
        ('date','date'),
        ('status','text'),

    ]

    db_obj = CustomSqliteAction(database_name=db_file_name, database_table=db_table, database_fields=db_fields)
```

-> this will create a file name `download_queue.db` if not exists

-> will create table name `DownloadQueue` if not exists.

-> will create that table will fields provides by `db_fields`.

-> each field tuple ( field_name, other arguments .... ) , you can add other arguments which is allowed by SQL.



## CURD FUNCTIONALITY

### Creating Data / Storing Data into Database Table

```python
db_obj.store_data(url='https://m.youtube.com/video_id',date='2022-10-01')
```

-> **FUNCTION** `store_data` 

-> provide arguments based on your table fields.

-> this example code will store a database entry of value id = 1 (cause it's auto-incrementing  ), url

-> status will be Null in database cause you haven't provided it.

### Updating Data Into Database Table

```python
db_obj.update_data(search_tuple=('id','1'), url='https://google.com/video_id')
```

-> **FUNCTION** `update_data`

-> will take one required argument to search for particular entry in database,

-> and the value that you want to update.

-> this example code will change the url of id 1.

### Reading Data From Database Table

```python
data = db_obj.read_data(url='https://m.youtube.com/video_id')
multi_con_data = db_obj.read_data(url='https://m.youtube.com/video_id',status='done')
all_data = db_obj.read_all()
```

-> **FUNCTION** `read_data`  and `read_all`

-> you can search and get data based on multiple or single arguments,

-> also you can get the whole table also.

-> will return list of python dictionary ( each row as dict object )

### Deleting Data From Database Table

```python
delete_id = 1
db_obj.delete_data(id=delete_id)
db_obj.delete_data(url='https://m.youtube.com/video_id')
db_obj.delete_data(url='https://m.youtube.com/video_id',status='done')
```

-> **FUNCTION** `delete_data`

-> you can delete data based on multiple or single arguments.