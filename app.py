import boto3
import base64
import logging
import traceback,sys
from chalice import Chalice

app = Chalice(app_name='rekognition-chalice')
app.debug = True
 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/rekognition', methods=['POST'], content_types=['application/octet-stream'], cors=True)
def rekognition():
    try:
        logger.info('Invoke Rekognition')

        res = boto3.client(service_name='rekognition', region_name='ap-northeast-1').detect_labels(
            Image = {
                'Bytes': base64.b64decode(app.current_request.raw_body.split(b'base64,')[1]),
            },
            MaxLabels=5,
            MinConfidence=10,
        )
 
        return ','.join([f'{boto3.client(service_name="translate", region_name="ap-northeast-1").translate_text(Text=label["Name"], SourceLanguageCode="en", TargetLanguageCode="ja").get("TranslatedText")} {label["Confidence"]:.2f}%,' for label in res['Labels']])

    except Exception as e:
        tb = sys.exc_info()[2]
        return 'error:{0}'.format(e.with_traceback(tb))
