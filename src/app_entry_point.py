from ip_geolocation_engine import get_ip_geolocation, display_geolocation, save_results
import sys
import time
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def app_entry_point():
    results = [] # store everything into current session

    running = True
    while running:
        clear_console()
        ip = input("Enter an IP Address or domain name (or type 'exit' to quit): ").strip()

        if ip.lower() == "exit":
            print("\nQuitting... Have a nice day!")
            sys.exit()

        print(f"\nLooking up geolocation for {ip}...\n")
        result = get_ip_geolocation(ip)

        if result:
            display_geolocation(result)
            results.append(result) # save results to the current session

        time.sleep(3)

        if result:
            save = input("\nWould you like to export your results? (y/n): ").strip().lower()
            if save == "y":
                # print("DEBUG RESULTS: ", results)
                save_results(results)
                print("Results have been saved to 'geolocation_results.txt'.")
        again = input("Would you like to lookup another IP? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nThank you for using the IP Geolocation Lookup module! Goodbye.")
