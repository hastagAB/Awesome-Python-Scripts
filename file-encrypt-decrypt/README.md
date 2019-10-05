# 🗝 crypt

A command line python script which can Encrypt a given file and also decrypt the encrypted file



#### Pre-requisites 
* install pipenv
```sh
$ brew install pipenv
```

* install dependencies
```sh
$ pipenv install
```

#### Usage
* Encrypt file
```sh
$ pipenv run python crypt -e file.txt
```
* Decrypt file
```sh
$ pipenv run python crypt -d file.enc
```
**note** 
- `file.enc` will be created if you pass in `file.txt`
- Do not loose the Encryption 🗝