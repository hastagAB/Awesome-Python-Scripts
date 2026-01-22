# Convert Dataturks json to YOLO format
The ```convert.py``` script downloads the images and converts the annotations from the Dataturks json file to YOLO format.
## Usage
1. Clone or download this repository.
2. Create folders for saving images and YOLO config files.
3. Execute:
```
python3 convert.py -d <path/to/dataturks.json> -i <directory/to/save/downloaded/images/> -y <directory/to/save/yolo/config/files/>
```
Note: ```-v``` flag can be used for detailed output.
## Output
1. Downloaded images along with their annotations in the specified directory.
2. YOLO config files ```train.txt, obj.names, obj.data, yolov3.cfg``` saved in the specified directory.
