import sys
from converter import Converter

def get_input(msg = ''):
    if (sys.version_info > (3, 0)):
        return input(msg)
    else:
        return raw_input(msg)

def is_int_or_float(value):
    return value.isdigit()

def process_check(value, callback):
    if value == 'Q' or value == 'q':
        user_selected(value)
    elif value == 'C' or value == 'c':
        if (callback.__name__ == 'process_px_to_rem'):
            process_rem_to_px()
            return
        else:
            process_px_to_rem()
            return
    elif is_int_or_float(value) == False:
        print("Warning:: Allowed number only! Or if you need to qute plesae enter Q.\n")
        callback()

def process_px_to_rem():
    px = get_input("[PX to REM] Enter a number of px that need to convert to rem. Enter C to Change to [REM to PX] or Q to quit!\n")

    process_check(px, process_px_to_rem)

    rem = Converter().px_to_rem(px)
    print("%spx == %srem" % (px, rem))
    process_px_to_rem()

def process_rem_to_px():
    rem = get_input("[REM to PX] Enter a number of rem that need to convert to px. Enter C to Change to [PX to REM] or Q to quit!\n")

    process_check(rem, process_rem_to_px)

    px = Converter().rem_to_px(rem)
    print("%srem == %spx" % (rem, px))
    process_rem_to_px()

def user_selected(user_input):
    if user_input == 'A' or user_input == 'a': # PX to REM
        process_px_to_rem()
    elif user_input == 'B' or user_input == 'b': # REM to PX
        process_rem_to_px()
    elif user_input == 'Q' or user_input == 'q':
        print("Nice to meet you. See you next time!")
        exit()
    else:
        print("""
Please Selected A or B to continue, Q to quit...
""")
        user_input = get_input()
        user_selected(user_input)


# Start
user_input = get_input("""
Please select your converter.

A. PX to REM
B. REM to PX
""");

user_selected(user_input)
