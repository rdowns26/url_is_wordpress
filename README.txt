INTRODUCTION
------------

This script was created to test if small business websites were built in WordPress or not based on the domain they used for their email address.


REQUIREMENTS
------------

This module requires the following modules:

 * Urllib2 (https://docs.python.org/2/library/urllib2.html)
 * Beautiful Soup 4 (https://pypi.python.org/pypi/beautifulsoup4)
 * Re (https://docs.python.org/2/library/re.html)
 * CSV (https://docs.python.org/2/library/csv.html)


 CONFIGURATION & STEPS
----------------------

1. Change line 48 for file name of email addresses.

2. Run script that ... 
	Reads email address
	Strips off everything but the domain
	Tries to access the domain by adding http://, https://, etc.
	Parses the source code to determine presence of "wp-" which is indicative of a WordPress site
	Returns either WORDPRESS, not wordpress, or cannot confirm if connection failed.
	Writes results to confirmed_wp_accounts.csv
