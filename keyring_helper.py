import getpass
import keyring
from os.path import exists
from typing import Tuple

tmp_dir_loc = 'secrets_and_tmp/'
un_file = tmp_dir_loc + '/username'
service_name = 'mint'

def get_credentials()-> Tuple[str, str]:
    username_exists = exists(un_file)
    if not username_exists:
        return _set_credentials()
    with open(un_file, "r") as f:
        un = f.read()
    pw = keyring.get_password(service_name, un)
    assert pw, "Password not found for {}; please delete {} to overwrite".format(un, un_file)
    return un, pw

def _set_credentials()-> Tuple[str, str]:
    un = input("Please enter your username.\n")
    assert isinstance(un, str) and len(un) > 0
    with open(un_file, "w") as f:
        f.write(un)
    print("Please enter your password.\n")
    pw = getpass.getpass()
    assert isinstance(pw, str) and len(pw) > 0
    keyring.set_password(service_name, un, pw)
    return un, pw
