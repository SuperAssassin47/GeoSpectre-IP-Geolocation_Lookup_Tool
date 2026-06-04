from app_entry_point import app_entry_point, clear_console
import sys

def main():
    running = True
    while running:
        clear_console()
        print("|| ===== WELCOME TO GEOSPECTRE ===== ||\n")

        print("Please select a module to initiate: \n")

        print("1. GeoSpectre IP Geolocation Tool")

        data = input("> ").strip()

        if data == "1":
            app_entry_point()
        elif data == "exit":
            print("Quitting... Have a nice day!")
            sys.exit()
        else:
            print("[!] Error! No module found.")

if __name__ == "__main__":
    main()
