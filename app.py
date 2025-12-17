from flask import Flask, render_template, request, send_from_directory
import qrcode
import os

app = Flask(__name__)

SAVE_FOLDER = 'qr_codes'
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# Serve QR codes folder as static
@app.route('/qr_codes/<filename>')
def qr_file(filename):
    return send_from_directory(SAVE_FOLDER, filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_path = None
    filename = None

    if request.method == 'POST':
        if 'generate' in request.form:
            data = request.form.get('data')
            filename = request.form.get('filename')
            if data and filename:
                qr_img = qrcode.make(data)
                file_path = f"{filename}.png"
                qr_img.save(os.path.join(SAVE_FOLDER, file_path))
                qr_path = f"/qr_codes/{file_path}"  # URL for browser

        elif 'delete' in request.form:
            filename = request.form.get('delete')
            file_path = os.path.join(SAVE_FOLDER, f"{filename}.png")
            if os.path.exists(file_path):
                os.remove(file_path)
                qr_path = None

    return render_template('index.html', qr_path=qr_path, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
