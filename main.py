import webapp2
import cgi
from caesar import encrypt

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
</head>
<body>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.Caesar.com/
    """

    def get(self):

        input_form = """
        <form action="/input" method="post" style="padding-left: 30%; font-size: 20px;">
            <label>
                Rotate by:
                <input type="int" name="rotation" style="width: 30px; font-size: 20px;"/>
            </label>
            <br>
            <textarea input type="text" name="text"
                    style="height: 100px; width: 500px; height: 300px; font-size: 20px;">
            </textarea>
            <br>
            <label>
                <input type="submit" value="Submit" style="font-size: 20px;"/>
            </label>
        </form>
        """

        response = page_header + input_form + page_footer
        self.response.write(response)

class Output(webapp2.RequestHandler):
    """ Handles requests coming in to '/input'
        e.g. www.Caesar.com/input
    """

    # def get(self):
    #
    #     output_form = """
    #     <form action="/output" method="post" style="padding-left: 30%; font-size: 20px;">
    #         <label>
    #             Rotate by:
    #             <input type="int" name="rotation" style="width: 30px; font-size: 20px;"/>
    #         </label>
    #         <br>
    #         <textarea input type="text" name="usertext"
    #                 style="height: 100px; width: 500px; height: 300px; font-size: 20px;">
    #         </textarea>
    #         <br>
    #         <label>
    #             <input type="submit" value="Submit" style="font-size: 20px;"/>
    #         </label>
    #     </form>
    #     """
    #
    #     response = page_header + output_form + page_footer
    #     self.response.write(response)

    def post(self):

        usertext = str(self.request.get("text"))
        rotby = int(self.request.get("rotation"))

        answer = encrypt(usertext, rotby)

        self.response.write(answer)
        #self.redirect('/output')
        #usertext.replace(usertext, answer)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/input', Output),
    ('/output', Output)
], debug=True)
