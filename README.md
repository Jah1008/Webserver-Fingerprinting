# Webserver-Fingerprinting 
This Python script is a simple tool for web server fingerprinting, designed to be used on a target server. It utilizes the requests library to send an HTTP GET request to a specified web server and then extracts and analyzes the server's response headers. The information collected includes the server's banner, key headers, and an attempt to determine the probable server type based on the order of the 'Date' and 'Server' headers.

Instructions:

1)Run the script in your local environment, ensuring that you have the requests library installed.
2)When prompted, enter the name of the target server you want to fingerprint (e.g., example.com).
3)The script will send an HTTP GET request to the specified server and retrieve the response headers, providing information about the server's configuration.
