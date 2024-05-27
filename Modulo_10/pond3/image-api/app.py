from flask import Flask, jsonify, request, make_response
import base64
from io import BytesIO
from PIL import Image, ImageOps

print("Starting API...")

app = Flask(__name__)

def apply_invert_color_filter(base64_string):

    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data))
    
    # Inverter as cores da imagem
    inverted_image = ImageOps.invert(image.convert('RGB'))

    output_buffer = BytesIO()
    inverted_image.save(output_buffer, format='JPEG')
    return base64.b64encode(output_buffer.getvalue()).decode('utf-8')

@app.route("/image", methods=['POST'])
def invert_colors():
    print("Request received, getting body json")
    data = request.json
    print("Extracting image from json body")
    base64_image = data['image']
    print("Applying filter to image")
    inverted_image = apply_invert_color_filter(base64_image)
    print("Returning response with inverted image")
    return jsonify({'image': inverted_image})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
