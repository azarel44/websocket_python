# websocket_python

This code uses Python version 3.6.1 for testing.
Host name and port number for server is localhost:8080.
The default page name is set to 'index.html'.
On browser, if type in http://localhost:8080, file index.html is automatically fetched.
If have other files (eg. 'new.html'), type in http://localhost:8080/new.html to retrieve the page.
If the requested file does not exist, forward to error 404 page.
This server only retrieve html files and have http version 1.1
