class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def __str__(self):
        return f'Zaměstnanec {self.name} pracuje jako {self.position}.'

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            print ('Užij si to, ty Pidiuku!')
        else:
            print (f'Nemáš nárok Pidiuku, zbývá ti jen {self.holiday_entitlement} dní.')

class Salesman (Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        super().__init__(name, position, holiday_entitlement)      
        self.car = car                


#class Item:
    #def __init__(self, name, rating):
        #self.name = name
        #self.rating = rating

#class Movie(Item):
    #def __init__(self, name, rating, length):
        #super().__init__(name, rating)   
        #self.length = length
    #def total_length(self):
        #return self.length

#class MovieInSeries(Movie):
    #def __init__(self, name, rating, length, series_name, movie_order):
        #super().__init__(name, rating, length)        
        #self.series_name = series_name
        #self.movie_order = movie_order

#spolecenstvo_prstenu = MovieInSeries ("Společenstvo prstenu", 9.9, 178, "Pán prstenů", 1)
#dve_veze = MovieInSeries ("Dvě věže", 9.9,179, "Pán prstenů",2)        
    
#class Series(Item):
    #def __init__(self, name, rating, episodes, episode_length):
        #super().__init__(name, rating)
        #self.episodes = episodes
        #self.episode_length = episode_length
   # def total_length(self):
    #    return self.episode_length*self.episodes    

#star_trek = Series ("Star Trek: Deep Space Nine", 10, 176, 45)
#print (star_trek.total_length())
# 
class Item:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    def rating_group(self):
        if self.rating <2:
            return "Below average"
        elif self.rating <7:
            return "Average"
        else:
            return "Above average"                          

class Movie(Item):
    def __init__(self, name, rating, length):
        super().__init__(name, rating)   
        self.length = length
    def total_length(self):
        return self.length
    def rating_group(self): #rating group je zde zbytečně
        if self.rating <2:
            return "Below average"
        elif self.rating <7:
            return "Average"
        else:
            return "Above average" 
        
velky_utek = Movie ("Velký útěk", 9.9, 165)   
print (velky_utek.rating_group())     