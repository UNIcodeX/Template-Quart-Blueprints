# from quart import Blueprint  # Not really necessary here since it's imported in common.

from common import *

bp = Blueprint("root", __name__)

@bp.route('/login/')
def login():
  return "dummy login page"

@bp.route('/')
@login_required
async def index():
  nav = navigation()
  return await render_template_string("""
  <html>
    <head>
      <title>Index</title>
    <head>
    <body>
      {{ locals['nav']|safe }}
    </body>
  </html>
  """, locals=locals())

@bp.route("/template")
async def template():
  return await render_template("template.html")