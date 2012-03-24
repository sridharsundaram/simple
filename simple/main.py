from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers.register_handler import RegisterHandler
from handlers.learner_handler import LearnerHandler
from handlers.home_handler import HomeHandler
from handlers.malldata import MallData
from handlers.officedata import OfficeData

application = webapp.WSGIApplication(
                                     [('/', RegisterHandler),
                                      ('/learner', LearnerHandler),
                                      ('/mall.data', MallData),
                                      ('/office.data', OfficeData),
                                      ('/home', HomeHandler),
                                    ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()