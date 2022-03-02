class House:
    def __init__(self, location, house_type, deal_type, price, ccompletion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = ccompletion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
            , self.price, self.completion_year)

houses = []
house1 = House ("downtown", "Apartment", "Montly", "150$", "2010y")
house2= House ("midtown", "House", "Montly", "80$", "2007y")
house3 = House ("uptown", "Apartment", "Sold", "1B$", "2018y")

houses.append(house1)
houses.append(house2)