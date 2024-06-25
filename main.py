from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_apk', methods=['POST'])
def generate_apk():
    app_name = request.form['app_name']
    app_logo_path = request.files['app_logo'].filename
    
    # Generate APK here with app_name and app_logo_path
    # Run the necessary commands or scripts to build the APK
    
    # Return the APK file to the user for download
    apk_path = 'path/to/generated.apk'
    return send_file(apk_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
