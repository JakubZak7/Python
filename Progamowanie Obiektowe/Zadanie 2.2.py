class Song:
    #! Otwieranie Klasy i inicjowanie jej za pomocą inita
    def __init__(self,performer,title,album,year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year
    
    #? Otwieranie metody __str__ która pozwala na wypisywanie wartości i zwracanie ich w formie tekstu
    def __str__(self):
        return f" Performer: {self.performer} \n Title: {self.title} \n Album: {self.album} \n Year: {self.year} \n"
    

#** Otwieranie funkcji main aby potem wyegzekwować działanie pliku

def main():
    song1 = Song("Belmondawg","CAPTCHA","Hustle As Usual",2021)
    song2 = Song("Kendrick Lamar","Tv off","GNX",2024)
    
    print(song1)
    print(song2)    
        
if __name__ == "__main__":
    main()