import os
import json
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

music_dir = 'assets/music/'
cover_dir = 'assets/cover/'
js_destination_file = 'js/main/music_list.js'

with open(js_destination_file,'w') as js_file:
    pass

def work_on_mlist(m_list,m_dir):
    out_list = []
    for mp3_index,mp3 in enumerate(m_list):
        file_path = music_dir + m_dir +  '/' + mp3
        mp3file = MP3(file_path,ID3=EasyID3)
        album = mp3file.get('album')
        artist = mp3file.get('artist')
        genre = mp3file.get('genre')
        title = mp3file.get('title')
        d_dict ={
            'id': str(mp3_index),
            'title': title,
            'artist': artist,
            'album': album,
            'genre': genre,
            'f_path':file_path,
            'c_path':file_path.replace('.mp3','.jpg').replace('/music/','/cover/')
        }
        out_list.append(d_dict)
    return out_list

def write_in_js_file(py_object, js_var_name):
    js_object = json.dumps(py_object,indent = 4)
    var = 'const ' + js_var_name + ' = '

    out_string = var + js_object + ';'

    with open(js_destination_file,'a') as js_file:
        js_file.write(out_string +'\n')


all_list = [d.lower() for d in os.listdir(music_dir)]
write_in_js_file(all_list,'music_list')

main_dict = {}

for main_dir in os.listdir(music_dir):
    m_list = os.listdir(music_dir+main_dir)
    out_list = work_on_mlist(m_list,main_dir)
    var = main_dir.lower()
    main_dict[var] = out_list

write_in_js_file(main_dict,'main_list')
    