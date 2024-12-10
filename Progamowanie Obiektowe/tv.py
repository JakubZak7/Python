class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channellist = []
        self.volume = 0
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
    
    def set_channel(self,new_channel_no):
        self.channel = new_channel_no
    
    def set_channels(self):
        self.channellist = ["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"]
    
    def set_volume(self,new_volume):
        self.volume = new_volume
        
    def show_channels(self):
        if len(self.channellist) == 0:
            print("There is no channels, add them")
        else:
            indicator = 1
            for i in range(0,len(self.channellist)):
                print(f"{indicator}. {self.channellist[i]}")
                indicator += 1
            
    def show_status(self):
        indexKanalu = self.channel - 1
        if self.is_on == True:
            print(f"TV is on, channel {self.channel}, ({self.channellist[indexKanalu]}), Volume: {self.volume}")
        else:
            print("Tv is off")

        