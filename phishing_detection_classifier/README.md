This use case is used to whether the URL is phishing URL or not.

A collection of website URLs for 11000+ websites. Each sample has 30 website parameters and a class label identifying it as a phishing website or not (1 or -1).

The data set includes information about:

     1. UsingIP (categorical - signed numeric) : { -1,1 }
	 2.	LongURL (categorical - signed numeric) : { 1,0,-1 }
	 3. ShortURL (categorical - signed numeric) : { 1,-1 }
	 4. Symbol@ (categorical - signed numeric) : { 1,-1 }
	 5. Redirecting// (categorical - signed numeric) : { -1,1 }
	 6. PrefixSuffix- (categorical - signed numeric) : { -1,1 }
	 7. SubDomains (categorical - signed numeric) : { -1,0,1 }
	 8. HTTPS (categorical - signed numeric) : { -1,1,0 }
	 9. DomainRegLen (categorical - signed numeric) : { -1,1 }
	10. Favicon (categorical - signed numeric) : { 1,-1 }
	11. NonStdPort (categorical - signed numeric) : { 1,-1 }
	12. HTTPSDomainURL (categorical - signed numeric) : { -1,1 }
	13. RequestURL (categorical - signed numeric) : { 1,-1 }
	14. AnchorURL (categorical - signed numeric) : { -1,0,1 }
