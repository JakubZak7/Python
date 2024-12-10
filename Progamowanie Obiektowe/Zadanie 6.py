class Phone():
    def __init__(self,model,year,hasInductionCharging,battery):
        self.model = model
        self.year = year
        self.hasInductionCharging = hasInductionCharging
        self.battery = battery
        
    def PlugToChargePhone(self):
        if self.hasInductionCharging == True:
            print("Phone has been connected to induction charger")
            self.battery += 20
        else:
            print("Phone has been sucessfully connected to charger")
            self.battery += 10
        
    def UnPlugThePhone(self):
        print("Phone has been sucessfully unpluged from the charger")
        self.battery -= 5
            
    def BatteryStatus(self):
        print(f"The battery has {self.battery} %")
        
def main():
    iphoneX = Phone("X",2015,False,50)
    iphone13 = Phone("13",2020,True,75)
    
    iphoneX.PlugToChargePhone()
    iphoneX.UnPlugThePhone()
    iphoneX.BatteryStatus()
    
    iphone13.PlugToChargePhone()
    iphone13.BatteryStatus()
    

if __name__ == "__main__":
    main()