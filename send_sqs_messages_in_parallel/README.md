# Send messages to sqs in parallel

A python script that will take a file with a lot of messages to be sent to sqs and will send them to a queue in highly parallelized manner.
<br>
This is especially useful for batch processing requests.
<br>
Works when ```aws configure``` is done correctly or iam role is attached to the machine

## Requirement

```bash
pip3 install boto3
```

#Usage 
Go to Upload_files_to_s3 directory and add your folder's name you want to upload to s3 and then run upload_files_to_s3.py as below:
```bash
$ python3 send_to_sqs.py
```
