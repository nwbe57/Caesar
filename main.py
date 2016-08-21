import webapp2
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar Cypher</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Caeser Cypher</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"]

class Index(webapp2.RequestHandler):

    def get(self):

            Rotate_by_form = """
            <form action="/Rotate_by" method="post">
                <label>
                    Rotate by:
                    <input type="text" name="rotate-by"/>
                </label>
            </form>
            """

            Input_form = """
                <form action="/Input_form" method="post">
                    <label>
                        <input type="text" name="input-text">
                    </label>
                </form>
            """

            Submit_form = """
                <form action="/Submit_form" method="post">
                    <label>
                        <input type="submit" name="submit-button">
                    </label>
                </form>
            """


        self.response.write('')

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
