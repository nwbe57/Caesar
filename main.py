import webapp2
import cgi
from caesar import encrypt




input_form = """
<form method="post" style="padding-left: 30%; font-size: 20px;">
    <!DOCTYPE html>
    <html>
    <head>
        <title>Caesar</title>
    </head>
    <body>
    <label>
        Rotate by:
        <input type="int" name="rotation" style="width: 30px; font-size: 20px;" value="0"/>
    </label>
    <br>
    <textarea input type="text" name="text"
            style="height: 100px; width: 500px; height: 300px; font-size: 20px;">{0}
    </textarea>
    <br>
    <label>
        <input type="submit" value="Submit" style="font-size: 20px;"/>
    </label>
    </body>
    </html>
</form>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.Caesar.com/
    """

    def get(self):
        clean_form = input_form.format("")


        self.response.out.write(clean_form)

    def post(self):
        answer = ''
        usertext = str(self.request.get("text"))
        rotby = int(self.request.get("rotation"))

        answer = encrypt(usertext,rotby)

        self.response.out.write(input_form.format(answer))


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
