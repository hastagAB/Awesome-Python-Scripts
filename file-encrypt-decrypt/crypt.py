import os
import argparse

from cryptography.fernet import Fernet

class Crypt:

    def __init__(self):
        
        # can be generated Fernet.generate_key()
        # if generated, save it below
        self.key = b'oBa5LeeJt1r4BmNyJXb6FHd1U21GMshH9Pqu_J-HzNQ='
        self.fernet = Fernet(self.key)

    def encrypt(self, input_file_path):
        """
        Encrypt a file
        """

        # split the file and take only the file name
        base_name = os.path.basename(input_file_path).split('.')[0].split('-')[-1]

        # creates a file name with extension .enc
        output_file = f"{base_name}.enc"
        if os.path.exists(output_file):
            print(f'Encrypted File already exists')
        else:
            with open(input_file_path, 'rb') as i:
                input_data = i.read()

            encrypted = self.fernet.encrypt(input_data)

            with open(output_file, 'wb') as o:
                o.write(encrypted)
            print(f'Encrypted file: {output_file}\n')


    def decrypt(self, input_file_path, output_file_ext='txt'):
        """
        Decrypt an already encrypted file
        """

        # split the file and take only the file name
        base_name = os.path.basename(input_file_path).split('.')[0].split('-')[-1]
        output_file = f'{base_name}.{output_file_ext}'
        with open(input_file_path, 'rb') as f:
            file_data = f.read()

        decrypted = str(self.fernet.decrypt(file_data), 'utf-8')

        with open(output_file, 'w') as o:
            o.write(decrypted)
        print(f'Decrypted file: {output_file}\n')

    
if __name__ == '__main__':
    crypt = Crypt()

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-e', '--encrypt',
                        help='Encrpyt the file')
    parser.add_argument('-d', '--decrypt', 
                        help='Decrypt the file')

    args = parser.parse_args()

    if args.encrypt:
        print(f'Input file: {args.encrypt}')
        crypt.encrypt(args.encrypt)
    elif args.decrypt:
        print(f'Input file: {args.decrypt}')
        crypt.decrypt(args.decrypt)
