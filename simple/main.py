from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from register import Register

application = webapp.WSGIApplication(
                                     [('/', Register)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()