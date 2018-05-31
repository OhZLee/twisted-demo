# coding: utf-8

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import cgi


class FormPage(Resource):
    isLeaf = True

    def render_GET(self, request):
        return """
        <html>
        <body>
        <form method="POST">
        <input name="form-field" type="text" />
        <input type="submit" />
        </form>
        </body>
        </html>
        """

    def render_POST(self, request):
        print request.args
        return """
        <html>
        <body>You submitted: %s</body>
        </html>
        """ % (cgi.escape(request.args["form-field"][0]),)
        # cgi.escape把输入里面的HTML标签转换为文字


factory = Site(FormPage())
reactor.listenTCP(8000, factory)
reactor.run()
