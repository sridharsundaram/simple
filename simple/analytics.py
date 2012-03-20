"""
Google Analytics Image URL so that Mobiles without Javascript will
work with Google Analytics
"""
import random

GA_ACCOUNT = "ACCOUNT ID GOES HERE";
GA_PIXEL = "/ga.php";

def googleAnalyticsGetImageUrl(self):
  global GA_ACCOUNT, GA_PIXEL;
  url = "";
  url += GA_PIXEL + "?";
  url += "utmac=" + GA_ACCOUNT;
  url += "&utmn=" + random.randrange(0, 0x7fffffff)

  referer = self.request.header.get("HTTP_REFERER")
  query = self.request.header.get("QUERY_STRING")
  path = self.request.header.get("REQUEST_URI")

  if (empty(referer)) {
    referer = "-";
  }
  url += "&utmr=" + urlencode(referer);

  if (!empty(path)) {
    url += "&utmp=" + urlencode(path);
  }

  url += "&guid=ON";

  return str_replace("&", "&amp;", url);
}
