from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import sys
import cgi
import base64
import tensorflow as tf
import keras
import numpy as np
import imghdr
import io
import hashlib
 
# simple mitigation to validate model file wasn't tampered
model_hash = "681226449b772fa06ec87c44b9dae724c69530d5d46d5449ff298849e5808b86"

def validate_model(filename):
    with open(filename,"rb") as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest();

        if hash == model_hash:
            return True
        else:
            return False

sys.stdout = open('log.txt','at')

MODEL_FILE = "models/huskymodel.h5"

# if validate_model(MODEL_FILE)==False:
#     print("Invalid model hash. Exiting.")
#     sys.exit("Model failed validation.")

#load the model
MODEL = tf.keras.models.load_model(MODEL_FILE)

print("Model loaded.")

#load the template html
with open("templates/husky.html","rb") as file:
    STATIC_HTML_PAGE = file.read()


#simple web server
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        forwardedfor = str(self.headers['X-Forwarded-For'])
        print(f"GET {forwardedfor}")
       
        self.send_response(200)
        self.end_headers()
        self.wfile.write(STATIC_HTML_PAGE)

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        if int(content_length) > 10000000:
            print("File too big")
            self.send_response(500, "File too big")
            return

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={"REQUEST_METHOD":"POST",
                     "CONTENT_TYPE":self.headers["Content-Type"],
                     })

        filename = str(form['file'].filename)
        forwardedfor = str(self.headers['X-Forwarded-For'])
        print(f"POST {forwardedfor} File: {filename} - ", end = ".")
        data = form["file"].file.read()

        print("Checking image", end = ". ")
        filetype = imghdr.what(file="", h=data)
        if filetype not in ["png","jpeg","gif"]:
             print(f"Unsupported media type:  {filetype}", end = ". ")
             self.send_response(415, "Only png, jpg and gif are supported.")
             return

        num_px = 128

        # read the image 
        from PIL import Image
        img = Image.open(io.BytesIO(data)).convert("RGB")
        img = img.resize((num_px, num_px))

        image = np.array(img)/255.
        image = np.expand_dims(image, axis=0)
 
        result = MODEL.predict(image)
    
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        score_percent = float(result[0]*100)
        score = format(score_percent, '.8f')
        
        response = '{ "score": "' + str(score) +'",'
        if (result > 0.5):
            response += '"text": "It is a husky!" }'
        else:
            response += '"text": "Does not look like a husky to me."}'

        print(f"Response: {response}")
        sys.stdout.flush()
        self.wfile.write(bytes(response,"utf-8"))


httpd = HTTPServer(("localhost", 20080), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, 
       keyfile="server.key", 
       certfile='server.crt', server_side=True)

print("Running.")
httpd.serve_forever()