import os
import argparse
import json
import requests

def download_image(image_url, image_dir):
    '''Downloads image from image_url to image_dir if the image doesn't exist.'''
    
    file_name = image_url.split('/')[-1]
    file_path = os.path.join(image_dir, file_name)
    if os.path.exists(file_path):
    	verbose("[INFO]%s exists, skipping download" % file_name, v_flag)
    	return file_path
    
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        verbose("[INFO]Downloaded %s" % file_name, v_flag)
        return file_path
    else:
        print('[WARNING]Unable to download image, skipping...')
        return False

def generate_annotation(label, data):
    '''Generate annotation from the json file.'''
    
    image_width = data['imageWidth']
    image_height = data['imageHeight']

    #if four coordinates of the bounding box is given
    if len(data['points']) == 4:
        xmin = image_width * min(data['points'][0][0], data['points'][1][0], data['points'][2][0], data['points'][3][0])
        ymin = image_height * min(data['points'][0][1], data['points'][1][1], data['points'][2][1], data['points'][3][1])
        xmax = image_width * max(data['points'][0][0], data['points'][1][0], data['points'][2][0], data['points'][3][0])
        ymax = image_height * max(data['points'][0][1], data['points'][1][1], data['points'][2][1], data['points'][3][1])

    #if diagonal coordinates given
    else:
        xmin = int(data['points'][0]['x'] * image_width)
        ymin = int(data['points'][0]['y'] * image_height)
        xmax = int(data['points'][1]['x'] * image_width)
        ymax = int(data['points'][1]['y'] * image_height)

    #calculating coodinate ratios as required for training yolo
    x_center = ((xmax + xmin) / 2.0) / image_width
    y_center = ((ymax + ymin) / 2.0) / image_height
    width = (xmax - xmin) / image_width
    height = (ymax - ymin) / image_height

    return ("%.6f %.6f %.6f %.6f\n"% (x_center, y_center, width, height))

def convert_to_yolo_annotation():
    classes = []
    train_txt = []
    with open(dataturks_json_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        data = json.loads(line)
        if data['annotation'] == None:
            continue

        file_path = download_image(data['content'], image_dir)

        if not file_path:
            continue

        annotation = ''
        
        for item in data['annotation']:
            if item['label'] == None:
                continue
            
            labels = item['label']
            if not isinstance(labels, list):
                labels = [labels]
                
            for label in labels:
                if label not in classes:
                    classes.append(label)

                annotation = annotation + str(classes.index(label)) + ' ' + generate_annotation(label, item)

        train_txt.append(str(os.path.abspath(file_path)) + '\n')

        annotation_file = '.'.join(file_path.split('.')[:-1]) + '.txt'

        with open(annotation_file, 'w') as f:
            f.write(annotation)
        verbose("[INFO]%s file generated." % annotation_file, v_flag)
            
    with open(os.path.join(yolo_dir, 'train.txt'), 'w') as file:
    	file.writelines(train_txt)
    verbose("[INFO]train.txt file generated.", v_flag)
                
    return classes

def generate_yolo_cfg_files(classes):
	
    with open(os.path.join(yolo_dir, 'obj.names'), 'w') as file:
        for item in classes:
            file.write(item + '\n')
    verbose("[INFO]obj.names file generated.", v_flag)

    with open(os.path.join(yolo_dir, 'obj.data'), 'w') as file:
        file.write('classes = %s\ntrain = %s\nnames = %s\nbackup = %s' %
                   (str(len(classes)),
                    str(os.path.join(os.path.abspath(yolo_dir), 'train.txt')),
                    str(os.path.join(os.path.abspath(yolo_dir), 'obj.names')),
                    str(os.path.join(os.path.abspath(yolo_dir), 'backup/'))
                   )
        )
    verbose("[INFO]obj.data file generated.", v_flag)

    n_classes = len(classes)

    n_filters = (n_classes + 5) * 3

    with open(os.path.join(yolo_dir, 'yolov3.cfg'), 'w') as file:
        with open('yolov3.cfg.template') as template:
            lines = template.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('#FILTER#', str(n_filters))
            lines[i] = lines[i].replace('#CLASS#', str(n_classes))
        file.writelines(lines)
    verbose("[INFO]yolov3.cfg file generated.", v_flag)

        
def main():
    if not os.path.isdir(image_dir):
        print('[ERROR]The directory %s does not exist' % os.path.abspath(image_dir))
        return
    if not os.path.exists(dataturks_json_path):
        print('[ERROR]The specified json file does not exitst')
        return
    if not os.path.isdir(yolo_dir):
        print('[ERROR]The directory %s does not exist' % os.path.abspath(yolo_dir))
        return
    classes = convert_to_yolo_annotation()
    generate_yolo_cfg_files(classes)
    

def arg_parser():
    parser = argparse.ArgumentParser(description = 'Converts Dataturks JSON format to yolo-darknet format.')
    parser.add_argument('-v', help = 'Verbose output.', action = 'store_true')
    parser.add_argument('-d', '--dataturks_json_path', required = True, help = 'Path to the Dataturks JSON file.')
    parser.add_argument('-i', '--image_dir', required = True, help = 'Path to the directory where the images with annotations will be stored.')
    parser.add_argument('-y', '--yolo_dir', required = True, help = 'Path to the directory where the files for training YOLO will be stored.')
    return parser.parse_args()
    
def verbose(message, v_flag):
	if v_flag == True:
		print(message)

if __name__ == '__main__':
    args = arg_parser()
    global dataturks_json_path
    global image_dir
    global yolo_dir
    global v_flag
    dataturks_json_path = args.dataturks_json_path
    image_dir = args.image_dir
    yolo_dir = args.yolo_dir
    v_flag = args.v
    main()
