from datetime import datetime, timedelta
import json
import mintapi
from typing import Optional

import keyring_helper

tmp_dir_loc = 'secrets_and_tmp/'

import ipdb; ipdb.set_trace()
un, pw = keyring_helper.get_credentials()
mint = mintapi.Mint(un, pw)

def get_x1_id() -> str:
    accounts = mint.get_account_data()
    for act in accounts:
        if act['name'].startswith('X1 Visa Credit Card'):
            return act['id']
    raise Exception('Did not find X1 account in Mint')

x1_id = get_x1_id()
cur_time = datetime.now()
txns = mint.get_transaction_data(id=x1_id,
                          start_date=cur_time,
                          end_date=cur_time-timedelta(days=2))


txns_file = tmp_dir_loc + 'txns.json'
with open(txns_file, "w") as f:
    f.write(json.dumps(txns))
