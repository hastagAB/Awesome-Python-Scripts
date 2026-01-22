import json
import sys
import urllib.request

if len(sys.argv) != 3:
    print("Usage: ./currencyrates.py lookup_currency base_currency. Example: ./currencyrates.py cad usd")
    sys.exit()

currency = sys.argv[1]
basecurrency = sys.argv[2]

currencyurl = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + basecurrency + "&v=1&s=cbr"
f = urllib.request.urlopen(currencyurl)
obj = json.loads(f.read())
result = "1 " + currency.upper() + " is "
result+="{:,.2f}".format(1/obj[currency.upper()]) + " " + basecurrency.upper()

print(result);
