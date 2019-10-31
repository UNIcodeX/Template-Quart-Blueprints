# from quart import Blueprint  # Not really necessary here since it's imported in common.

from common import *

bp = Blueprint("test", __name__, url_prefix="/test")

@bp.route("/")
@login_required
def index():
  return navigation()

@bp.route("/_sync/")
@login_required
def _sync():
  nav = navigation()
  return nav

@bp.route("/_async/")
@login_required
async def _async():
  nav = navigation()
  return await render_template_string("""
  <html>
    <head>
      <title>Test - Async</title>
    <head>
    <body>
      {{ locals['nav']|safe }}
    </body>
  </html>
  """, locals=locals())
