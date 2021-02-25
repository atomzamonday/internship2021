from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = "0.0.0.0"
serverPort = 8080

def getServerObj(handler):
  class Server(BaseHTTPRequestHandler):
    def do_GET(self):
      try:
        [respond_status,respond_body] = handler(self.path)
      except:
        [respond_status,respond_body] = [400,{"message":"not-found"}]
      self.send_response(respond_status)
      self.send_header("Content-type", "application/json")
      self.end_headers()
      self.wfile.write(bytes(json.dumps(respond_body), "utf-8"))
  return HTTPServer((hostName, serverPort), Server)

def runServer(handler):
  webServer = getServerObj(handler)
  try:
    print("Server started http://%s:%s" % (hostName, serverPort))
    webServer.serve_forever()  
  except KeyboardInterrupt:
    pass
  webServer.server_close()
  print("\nServer stopped.")

if __name__ == "__main__":
  def testHandler(path):
    if(path == "/hi"):
      return [200,{"message":"hello!"}]
  runServer(testHandler)