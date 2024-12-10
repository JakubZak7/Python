from tv import TV
#! Importowanie danych z pliku do pliku
    
def main():
    tvSalon = TV()
    
    tvSalon.turn_on()
    tvSalon.show_channels()
    tvSalon.set_channels()
    tvSalon.show_status()
    tvSalon.show_channels()
    tvSalon.set_channel(5)
    tvSalon.set_volume(8)
    tvSalon.show_status()
    tvSalon.turn_off()
    
if __name__ == "__main__":
    main()