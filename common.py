from functools import wraps
import time

from quart import Quart, g, websocket, request, session, render_template_string, render_template, redirect, url_for

LOGGEDIN = True

def navigation():
  return f"""
    <h1>
      <a href="{ url_for('root.index') }">/</a> 
      <a href="{ url_for('test.index') }">test/</a> 
      [<a href="{ url_for('test.test_sync') }">test_sync</a> | <a href="{ url_for('test.test_async') }">test_async</a>]
      <br/>
      Current Page: { request.url }
    </h1>
    """

def login_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    print(f"==> Decorator hit! Shots fired from '{f.__name__}'!!")
    if not LOGGEDIN:
      return redirect(url_for('login'))
    return f(*args, **kwargs)
  return decorated
