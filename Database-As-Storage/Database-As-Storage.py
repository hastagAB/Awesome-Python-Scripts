from dataclasses import field, fields
import sqlite3
from unittest import result

class CustomSqliteAction():
    def __init__(self,database_name, database_table, database_fields):
        self.database = database_name
        self.table_name = database_table
        self.fields = database_fields

        self.db_conn = None
        self.valid_fields = None

    def connect_to_db(self):
        print('[+] Connecting to {}'.format(self.database))
        db_conn = sqlite3.connect(self.database)
        self.db_conn = db_conn

    def load_table_info(self):
        self.valid_fields = [f_name[0] for f_name in self.fields]

    def table_validation(self,inserted_fields):
        return list(set(inserted_fields).difference(set(self.valid_fields)))

    def _parse_result(self,db_data):
        query_set = []
        for data in db_data:
            data_dict = {k: v for k, v in zip(self.valid_fields, data)}
            query_set.append(data_dict)
        return query_set

    def create_table(self):
        sql_string = """CREATE TABLE IF NOT EXISTS {table_name} {field_string};"""
        field_string = "("+", ".join([" ".join(fi for fi in f) for f in self.fields])+")"
        sql_string = sql_string.format(table_name=self.table_name,field_string=field_string)

        print("[+] Creating Table {} .....\n".format(self.table_name))
        cur = self.db_conn.cursor()
        cur.execute(sql_string)

    def table_exists(self):
        sql_string = """SELECT * FROM {}""".format(self.table_name)
        try:
            cur = self.db_conn.cursor()
            cur.execute(sql_string)
            print('[+] Connecting To Table {}\n'.format(self.table_name))
            return True
        except sqlite3.OperationalError:
            print('[-] TABLE NAME {} DOES NOT EXISTS'.format(self.table_name))
            return False

    def store_data(self,**kwargs):
        validation = self.table_validation(kwargs.keys())
        if not validation:
            sql_string = """INSERT INTO {table_name} {field_string} VALUES {value_string};"""
            field_string = "("+", ".join([f for f in kwargs.keys()])+")"
            value_string = "("+ ", ".join([f"'{v}'" for v in kwargs.values()]) +")"

            sql_string = sql_string.format(table_name=self.table_name,field_string=field_string,value_string=value_string)
            cur = self.db_conn.cursor()
            try:
                cur.execute(sql_string)
            except sqlite3.OperationalError:
                print('[-] Database Syntax Error probabily because of \' in data ')
            self.db_conn.commit()
        else:
            print('\n[-] STORE DATA ERROR ...')
            print('[-] {} IS NOT VALID FIELD NAME'.format(', '.join(validation)))
            print('[-] CHOICES ARE {}'.format((', ').join(self.valid_fields)))

    def delete_data(self,**kwargs):
        validation = self.table_validation(kwargs.keys())
        if not validation:
            if len(kwargs) == 1:
               sql_string = """DELETE FROM {table_name} WHERE {field} = '{field_id}';"""
               sql_string = sql_string.format(table_name=self.table_name,field=list(kwargs.keys())[0],field_id=list(kwargs.values())[0])
            elif len(kwargs) > 1:
                inintial_string = """DELETE FROM {table_name} WHERE """.format(table_name=self.table_name)
                field_string = " AND ".join(["{field} = '{field_value}'".format(field=f[0],field_value=f[1]) for f in kwargs.items() ]) + ";"
                sql_string = inintial_string + field_string
            else:
                print('[-] At least Provide 1 Argument')
                return
            
            cur = self.db_conn.cursor()
            cur.execute(sql_string)
            self.db_conn.commit()
            print("[+] Delete Data Successfully") 

        else:
            print('\n[-] DELETE DATA ERROR ...')
            print('[-] {} IS NOT VALID FIELD NAME'.format(', '.join(validation)))
            print('[-] CHOICES ARE {}'.format((', ').join(self.valid_fields)))

    def update_data(self,search_tuple, **kwargs):
        validation = self.table_validation(kwargs.keys())
        if not validation:
            if len(kwargs) == 1:
                sql_string = """UPDATE {table_name} SET {field} = '{update_value}' WHERE {p_field} = {field_id};"""
                sql_string = sql_string.format(table_name=self.table_name, field=list(kwargs.keys())[0], update_value=list(kwargs.values())[0], p_field=search_tuple[0], field_id=search_tuple[1])
            else:
                print('[-] Only One Upadte Argument Allowed')
                return
            cur = self.db_conn.cursor()
            cur.execute(sql_string)
            self.db_conn.commit()
            print("[+] Update Data Successfully")
        else:
            print('\n[-] DELETE DATA ERROR ...')
            print('[-] {} IS NOT VALID FIELD NAME'.format(', '.join(validation)))
            print('[-] CHOICES ARE {}'.format((', ').join(self.valid_fields)))

    def read_data(self,**kwargs):
        validation = self.table_validation(kwargs.keys())
        if not validation:
            if len(kwargs) == 1:
                sql_string = """SELECT * FROM {table_name} WHERE {field} = '{read_value}';"""
                sql_string = sql_string.format(table_name=self.table_name, field=list(kwargs.keys())[0], read_value=list(kwargs.values())[0])
            elif len(kwargs) > 1:
                inintial_string = """SELECT * FROM {table_name} WHERE """.format(table_name=self.table_name)
                field_string = " AND ".join(["{field} = '{read_value}'".format(field=f[0],read_value=f[1]) for f in kwargs.items() ]) + ";"
                sql_string = inintial_string + field_string
            else:
                print('[-] Provide At least One Argument')
                return
            
            cur = self.db_conn.cursor()
            cur.execute(sql_string)
            self.db_conn.commit()

            #FETCHING DATA
            result = cur.fetchall()
            return self._parse_result(result)
        else:
            print('\n[-] READ DATA ERROR ...')
            print('[-] {} IS NOT VALID FIELD NAME'.format(', '.join(validation)))
            print('[-] CHOICES ARE {}'.format((', ').join(self.valid_fields)))

    def read_all(self):
        #PART1 : CREATING THE SQL STRING
        sql_string = """SELECT * FROM {table_name};"""
        sql_string = sql_string.format(table_name=self.table_name)

        #PART2 : EXECUTING THAT CREARED STRING
        cur = self.db_conn.cursor()
        cur.execute(sql_string)
        self.db_conn.commit()

        #FETCHING DATA
        result = cur.fetchall()
        return self._parse_result(result)

    def load(self):
        self.connect_to_db()
        if not self.table_exists():
            self.create_table()
            self.load_table_info()
        else:
            self.load_table_info()


