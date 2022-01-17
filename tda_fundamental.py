



import pandas as pd
import numpy as np


import requests
import time

# create a config file that has your api key and encryption password that you generated the first time for a particular brokerage account
from tda_config import tda
from tda_config import encryption_passcode

import numpy as np
from datetime import datetime, timedelta
from pytz import timezone
import robin_stocks.tda as T

# example to get fundamentals data for any ticker

url = 'https://api.tdameritrade.com/v1/instruments'
payload = {'apikey':tda,'symbol': 'MSFT','projection':'fundamental'}



X = T.helper.request_get(url, payload, parse_json= True)
X = pd.DataFrame(X[0]['MSFT'])
df = X['fundamental'].reset_index(drop = False)

# to get account access to make trades you need the encryption password

client_id = tda


T.authentication.login(encryption_passcode)

r = T.accounts.get_accounts(options=None, jsonify=None)

