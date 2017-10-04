from flask import Flask, send_file, request
from tempfile import mkstemp

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw, ImageFilter

app = Flask('memegen')


@app.route('/generate', methods=["GET"])
def generate():
    text = request.args.get('memetext', type=str)
    bg = request.args.get('bg', type=int)
    fontSize = request.args.get('fontsize', type=int)
    color = request.args.get('color', type=str)
    x = request.args.get('x', type=int)
    y = request.args.get('y', type=int)
    blur = request.args.get('blur', type=int)

    _, tempfile = mkstemp('png')
    img = Image.open("gift.png")
    img = img.filter(ImageFilter.GaussianBlur(radius=blur))
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("THSarabunNew.ttf",fontSize)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((x, y), text,
              color, font=font)
    img.save(tempfile, format='png')
    return send_file(tempfile, 'image/png')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
