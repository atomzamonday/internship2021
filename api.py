from imageGetter import logo_url
from http.server import BaseHTTPRequestHandler, HTTPServer
from jsonServer import runServer

url = "https://theinternship.io/"
hostName = "0.0.0.0"
serverPort = 8080

test = []

for line in logo_url:
  test.append(url + line)

score_titles = {"companies": [{"logo": t} for t in test]}

if __name__ == '__main__':
  def handler(path):
    if(path == "/companies"):
      return [200,score_titles]
  runServer(handler)