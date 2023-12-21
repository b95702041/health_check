import yaml
import requests
import time
import math
#import sys
import os
import collections

request_stats = collections.defaultdict(lambda: {'req_count': 0, 'up_count': 0})

def calculate_availability(url,method, up_count, req_count):
    key = url + method
    request_stats[key]['req_count'] += req_count
    request_stats[key]['up_count'] += up_count
    total_up_count = request_stats[key]['up_count']
    total_req_count = request_stats[key]['req_count']
    number = round(100 * (total_up_count / total_req_count)) if total_req_count > 0 else 0
    #number = round(100 * (request_stats[key]['up_count'] / request_stats[key]['req_count']))
    console_out = (url + " " + method + " has " + str(number) + "% availability percentage")
    print (console_out)

    with open("logging.txt", "w") as myfile:
        myfile.write(console_out + "\n")
    
    return total_up_count, total_req_count

def current_milli_time():
    return round(time.time() * 1000)

def send_request(data, request_stats):
    # headers(dictionary, optional) — The HTTP headers to include in the request.
    #If this field is present, you may assume that the keys and values of this dictionary are strings that are valid HTTP header names and values.
    #If this field is omitted, no headers need to be added to or modified in the HTTP request
    headers = data.get('headers', {})
    
    #If method field is present, you may assume it’s a valid HTTP method (e.g. GET, POST,etc.).
    #If this field is omitted, the default is GET
    method = data.get('method', 'GET')

    # Assuming that the URL is always a valid HTTP or HTTPS address based on instruction.
    url = data['url']

    #If  body  field is present, you should assume it's a valid JSON-encoded string. 
    #You do not need to account for non-JSON request bodies.
    #If this field is omitted, no body is sent in the request
    body = data.get('body', None)
    
    #while True:
    try:
        req_count = 0
        start = current_milli_time()
        if method == 'GET':
            response = requests.get(url, headers=headers, timeout=5)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=body, timeout=5)
            
        roundtrip = current_milli_time() - start
        req_count += 1
        #print ("roundtrip", roundtrip)
        if  200 <= response.status_code < 300 and roundtrip <= 500 :
            up_count = 1
            #print ('UP!')
        else:
            up_count = 0
            #print ('DOWN!')

        #calculate_availability(url, method, up_count, req_count)
        total_up_count, total_req_count = calculate_availability(url, method, up_count, req_count)    
        # Print the counts if needed
        #print(f"Up Count: {total_up_count}, Total Requests: {total_req_count}")
        # Wait 15 seconds before continuing.
        time.sleep(15)
    except requests.RequestException as e:
        return 'ERROR', None

def main(config_file_path):
    # Check if the file exists
    if not os.path.exists(config_file_path):
        print("File doesn't exist.")
        return

    # Check if the file is a YAML file
    _, file_extension = os.path.splitext(config_file_path)
    if file_extension.lower() != '.yaml' and file_extension.lower() != '.yml':
        print("Not a YAML file.")
        return

    # Process the file
    while True:  # Keep visiting URLs until interrupted by Ctrl+C
        try:
            with open(config_file_path, 'r') as file:
                data = yaml.safe_load(file)
                for req in data['requests']:
                    send_request(req, request_stats)
                    pass
        except KeyboardInterrupt:
            print("\nStopping the program.")
            break

if __name__ == "__main__":
    config_file = input("Please enter file name or absolute path name: ")
    main(config_file)