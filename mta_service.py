#!/usr/bin/python

''' Python Script to get the status of MTA Service. '''

__author__ = "Christopher James Burke"
__copyright__ = ""
__credits__ = ["Christopher James Burke"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Christopher James Burke"
__email__ = "christopherjamesburke@gmail.com"
__status__ = "Production"
__date__ = "2013/09/21 14:27:28"

import urllib
from xml.etree.ElementTree import parse
import sys


def main(line_name):
    # Open the MTA.info url and read the data.
    u = urllib.urlopen('http://www.mta.info/status/serviceStatus.txt')
    data = u.read()

    # Create file serviceStatus.xml and write data.
    f = open('serviceStatus.xml', 'wb')
    f.write(data)
    f.close()

    # Parse the serviceStatus.xml anf find all that match line_name
    doc = parse('serviceStatus.xml')
    subway = doc.findall('subway')
    lines = subway[0].findall('line')
    try:
        train_line = [l for l in lines
                      if l.find('name').text.find(line_name) > 0][0]
    except IndexError:
        print("No Service Status on mta.info")
        sys.exit(0)

    #
    _train = {
        'name': train_line.find('name').text,
        'status': train_line.find('status').text,
        'Date': train_line.find('Date').text,
        'Time': train_line.find('Time').text,
        'text': (train_line.find('text').text or "").encode('utf-8')
    }

    html = """
    <html xmlns="http://www.w3.org/1999/xhtml">
    <body>
            <h1>{name}</h1>
            <h2>Status</h2>
                <p>{status}</p>
            <h2>Date Time</h2>
                <p>{Date} :: {Time}</p>
            <h2>Information</h2>
            <p>
                {text}
            </p>
    </body>
    </html>
    """

    print(html.format(**_train))

    f = open('current_%s_train_status.html' % line_name, 'wb')
    f.write(html.format(**_train))
    f.close()


if __name__ == "__main__":
    main(str(sys.argv[1]))
