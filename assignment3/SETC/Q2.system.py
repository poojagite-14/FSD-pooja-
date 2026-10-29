from flask import Flask
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return "System Information - Go to /system"

@app.route("/system")
def system_info():
    return (
        "Operating System: " + platform.system() +
        "<br>OS Version: " + platform.version() +
        "<br>Machine: " + platform.machine() +
        "<br>Processor: " + platform.processor()
    )

if __name__ == "__main__":
    app.run(debug=True)