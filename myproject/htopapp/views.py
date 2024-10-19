from django.http import HttpResponse
import os
import time
import subprocess
import pwd

def home_view(request):
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")

def htop_view(request):
    # Get your name
    name = "Varshitha Y R"

    # Get system username in a safer way
    try:
        username = os.getenv('USER') or pwd.getpwuid(os.getuid()).pw_name
    except Exception:
        username = "Unknown"

    # Get server time in IST
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Get `top` command output (use `top` only in systems where it exists)
    try:
        top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')
    except Exception:
        top_output = "Top command not available in this environment."

    # Create the response string
    response = f"""
    <html>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre><strong>Top Output:</strong><br>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response)
