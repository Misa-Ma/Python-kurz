class Ticket:
    def __init__(self,basic_price,seat_number): #tato třída bude sloužit pro cesty autobusem
        self.basic_price = basic_price
        self.seat_number = seat_number

class TrainTicket(Ticket):
    def __init__(self,basic_price,seat_number,fare_class):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class

    def get_price(self):
        if self.fare_class == "business":
            price = self.basic_price * 1.3
        else:
            price = self.basic_price
        return price  
                 
class AirPlaneTicket(TrainTicket):
    def __init__ (self, basic_price, seat_number,fare_class, checkout_luggages):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggages = checkout_luggages

    def get_price(self):
        if self.fare_class == "bussiness":
            price = self.basic_price * 1.5
        else:
            price = self.basic_price
    
        price += self.checkout_luggages * 2000

        return price
    
levnej_vlak = TrainTicket(150, 11, "economy")
drahej_vlak = TrainTicket(150, 11, "bussiness")
levny_letadlo = AirPlaneTicket(6000, 33, "economy", 1)
drahy_letadlo = AirPlaneTicket(6000, 33, "bussiness", 1)

total_price_eco = levnej_vlak.get_price() + levny_letadlo.get_price()
total_price_buss = drahej_vlak.get_price() + drahy_letadlo.get_price()

print(total_price_eco)
print(total_price_buss)

