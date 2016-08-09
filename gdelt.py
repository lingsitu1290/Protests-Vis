
# use the requests library to get a response from the API
# r = requests.get("http://data.gdeltproject.org/gdeltv2/20160807000000.export.CSV.zip")

# zip_ref = zipfile.ZipFile(r, 'r')
# zip_ref.extractall(/desktop)
# zip_ref.close()

# print type(r)
# print dir(r)

# # what data type is the output of r.json() ? 


# # a dictionary, you say? What are the keys? 
# print gdelt

# zf = zipfile.ZipFile('20160715.export.CSV.zip', 'r')
# print dir(zf)





# import csv

# with open('20160715.export.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter='\t')

#     for row in readCSV:
#         if row[6]=="TURKEY":
#             # print "GlobalEventID: ", row[0], "Day: ", row[1]
#             # print "ActorCode: ", row[5], "ActorName: ", row[6], 
#             # print "Actor1Country: ", row[7], "ActorKnownGroup: ", row[8], 
#             # print "ActorEthnicCode: ", row[9], "ActorReligion: ", row[10], "EventCode: ", row[16]
#             # print "EventBaseCode: ", row[17], "EventRootCode: ", row[18], "QuadClass: ", row[19]
#             # print "GoldStein: ", row[20], "NumArticles: ", row[23], "AvgTone: ", row[24]
#             # print "GeoFullName: ", row[26], "Lat: ", row[30], "Long: ", row[31]
#             # print "URL: ", row[33], row[35]
            
#             # list_of_col = ["GLOBALEVENTID","SQLDATE MonthYear","Year","FractionDate","Actor1Code","Actor1Name","Actor1CountryCode","Actor1KnownGroupCode","Actor1EthnicCode","Actor1Religion1Code","Actor1Religion2Code","Actor1Type1Code","Actor1Type2Code","Actor1Type3Code", "Actor2Code",  "Actor2Name",  "Actor2CountryCode",  "Actor2KnownGroupCode",   "Actor2EthnicCode",    "Actor2Religion1Code", "Actor2Religion2Code", "Actor2Type1Code", "Actor2Type2Code", "Actor2Type3Code", "IsRootEvent", "EventCode",   "EventBaseCode",   "EventRootCode",  "QuadClass",   "GoldsteinScale",  "NumMentions", "NumSources",  "NumArticles", "AvgTone", "Actor1Geo_Type",  "Actor1Geo_FullName",  "Actor1Geo_CountryCode",  "Actor1Geo_ADM1Code",  "Actor1Geo_Lat",   "Actor1Geo_Long",  "Actor1Geo_FeatureID", "Actor2Geo_Type",  "Actor2Geo_FullName",  "Actor2Geo_CountryCode",   "Actor2Geo_ADM1Code",  "Actor2Geo_Lat",   "Actor2Geo_Long",  "Actor2Geo_FeatureID", "ActionGeo_Type",  "ActionGeo_FullName",  "ActionGeo_CountryCode",  "ActionGeo_ADM1Code",  "ActionGeo_Lat",   "ActionGeo_Long",  "ActionGeo_FeatureID", "DATEADDED",   "SOURCEURL"]

#             # i = 0
#             # for col in list_of_col:
#             #     print list_of_col[i], row[i]
#             #     i+=1
#             # print "Actor1Country: ", row[7]
#             # print "EventBaseCode: ", row[16]
#             # print row

#             #PRINTS ALL URL
#             print "EventBaseCode: ", row[27]
#             print "GoldsteinScale: ", row[30]
#             print "Lat: ", row[39]
#             print "Long: ", row[40]
#             print "URL: ", row[57]


            # import urllib2

            # for line in urllib2.urlopen(row[57]):
            #     print line

## Read the HTML from a URL
# import urllib2

# for line in urllib2.urlopen(row[57]):
#     print line

# list_of_col = ["GLOBALEVENTID","SQLDATE MonthYear","Year","FractionDate","Actor1Code","Actor1Name","Actor1CountryCode","Actor1KnownGroupCode","Actor1EthnicCode","Actor1Religion1Code","Actor1Religion2Code","Actor1Type1Code","Actor1Type2Code","Actor1Type3Code", "Actor2Code",  "Actor2Name",  "Actor2CountryCode",  "Actor2KnownGroupCode",   "Actor2EthnicCode",    "Actor2Religion1Code", "Actor2Religion2Code", "Actor2Type1Code", "Actor2Type2Code", "Actor2Type3Code", "IsRootEvent", "EventCode",   "EventBaseCode",   "EventRootCode",  "QuadClass",   "GoldsteinScale",  "NumMentions", "NumSources",  "NumArticles", "AvgTone", "Actor1Geo_Type",  "Actor1Geo_FullName",  "Actor1Geo_CountryCode",  "Actor1Geo_ADM1Code",  "Actor1Geo_Lat",   "Actor1Geo_Long",  "Actor1Geo_FeatureID", "Actor2Geo_Type",  "Actor2Geo_FullName",  "Actor2Geo_CountryCode",   "Actor2Geo_ADM1Code",  "Actor2Geo_Lat",   "Actor2Geo_Long",  "Actor2Geo_FeatureID", "ActionGeo_Type",  "ActionGeo_FullName",  "ActionGeo_CountryCode",  "ActionGeo_ADM1Code",  "ActionGeo_Lat",   "ActionGeo_Long",  "ActionGeo_FeatureID", "DATEADDED",   "SOURCEURL"]

# print len(list_of_col)


from BeautifulSoup import BeautifulSoup
import urllib2
import requests
import StringIO
import zipfile
import os
import csv

# extracting all zipped csv from gdelt 
# Get URLS
def get_URLs():
    list_of_zipped_files = []

    html_page = urllib2.urlopen("http://data.gdeltproject.org/events/index.html")
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        zipped_csv =  str(link.get('href'))
        list_of_zipped_files.append(zipped_csv)
    # Don't want first two because not csv files and third and last are corrupt  
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
# loop through files in data directory to extract row[27] starting with 14 for PROTESTS
def process_csv(data_dir): 
    for file in os.listdir(data_dir):
        print "Opening File: ", file 
        if not file.lower().endswith('.csv'):
            continue
        with open(data_dir+"/"+file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter='\t')
            for row in readCSV:
                if row[27]:

                    #PRINTS ALL NEED INFO
                    print "EventBaseCode: ", row[27]
                    print "GoldsteinScale: ", row[30]
                    print "Lat: ", row[39]
                    print "Long: ", row[40]
                    print "URL: ", row[57]

                # READ INTO POSTGRES!!!! SEED.P

if __name__ == "__main__":
    data_dir = './data'
    # URLs = get_URLs()
    # get_CSVs(URLs, data_dir)
    process_csv(data_dir)








    # list_of_file_links.append(link_to_csv)
        # zip_ref = zipfile.ZipFile(list_of_file_links[5], 'r')
        # zip_ref.extractall("/Users/Situ/desktop")
        # zip_ref.close()

# print list_of_file_links
        # for link in list_of_file_links:


        # f = open('http://data.gdeltproject.org/events/20160802.export.CSV.zip', 'rb')
        # zip_ref = zipfile.ZipFile(f)
        # zip_ref.extractall('/Users/Situ/src/PROJECT')
        # zip_ref.close()

# print list_of_file_links




# import requests
 
# r = requests.get('http://data.gdeltproject.org/events/20160807.export.CSV.zip')
# f = open('79-13.zip', 'w')
# f.write(r.content)
# f.close()

