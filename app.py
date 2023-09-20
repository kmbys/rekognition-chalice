from chalice import Chalice

app = Chalice(app_name='rekognition-chalice')


@app.route('/rekognition', methods=['POST'], content_types=['application/octet-stream'], cors=True)
def rekognition():
    return '猫 69%, ごみ袋 31%'
