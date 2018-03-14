# This code uses Python version 3.6.1 for testing

# Host name and port number for server is localhost:8080
# The default page name is set to 'index.html'
# On browser, if type in http://localhost:8080, 
# file index.html is automatically fetched.
# If have other files (eg. 'new.html'),
# type in http://localhost:8080/new.html to retrieve the page
# If the requested file does not exist, forward to error 404 page
# This server only retrieve html files and have http version 1.1


import socket   # Enable socket module

# Create a socket for IPv4 protocol which uses TCP byte stream
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Set socket to be reusable
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# Create a host name and a port number
server_socket.bind(('localhost',8080))
# Specify how many requests can be queue up
server_socket.listen(5)

# Because server has to always listen to requests,
# the socket has to continously accept requests
while True:
    # accept client's request and store client's socket connection and socket address
    client_connection,client_address = server_socket.accept()
    # get the details of the request
    request = client_connection.recv(1024).decode('utf-8')
    # Put each word of the request into a list with white space as the separator
    string_list = request.split(' ')
    # This is the HTTP request method type of the message
    method = string_list[0]
    # Name of the requested file
    requesting_file = string_list[1]
    # Remove the '/' symbol in front of the requested file name
    server_file = requesting_file.strip('/')
    # Because some home page doesn't contain index.html in the request but only a '/'
    # Ex: GET / HTTP/1.1
    # When filtering out the '/', the requested name file will be empty
    # Thus, we have to assume that index.html is the site's homepage
    if (server_file == ''):
        server_file = 'index.html'
    try:
        # Open and read the page's contents
        file = open(server_file,'rb')
        data = file.read()
        file.close()
        # If the file exist and is able to be read, it means that data retrieval is success
        header = 'HTTP/1.1 200 OK\n'
        # Specify the page's type
        header += 'Content-Type: text/html \n\n'
    except Exception as e:
        # If the file is not found in server, throw 404 error message
        header = 'HTTP/1.1 404 Not Found\n\n'
        data = '<html><body><h1>Error 404: File not found</h1></body></html>'.encode('utf-8')
    # Finalize response to the client by adding the header and the contents
    response = header.encode('utf-8')
    response += data
    # Send the response
    client_connection.send(response)
    # Close socket connection
    client_connection.close()
