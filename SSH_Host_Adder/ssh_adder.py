import argparse, os

ssh_template = """
HOST {name}
    HostName {hostname}
    User {user}
    Port {port}
"""

def args_to_obj(args):
    obj = ssh_template.format(**args)
    return obj

def add_to_conf(conf, obj):
    conf = os.path.expanduser(conf)
    with open(conf, 'a') as f: 
        f.write(obj)


def main():
# create the top-level parser
    parser = argparse.ArgumentParser(prog = "Adds ssh hosts to the ssh config file. Is kind of a simple script which doesn't support all the options. May update with more stuff. \nExample usage: ./ssh_adder myhost 192.168.80.1 --user someuser --port 2200 --conf /path/to/non-default/ssh/config")
    
    # create the parser for the "a" command
    parser.add_argument('name', help = "This is the name of the Host to add to the config. For instance, if you want to do `ssh somehost`, then name should be `somehost`")
    parser.add_argument('hostname',  help = "This is the hostname/ip address of the host. If `somehost`'s address is 192.168.80.1, then hostname=192.168.80.1")
    parser.add_argument('--user', default = 'root', help="The user to connect with. Defaults to root")
    parser.add_argument('--port', default = 22, type = int, help = "The port to connect to. Defaults to 22")
    parser.add_argument('--conf', default = '~/.ssh/config', help = "The path to the ssh config file. Defaults to ~/.ssh/config, which is the default location. ")

    args = parser.parse_args()

    obj = args_to_obj(args.__dict__)
    add_to_conf(args.conf, obj)

main()
