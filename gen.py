#
# Apache mod rewrite rules generator
#
# Usage: python gen.py input.csv > output.conf
#
# input csv: CSV vile without headers
# column 1: redirect source
# column 2: operation, either "301" or "only get allowed"
# column 3: redirect target 
#
# eg: http://alamo.no/helpfulinformation/us,301,https://www.alamo.no/nyttig-informasjon/usa/

import csv
import re
import sys

with open(sys.argv[1], 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        src = row[0]
        operation = row[1]
        dst = row[2]
        # rewrite dst to beta
        dst = dst.replace("www.alamo","beta.alamo")
        src_beta = src.replace("www.alamo","beta.alamo")
        if operation == "only get allowed":
            cond = "RewriteCond %{REQUEST_METHOD} !POST"
            # part of the url from the first slash eg.: RatesAndReservation/1668/fi/hotdeals_pay_locally/configuration_xml_default=alfi_trade
            path_str = "/".join(src.split("/")[3:])
            rule = "RewriteRule ^%s$ %s  \t [R=301,L]" % (path_str, dst)
            print("# %s -> %s" % (src_beta, dst))
            print("%s\n%s\n" % (cond, rule))
            continue
        if re.findall(r'\?', src):
            # query string
            base, query = src.split("?")
            cond = []
            base = "/".join(base.split("/")[3:])
            cond.append("RewriteCond %%{REQUEST_URI} ^/%s \t \n" % base)
            #cond.append("RewriteCond %%{QUERY_STRING} ^(.*&)?%s$ \t\n" % query)
            cond.append("RewriteCond %%{QUERY_STRING} ^%s$ \t\n" % query)
            rule = "RewriteRule ^%s %s? \t [R=301,L]\n" % (base,dst)
            output = "".join(cond)
            output += "%s" % rule
            print("# %s -> %s" % (src_beta, dst))
            print(output)
        else:
            path_str = "/".join(src.split("/")[3:])
            # make sure there is no similar rule that has query string after this 
            cond = "RewriteCond %{QUERY_STRING} ^$"
            rule = "RewriteRule ^%s$ %s [R=301,L] " % (path_str, dst)
            print("# %s -> %s" % (src_beta, dst))
            print("%s\n%s\n" % (cond, rule))

