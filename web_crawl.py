import urllib2
import pickle
import time
import sys

base_url = 'http://www.bbc.co.uk/sport/0/football/'
start_string = 19221271  # Arsenal's match at start of 2012/2013 season
#########
counter = 0
had_an_error = False
id_url = start_string
#########

try:
	pickle_filename = sys.argv[1]+".p"
	print "\nPickle filename is", pickle_filename
except:
	print "You need to enter a pickle name as an argument. Exiting."
	exit()

print "\nLoading pickle..."

try:
	saved_data = pickle.load(open( pickle_filename, "rb" ) )
	print "\nPickle found and loaded.\n"
except:
	print "\nPickle not found. Creating a new dict.\n"
	saved_data = {}

while had_an_error == False:
	try:
		full_path = base_url + str(id_url)
		response = urllib2.urlopen(full_path)
		html = response.read()
		saved_data[id_url] = html
		print "Successfully pulled",full_path

		# While testing
		if counter==20:
			id_url += 1
		
		id_url += 7
		counter += 1
		time.sleep(3)

	except:
		print "\nThis does not exist:", id_url
		print "\nLast URL to find was this:", id_url-7
		print "\nWe have successfully pulled", counter, "URLs before this error."
		print "\nSaving to pickle, and exiting..."
		pickle.dump (saved_data, open(pickle_filename, 'wb'))
		print "\nExit."
		had_an_error = True
		exit()

