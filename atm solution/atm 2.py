def withdraw(balance,request):
		print "current balance" , balance
		if   request > balance:
		        print("Can't give you all this money !!")

		elif request < 0:
		        print("More than zero plz!")

		else:
			balance=balance-request
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
		return balance

balance=500
balance=withdraw(balance,277)
balance=withdraw(balance,30)
balance=withdraw(balance,5)
balance=withdraw(balance,500)
