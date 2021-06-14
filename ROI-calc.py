class ROI():
	def __init__(self, rental_income, down_payment, closing_cost, maintenance, insurance, HOA, mortgage, improvments, investment):
		self.rental_income = rental_income
		self.expenses = expenses
		self.mortgage = mortgage
		self.maintenance = maintenance
		self.improvments = improvments
		self.investment = investment

    def rental_income(self):
        while True:
            self.rent = input("\nWhat's the expected monthly rent for this property?")
        if self.rental_income.lower() == 'quit':
            break
        if not self.rental_income.isdigit():
            print("Please enter a valid amount")
            continue
        else:
            return int(self.rental_income)

    def down_payment(self):
        while True:
            self.down_payment = input("\nWhat will be the down payment?")
        if self.down_payment.lower() == 'quit':
            break
        elif not self.down_payment.isdigit():
            print("Please enter a amount")
            continue
        else:
            return int(self.down_payment)
  
    def closing_cost(self):
        while True:
            self.closing_cost = input("\nWhat are the expected closing costs?")
        if self.closing_cost.lower() == 'quit':
            break
        elif not self.closing_cost.isdigit():
            print("Please enter a valid amount")
            continue
        else:
            return int(self.closing_cost)
  
    def mortgage(self):
        while True:
            self.mortgage = input("\nWhat's the expected monthly mortgage amount?")
        if self.mortgage.lower() == 'quit':
            break
        elif not self.mortgage.isdigit():
            print("Enter a valid amount.")
            continue
        else:
            return int(self.mortgage)

    def HOA(self):
        while True:
            self.HOA = input("\nWhat's the expected monthly amount for HOA costs??")
        if self.HOA.lower() == 'quit':
            break
        elif not self.HOA.isdigit():
            print("Enter a valid amount.")
            continue
        else:
            return int(self.HOA)
  
    def Insurance(self):
        while True:
            self.Insurance = input("\nWhat's the expected monthly insurance amount?")
        if self.Insurance.lower() == 'quit':
            break
        elif not self.Insurance.isdigit():
            print("Enter a valid amount.")
            continue
        else:
            return int(self.Insurance)

    def management(self):
        while True:	
            self.management = input("\nWhat percentage of the monthly rent will be paid to property management")		
        if self.management.lower() == 'quit':
            break
        elif not self.management.isdigit():
            print("Please enter a valid amount.")
            continue
        else:
            return int(self.rent) * int(self.management) / 100

    def maintenance(self):
        while True:
            self.maintenance = input('\nWhat are your expected monthly maintenance fees?')
        if self.maintenance.lower() == 'quit':
            break
        elif not self.maintenance.isdigit():
            print("Enter a valid amount.")
            continue
        else:
            return int(self.maintenance)

    def improvements(self):
        while True:
            self.improvements=input("\nHow much money will need to be spent on improvements?")
        if self.improvements.lower() == 'quit':
            break
        elif not self.improvements.isdigit():
            print("Please enter a valid amount.")
            continue
        else:
            return int(self.improvements)

    def estimatedROI(self):
        self.expenses = int(self.mortgage) + int(self.maintenance) + int(self.management) + int(self.HOA) + int(self.Insurance)
        self.investment = int(self.down_payment) + int(self.closing_cost) + int(self.improvements)
        print(f"Your estimate ROI is {round((int(self.rental_income) - self.expenses)*12 / self.investment *100,2)}%.")

    def Return():
	   Return = ROI()

	while True:
		response = input("\nTo see your return on investment type 'yes' or type 'no' to quit")

		if responce.lower() == 'yes':
			estimatedROI.rental_income()
			estimatedROI.mortgage()
			estimatedROI.maintenance()
			estimatedROI.management()
			estimatedROI.down_payment()
			estimatedROI.closing_cost()
			estimatedROI.HOA()
			estimatedROI.Insurance()
			estimatedROI.improvements()
			break
		elif response.lower() == 'quit':
			break

	Return()
    
execute()
  

  
