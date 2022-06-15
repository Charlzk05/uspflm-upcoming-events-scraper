import csv
from itertools import zip_longest
import sys
import requests
from bs4 import BeautifulSoup
import os

error_print = "Something went wrong :/"

def main(cookies, file_name):
    cookies = {
        'MoodleSession': f'{cookies}',
    }

    params = { 
        'view': 'upcoming',
    }

    links_list = []
    titles_list = []
    time_date_list = []

    cookies_error = "Please paste a valid moodle cookies\n"

    try:
        print("\nRequesting...")
        response = requests.get('https://uspflm.com/calendar/view.php', params=params, cookies=cookies)
    except:
        os.system("cls")
        print(cookies_error)
        sys.exit()

    soup = BeautifulSoup(response.text, "html.parser")
    get_links = soup.find_all("a", {"class":"card-link"})
    get_title = soup.find_all("h3", {"class":"name d-inline-block"})
    get_div_date = soup.find("div", {"class", "eventlist my-1"})
    get_time_dates = get_div_date.find_all("div", {"class", "col-11"})

    for get_time_datess in get_time_dates:
        get_time_datess = get_time_datess.text
        if "January" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "February" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "March" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "April" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "May" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "June" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "July" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "August" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "September" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "October" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "November" in get_time_datess:
            time_date_list.append(get_time_datess)
        elif "December" in get_time_datess:
            time_date_list.append(get_time_datess)
        else:
            continue
        
    for get_titles in get_title:
        get_titles = get_titles.string
        titles_list.append(get_titles)
        
    for get_linkss in get_links:
        get_linkss = get_linkss["href"]
        links_list.append(get_linkss)
 
    data = [titles_list, time_date_list, links_list]
    export_data = zip_longest(*data, fillvalue="")
    
    get_file_name = f"{file_name}.csv"
    with open(get_file_name, "w", encoding="ISO-8859-1",newline="") as file:
        header = ("Title", "Date", "Links")
        csv.writer(file).writerow(header)
        csv.writer(file).writerows(export_data)

    os.system("cls")
    print(f"Saved on {get_file_name}\n")

if __name__ == "__main__":
    try:
        print("USPFLM Upcoming Events Scrapper by Charliezkie.\n")
        moodle_cookies = input("Insert your moodle cookies: ")
        file_naming = input("Insert a file name (optional) (press enter to skip): ")
        if file_naming == "":
            main(moodle_cookies, "upcoming events")
        else:
            main(moodle_cookies, file_naming)
    except:
        print(error_print)
