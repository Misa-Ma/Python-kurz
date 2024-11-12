class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_time_to_read(self):
        pass    

class Book (Item):
    def __init__(self, title, price, pages):
        super().__init__(title, price) 
        self.pages = pages

    def get_info(self):
        return f'Kniha:{self.title}\nPočet stránek: {self.pages}\nCena: {self.price} Kč'   

    def get_time_to_read(self, minute_per_pages=4):
        total_minutes = self.pages * minute_per_pages
        total_hours = total_minutes/60
        return round (total_hours,2)

class AudioBook (Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator     

    def get_info(self):
        return f'Kniha: {self.title}\nCena: {self.price} Kč\nDoba poslechu: {self.duration_in_hours} hodin\nPředčítač:{self.narrator}.'  

    def get_time_to_read(self):
        return round (self.duration_in_hours,2)

     
                 
Kniha = Book ("Stopařův průvodce po Galaxii", 250,140)
print (Kniha.get_info())
print (f'Čas potřebný na přečtení knihy a orientace v cestování vesmírem: {Kniha.get_time_to_read()} hodin lidského času.')
Kniha2 = Book (" Kadet Hornblower", 399, 242)
print (Kniha2.get_info())
print (f'Čas potřebný na přečtení knihy: {Kniha2.get_time_to_read()} hodin.')
AudioKniha = AudioBook ("Problém tří těles", 299, 14.4, "Zbyšek Horák")
print (AudioKniha.get_info())
total_time_Kniha2_AudioKniha = Kniha2.get_time_to_read() + AudioKniha.get_time_to_read()
print (f'Celkový čas přečtení Knihy a Poslechu Audio Knihy: {total_time_Kniha2_AudioKniha} hodin')