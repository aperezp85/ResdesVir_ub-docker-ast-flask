from flask import Flask, render_template, request
import socket
import os

app = Flask(__name__)

def get_asterisk_status():
    try:
        host = os.environ.get('ASTERISK_HOST', 'asterisk')
        port = int(os.environ.get('ASTERISK_PORT', 5038))
        user = os.environ.get('ASTERISK_USER', 'flask')
        password = os.environ.get('ASTERISK_PASS', 'flask123')

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((host, port))

        banner = s.recv(1024).decode()

        login = f"Action: Login\r\nUsername: {user}\r\nSecret: {password}\r\n\r\n"
        s.send(login.encode())
        response = s.recv(1024).decode()

        ping = "Action: Ping\r\n\r\n"
        s.send(ping.encode())
        pong = s.recv(1024).decode()

        s.close()

        if 'Pong' in pong:
            return 'Conectado y activo'
        return 'Conectado'

    except Exception as e:
        return f'Sin conexion: {str(e)}'

@app.route('/')
def index():
    ip = request.remote_addr
    asterisk_status = get_asterisk_status()
    return render_template('index.html', ip=ip, asterisk_status=asterisk_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
