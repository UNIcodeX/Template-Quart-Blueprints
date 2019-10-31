from common import *
from views.ViewsRoot import bp as vr
from views.ViewsTest import bp as vt

app = Quart(__name__)

app.register_blueprint(vr)
app.register_blueprint(vt)

if __name__ == "__main__":
  app.run(debug=True)