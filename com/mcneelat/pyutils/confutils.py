import json


def load_conf(conf_file):
    print("[*] Reading config from '%s'" % conf_file)
    with open(conf_file) as f:
        conf_data = json.loads(f.read())
    return conf_data
