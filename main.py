from common import *
from ViewsRoot import bp as vr
from ViewsTest import bp as vt

app = Quart(__name__)

app.register_blueprint(vr)
app.register_blueprint(vt)

if __name__ == "__main__":
  app.run(debug=True)