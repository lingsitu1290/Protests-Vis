from BeautifulSoup import BeautifulSoup
import urllib2
import requests
import StringIO
import zipfile
import os
import csv

from sqlalchemy import func
from model import Event

from model import connect_to_db, db
from server import app

DATA_DIR = "./data"

# Get URLS from gdelt URL
def get_URLs():
    """Get list of URLs from webpage.

        >>> get_URLs()[-5:-1]
        ['1983.zip', '1982.zip', '1981.zip', '1980.zip']
        >>> get_URLs()[-2:-1]
        ['1980.zip']
        >>> get_URLs()[-6:-1]
        ['1984.zip', '1983.zip', '1982.zip', '1981.zip', '1980.zip']

    """
    list_of_zipped_files = []

    html_page = urllib2.urlopen("http://data.gdeltproject.org/events/index.html")
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        zipped_csv =  str(link.get('href'))
        list_of_zipped_files.append(zipped_csv)
    # Don't want first two files because not csv files and third and last are corrupt 
    return list_of_zipped_files[3:-1]


def process_URL(item):
    """Process the URL.

        >>> process_URL('20160818.export.CSV.zip')
        'http://data.gdeltproject.org/events/20160818.export.CSV.zip'
        >>> process_URL('20160111.export.CSV.zip')
        'http://data.gdeltproject.org/events/20160111.export.CSV.zip'

    """

    link_to_csv = "http://data.gdeltproject.org/events/" + item

    return link_to_csv


def download_and_unzip_file(URL):
    """Download the file and unzip file into data directory and return unzipped file name."""

    print "Downloading: ", URL
    response = requests.get(URL)

    print "Unzipping: ", URL
    zipDocument = zipfile.ZipFile(StringIO.StringIO(response.content))
    #Unzip all files to data directory 
    zipDocument.extractall(DATA_DIR)


def process_csv(file_name):
    """Get data."""

    protests_data = []

    print "Opening File: ", file_name
    # if not item.lower().endswith('.csv'):
    #     continue
    with open(DATA_DIR+"/"+file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='\t')
        for row in readCSV:
            # Want all EventBaseCode that starts with 14 listed for Protests 
            # and discard data with missing eventcodes and lat/logs
            # Extract all protest events 
            if row[27][0:2] == "14" and row[26] != "" and row[53] != "" and row[54] != "":

                #Prints all needed info
                # print "SQLDATE: ", row[1]
                # print "MonthYear: ", row[2]
                # print "Year: ", row[3]
                # print "Full Country Name: ", row[36]
                # print "EventCode: ", row[26]
                # print "EventBaseCode: ", row[27]
                # print "EventRootCode: ", row[28]
                # print "QuadClass: ", row[29]
                # print "GoldsteinScale: ", row[30]
                # print "Lat: ", row[53]
                # print "Long: ", row[54]
                # print "URL: ", row[57]

                # Add event to protest_data list
                protests_data.append(row)
    # print protests_data 
    return protests_data


def load_data(protests_data):
    """Load events into database."""

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate events 
    print "Storing"

    # Read through each protest event all need info
    for protest in protests_data:
        event_id = protest[0]
        full_date = protest[1]
        year = protest[3]
        event_code = protest[27]
        # goldstein_scale = protest[30]
        full_location = protest[36]
        # country_code = protest[37]
        latitude = protest[39]
        longitude = protest[40]
        url = protest[57]

        if latitude == "" or longitude == "":
            continue

        event = Event(event_id=event_id,
                      full_date=full_date,
                      year=year, 
                      event_code=event_code,
                      # goldstein_scale=goldstein_scale,
                      full_location=full_location,
                      # country_code=country_code,
                      latitude=latitude,
                      longitude=longitude,
                      url=url)

        # Add event to session
        db.session.add(event)

    # Commit to database
    db.session.commit()


def delete_file(file_name):
    """Delete the file."""

    print "Deleting: ", file_name
    os.remove(DATA_DIR + "/" + file_name)


def process_file():
    """Download, unzip, store into database, and delete file."""

    list_of_zipped_files = get_URLs()
    # list_of_URLs = process_URL(list_of_zipped_files)

    for item in list_of_zipped_files:
        url = process_URL(item)
        download_and_unzip_file(url)
        #Get rid of the .zip at end of the file
        file_name = item[0:-4]
        protests_data = process_csv(file_name)
        load_data(protests_data)
        delete_file(file_name)


if __name__ == "__main__":
    from doctest import testmod
    if testmod().failed == 0:
        connect_to_db(app)
        process_file()
