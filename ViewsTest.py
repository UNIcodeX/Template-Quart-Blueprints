from quart import Blueprint

from common import *

bp = Blueprint("test", __name__, url_prefix="/test")

@bp.route("/")
@login_required
def index():
  return navigation()

@bp.route("/test_sync/")
@login_required
def test_sync():
  nav = navigation()
  return nav

@bp.route("/test_async/")
@login_required
async def test_async():
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
