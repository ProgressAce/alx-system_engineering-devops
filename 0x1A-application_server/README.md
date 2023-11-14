# Application server
In this project I use WSGI (web server gateway interface) standards to have my (nginx)web server and (flask)web framework interact with each other. The application server I use is 'gunicorn' and it will serve as the wsgi translator between the two. All those so that my web server can pass requests that need to be served dynamically. Yay!
