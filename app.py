from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import io

#declaring the exe path for tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        # Convert the uploaded image file to a PIL Image object
        image = Image.open(image_file.stream)
        # Process the image directly without saving it to disk
        extracted_text = extract_text_from_image(image)
        return render_template('result.html', text=extracted_text)
    return render_template('index.html')

def extract_text_from_image(image):
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
