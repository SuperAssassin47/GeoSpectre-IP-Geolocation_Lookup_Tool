from fileinput import filename

import requests
import os

def get_ip_geolocation(ip):
    url = f"https://ipapi.co/{ip}/json/"
    try:
        response = requests.get(url, timeout=5) # API call with a 5 sec timeout
        response.raise_for_status() # raise error if not a 200 status code
        data = response.json()


        if "error" in data:
            print(f"[!] Error: {data['reason']}")
            return None

        return {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country_name"),
            "ISP": data.get("org"),
            "Latitude": data.get("latitude"),
            "Longitude": data.get("longitude"),
            "Timezone": data.get("timezone")
        }
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: Failed to connect to API --> {e}")
        return None

def display_geolocation(info):
    if not info:
        print("No geolocation information found.")
        return

    print("-" * 40)
    print(f"Geolocation Information for: {info['IP']}")
    print("-" * 40)
    print(f"City: {info['City']}")
    print(f"Region: {info['Region']}")
    print(f"Country: {info['Country']}")
    print(f"ISP: {info['ISP']}")
    print(f"Latitude: {info['Latitude']}")
    print(f"Longitude: {info['Longitude']}")
    print(f"Timezone: {info['Timezone']}")
    print("-" * 40)

def get_appdata_path():
    appdata = os.getenv("APPDATA")
    app_dir = os.path.join(appdata, "GeoSpectre")

    # Create the folder if it doesn't exist
    os.makedirs(app_dir, exist_ok=True)

    return app_dir

def save_results(results):
    save_dir = get_appdata_path()
    file_path = os.path.join(save_dir, "geolocation_results.txt")

    with open(file_path, "w") as f:
        f.write("IP Geolocation Results\n")
        f.write("=" * 50 + "\n")
        for result in results:
            f.write(
                f"IP: {result['IP']}\n"
                f"City: {result['City']}\n"
                f"Region: {result['Region']}\n"
                f"Country: {result['Country']}\n"
                f"ISP: {result['ISP']}\n"
                f"Latitude: {result['Latitude']}\n"
                f"Longitude: {result['Longitude']}\n"
                f"Timezone: {result['Timezone']}\n"
                + ("-" * 50) + "\n" # evaluate as Python code, not as an f-string literal
            )
        print(f"[/] Save results to {file_path}")
