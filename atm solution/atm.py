money = 500
request=277
while request>0:
	if request>=100:
		print "give 100"
		request-=100
	elif request<100 and request>=50:
		print "give 50"
		request-=50
	elif request>=10:
		print "give 10"
		request-=10
	elif request>=5:
		print "give 5"
		request-=5
	elif request<5:
		print "give" , (request)
		request=0


