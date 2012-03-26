from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers.register_handler import RegisterHandler
from handlers.learner_handler import LearnerHandler
from handlers.home_handler import HomeHandler
from handlers.manifest_handler import ManifestHandler

application = webapp.WSGIApplication(
                                     [
                                      (r'/([0-9]{10})', HomeHandler),
                                      ('/', RegisterHandler),
                                      ('/learner', LearnerHandler),
                                      ('/lesson1.mf', ManifestHandler),
                                    ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()