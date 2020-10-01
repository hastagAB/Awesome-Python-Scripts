## HOW TO USE

#### Using OpenCv ([link](./toonify-opencv.py))


- To just view the image
```python
python3 toonify-opencv.py -i img_path
```


- To view and download the image 
```python
python3 toonify-opencv.py -i img_path -o download_path
```

#### Using Toonify-API(by DeepAI) 


##### For local image ([link](./toonify-API-1.py))

```python 
python3 toonify-API-1.py -i img_path -k api_key

```

##### For URLS ([link](./toonify-API-2.py))

```python 
python3 toonify-API-2.py -i img_path -k api_key

```

> NOTE: The toonify image works well with .jpg format and might give some problem with other formats


For more details on toonify API:

[toonify API doc](https://deepai.org/machine-learning-model/toonify)