if __name__ == '__main__':
    db_file_name = 'download_queue.db'
    db_table = 'DownloadQueue'
    db_fields = [
        ('id','integer','primary key','autoincrement'),
        ('url','text'),
        ('date','date'),
        ('status','text'),

    ]

    db_obj = CustomSqliteAction(database_name=db_file_name, database_table=db_table, database_fields=db_fields)

    #will create .db file if not exists
    #will create table if not exists
    db_obj.load()

    #let's Store Some Data
    #function > store_data()
    #you can also use python datetime object as a date field
    db_obj.store_data(url='https://m.youtube.com/video_id',date='2022-10-01')


    #let's Update Some Data
    #function > update_data()
    db_obj.update_data(search_tuple=('id','1'), url='https://google.com/video_id')


    #let's Read Some data
    #function > read_data() , read_all()

    #read_data()
    #-> will read based on single condition or multiple condition and returns python list contaning all the data
    print('Single Argument Search ...')
    data = db_obj.read_data(url='https://m.youtube.com/video_id')
    print(data)

    print('Multiple Argument Search ...')
    multi_con_data = db_obj.read_data(url='https://m.youtube.com/video_id',status='done')
    print(multi_con_data)

    print('Reading All Data ...')
    all_data = db_obj.read_all()
    print(all_data)

    #let's delete Some Data
    #function > delete_data()
    delete_id = 1
    db_obj.delete_data(id=delete_id)
    db_obj.delete_data(url='https://m.youtube.com/video_id')
    db_obj.delete_data(url='https://m.youtube.com/video_id',status='done')
