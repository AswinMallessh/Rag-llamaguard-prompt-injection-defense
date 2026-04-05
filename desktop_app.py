import webview
from app import app
from waitress import serve
import threading
import sys

def run_server():
    serve(app, host='127.0.0.1', port=5000)

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    webview.create_window(
        'Secure AI Chatbot',
        'http://127.0.0.1:5000',
        width=800,
        height=700
    )

    webview.start()
    sys.exit()