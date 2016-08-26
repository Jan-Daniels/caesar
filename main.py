# Get text from user and the number to rotate the text by for encryption
# https://github.com/Jan-Daniels/caesar.git

import webapp2
import cgi
from caesar import encrypt

# Provide html for retrieving string and rotatation number from user
form="""

<!DOCTYPE html>
<html>
<head>
	<title>Caesar</title>
    <style type="text/css">
        form {
                background-color: #0080FF;
                padding: 10px;
                margin: 0 auto;
                width: 500px;
                font-family: "Times New Roman", Times, serif;
                font: 30px;
                border-radius: 20px;
            }
        textarea {
                margin: 10px 0;
                width: 500px;
                height: 50px;
            }
    </style>
</head>
<body>
    <form method="POST">
        <h1>Enter your text to Encrypt:</h1>
        <textarea type="text" name="text_to_encrypt" value="">%(text_to_encrypt)s</textarea>
        <div>
            <label><h1>Rotate by: <input type="text" name="rotate_number" value="%(rotate_number)s"/></h1></label>
            <input type="submit">
        </div>
        
    </form>
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):

    def write_form(self, text_to_encrypt="", rotate_number=""):
        self.response.out.write(form % { "text_to_encrypt": text_to_encrypt,
										 "rotate_number": rotate_number } )
	
    def get(self):
        self.write_form()

    def post(self):
        original_text = self.request.get("text_to_encrypt")
        text_to_send = cgi.escape(original_text, quote=True)
        rotate_number = self.request.get("rotate_number")

        #Call function to rotate text
        rotated_text = encrypt( text_to_send, int(rotate_number) )

        #Write back out the rotated text
        self.write_form( rotated_text, rotate_number )

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
