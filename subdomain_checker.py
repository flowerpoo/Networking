import requests
import time
from tabulate import tabulate

# Function for scanning subdomains
def domain_scanner(domain_name, sub_domnames):
    print('-----------Scanner Started-----------')
    while True:
        results = []  # List to store results

        # Loop for getting URLs
        for subdomain in sub_domnames:
            url = f"https://{subdomain}.{domain_name}"  # Making URL by putting subdomain one by one

            try:
                # Sending GET request to the URL
                response = requests.get(url)

                # If the URL is valid (status code 200), store it as "up"
                status = "up" if response.status_code == 200 else "down"
            except requests.ConnectionError:
                # If URL is invalid, store it as "down"
                status = "down"

            # Append the subdomain and its status to the results list
            results.append({"Subdomain": subdomain, "Status": status})

        # Display the results in tabular format
        table = tabulate(results, headers="keys", tablefmt="grid")
        print(table)
        time.sleep(60) # Wait for 1 minute before checking again
        print("next cycle") #message after one itration
       

# Main function
if __name__ == '__main__':
    domain_name= input("Enter the Domain Name: ")  # Input the domain name
    print('\n')

    # Opening the subdomain text file
    with open('subdomain.txt', 'r') as file:
       sub_domain = file.read().splitlines()  # Reading the file and splitting lines to get subdomains

    domain_scanner(domain_name, sub_domain) # function call