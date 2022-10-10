import csv

class BetterCSVStorage():

    def __init__(self, csv_path):
        self.csv_f_path = csv_path
        self.valid_headers = None
        self.allowed_comparison = ['==', '!=']

    def load(self):
        with open(self.csv_f_path, 'r') as csv_f:
            csv_reader = csv.reader(csv_f)
            self.valid_headers = next(csv_reader)

    def write_dict_csv(self, data_rows):
        if data_rows:
            field_names = list(data_rows[0].keys())
            with open(self.csv_f_path,'w') as csv_wf:
                csv_writer = csv.DictWriter(csv_wf, fieldnames=field_names)
                csv_writer.writeheader()
                for row in data_rows:
                    csv_writer.writerow(row)
            print('[+] Data Written Successfully ...')
        else:
            print('[-] Error : Data Rows Could not be empty ...')

    def get_filtered_data(self, col_name, comparison, value):
        if not self.valid_headers:
            self.load()
        if not col_name in self.valid_headers:
            print('[-] Error : Enter Valid Column Name.')
            print('[*] Info : Allowed Column Names Are : {}'.format(', '.join(self.valid_headers)))
        else:
            if not comparison in self.allowed_comparison:
                print('[-] Error : Invalid Comparison.')
                print('[*] Info : Allowed Comparison Are : {}'.format(', '.join(self.allowed_comparison)))
            else:
                filtered_data = []
                with open(self.csv_f_path,'r') as c_file:
                    csv_reader = csv.DictReader(c_file)
                    for row_index, row in enumerate(csv_reader):
                        try:
                            if (comparison == '=='):
                                if row[col_name] == value:
                                    row['update_index'] = row_index
                                    filtered_data.append(row)
                            if (comparison == '!='):
                                if row[col_name] != value:
                                    row['update_index'] = row_index
                                    filtered_data.append(row)
                        except KeyError:
                            continue
                return filtered_data

    def update_data(self, update_index, col_name, value):
        if not self.valid_headers:
            self.load()
        if not col_name in self.valid_headers:
            print('[-] Error : Enter Valid Column Name.')
            print('[*] Info : Allowed Column Names Are : {}'.format(', '.join(self.valid_headers)))
        else:
            if not update_index:
                print('[-] Error Valid Data Index ....')
            else:
                try:
                    update_index = int(update_index)
                except:
                    print('[-] Error : Update Index is Not Valid')
                    return
                updated_rows = []
                with open(self.csv_f_path,'r') as csv_rf:
                    csv_reader = csv.DictReader(csv_rf)
                    for row_index, row in enumerate(csv_reader):
                        if update_index == row_index:
                            print('[+] Updating Index {}'.format(update_index))
                            row[col_name] = value
                        updated_rows.append(row)
                self.write_dict_csv(updated_rows)

if __name__ == '__main__':

    csv_path = 'dummy_data.csv'

    #init class and get the object
    csv_obj = BetterCSVStorage(csv_path)

    #Now user that object as storage

    #Filter Data Based on Different parameters
    #This List will contain additional ( update_index ) which is row index of each row in csv.
        #This update_index will be use to update value of certain index.
    filtered_data = csv_obj.get_filtered_data('download_status', '==', '')

    #Change Data Based on Different parameters
    csv_obj.update_data(4,'download_status', 'done')
