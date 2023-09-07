# To Rename Large number of files in a folder sequentially.

## Requirements
1. Argparse
2. tqdm
   
## Usage:

```python
python BulkFileRenamer.py <path> -e <extensions> -n <name> --log

Renamed File: <Name><index>.<original extension>
```
## Example:

```python
./testing_dir/
            |__ a.png
            |__ b.jpg
            |__ c.jpeg
            |__ d.xyz
```

```python
python BulkFileRenamer.py ./testing_dir/ -e jpg,png,jpeg -n train_image_ -l 
```

### After Renaming

```python
./testing_dir/
            |__ train_image_1.png
            |__ train_image_2.jpg
            |__ train_image_3.jpeg
            |__ d.xyz
            |__ train_image_log.txt <log to store the mapping, {old_name}: {new_name}>
```