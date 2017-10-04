from flask import Flask, send_file, request
from tempfile import mkstemp

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

app = Flask('memegen')


@app.route('/generate', methods=["GET"])
def generate():
    text = request.args.get('text', type=str)
    bg = request.args.get('bg', type=int)
    fontsize = request.args.get('fontsize', type=int)
    color = request.args.get('color', type=str)
    x = request.args.get('x', type=int)
    y = request.args.get('y', type=int)

    _, tempfile = mkstemp('png')
    img = Image.open("gift.png")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("THSarabunNew.ttf", 36)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0), "สวัสดีครับสั้นส้นกตัญญูรู้คุรา่ฟสดากฟหฟกดหฟกดกหฟด\nkjdkljflkdjfkljdklfjdlksf",
              '#123456', font=font)
    img.save(tempfile, format='png')
    return send_file(tempfile, 'image/png')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
