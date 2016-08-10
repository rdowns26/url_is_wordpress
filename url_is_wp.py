"""
This script will return back sites that are definitely wordpress sites and are using http:// 
"""

import urllib2
from bs4 import BeautifulSoup
import re
import csv

def checking_wordpress(url):
	print "The company URL we are checking: ",url
	confirmed_wp = "unsure"

	success = False
	operators = ["http://","https://","http://www."]
	for op in operators:
		try_url = op + url
		print "trying ... ",try_url
		try:
			response = urllib2.urlopen(try_url,timeout=5)
			page_source = response.read()
			success = True
			break
		except urllib2.URLError, e:
			print "error: ",e
			success = False
		except:
			print "unknown error, trying next operator"
			success = False

	if success == False:
		print "all connections failed"
		return confirmed_wp
		

	soup = BeautifulSoup(page_source, 'html.parser')
	for link in soup.find_all('script'):
		script = str(link.get('src'))
		if re.search('wp-',script):
			confirmed_wp = "yes"
			break
		else:
			confirmed_wp = "no"

	return confirmed_wp

reader = csv.reader(open('input_emails.csv'))
accounts = {}
for row in reader:
    email = row[1]
    ad_id = row[0]
    accounts[email] = ad_id

confirmed_wp_domains = []

count=1

for e in accounts:
	print count
	domain_index = e.index('@')
	domain = unicode(e[domain_index+1:])

	wp_check=checking_wordpress(domain)
	if wp_check == "yes":
		confirmed_wp_domains.append(domain)
		status = "wordpress"
		print domain,": WORDPRESS"
	elif wp_check == "unsure":
		print domain,": cannot confirm"
		status = "unsure"
	else:
		print domain,": not wordpress"
		status = "no"

	ad_id = accounts[e]
	accounts[e]=[ad_id,status]
	count += 1

print "CONFIRMED WORDPRESS DOMAINS:"
print confirmed_wp_domains

with open('confirmed_wp_accounts.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in accounts.items():
    	if accounts[key][1] == "wordpress":
       		writer.writerow([key, value])
