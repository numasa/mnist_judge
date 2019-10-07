import base64
import json
import io
import pickle
import boto3

from PIL import Image
from PIL import ImageOps
import numpy
import joblib

def shape_img(base64_image):
    '''
    base64画像を整形する
    '''

    # formatと画像部分に分割
    format, imgstr = base64_image.split(';base64,')
    # base64デコード
    imgbyte = base64.b64decode(imgstr)
    # PIL変換
    imgpil = Image.open(io.BytesIO(imgbyte))
    # グレースケール + 反転
    imgpil_fix = ImageOps.invert(imgpil.convert('L'))
    # ndarrayにして返却
    return numpy.asarray(imgpil_fix)

def judge(event, context):
    '''
    手書き文字をMNIST学習モデルで判定
    '''

    base64_image = json.loads(event['body'])['base64_image']
    if base64_image:
        img = shape_img(base64_image) / 255

    s3 = boto3.client('s3')
    jbl = s3.get_object(Bucket="mnistjudge-static", Key="svc.joblib")['Body'].read()
    jbl_io = io.BytesIO(jbl)
    svc = joblib.load(jbl_io)

    predict = svc.predict(img.reshape((-1, 784)))
    res = {"predict": int(predict)}
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(res),
    }