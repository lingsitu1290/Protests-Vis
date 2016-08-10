from BeautifulSoup import BeautifulSoup
import urllib2
import requests
import StringIO
import zipfile
import os
import csv
 
# Get URLS from gdelt URL
def get_URLs():
    list_of_zipped_files = []

    html_page = urllib2.urlopen("http://data.gdeltproject.org/events/index.html")
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        zipped_csv =  str(link.get('href'))
        list_of_zipped_files.append(zipped_csv)
    # Don't want first two files because not csv files and third and last are corrupt  
    return list_of_zipped_files[3:-1]


# Get CSV zip files 
def get_CSVs(URLs, data_dir): 
    for item in URLs: 
        link_to_csv = "http://data.gdeltproject.org/events/" + item
        print "Downloading: ", link_to_csv
        response = requests.get(link_to_csv)

        #Unzipping the file 
        print "Unzipping: ", link_to_csv
        zipDocument = zipfile.ZipFile(StringIO.StringIO(response.content))
        #Unzip all files to data directory 
        zipDocument.extractall(data_dir)

# Process CSV
def process_csv(data_dir): 
    protests_data = []

    for file in os.listdir(data_dir):
        print "Opening File: ", file 
        if not file.lower().endswith('.csv'):
            continue
        with open(data_dir+"/"+file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter='\t')
            for row in readCSV:
                # Want all EventBaseCode that starts with 14 listed for Protests
                # Extract all protest events 
                if row[27][0:2] == "14":

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

                    return protests_data.append(row)
          

if __name__ == "__main__":
    data_dir = './data'
    URLs = get_URLs()
    get_CSVs(URLs, data_dir)
    process_csv(data_dir)