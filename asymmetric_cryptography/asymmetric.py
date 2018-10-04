from Crypto import Random
from Crypto.PublicKey import RSA
import base64


def generate_keys(modulus_length=256*4):
    privatekey = RSA.generate(modulus_length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey


def encryptit(message , publickey):
    encrypted_msg = publickey.encrypt(message, 32)[0]
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    return encoded_encrypted_msg


def decryptit(message, privatekey):
    decoded_encrypted_msg = base64.b64decode(message)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg


if __name__ == '__main__':
    message = "This is a awesome message!"
    privatekey , publickey = generate_keys()
    encrypted_msg = encryptit(message.encode("utf-8"), publickey)
    decrypted_msg = decryptit(encrypted_msg, privatekey)

    print(f'{privatekey.exportKey()} - ({len(privatekey.exportKey())})')
    print(f'{publickey.exportKey()} - ({len(publickey.exportKey())})')
    print(f'Original: {message} - ({len(message)})')
    print(f'Encrypted: {encrypted_msg} - ({len(encrypted_msg)})')
    print(f'Decrypted: {decrypted_msg} - ({len(decrypted_msg)})')