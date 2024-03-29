from application import app
import webview
import threading

import watchfiles

def watch_and_reload():
    for _ in watchfiles.watch('templates'):
        window.evaluate_js('window.location.reload()')


window = webview.create_window('App', app, confirm_close=True)
if __name__ == '__main__':
    t = threading.Thread(target=watch_and_reload, daemon=True)
    t.start()
    webview.start()