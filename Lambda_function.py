import json
import urllib.request
import boto3

def lambda_handler(event, context):
    url = "https://api.bluelytics.com.ar/v2/latest"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        compra = data['blue']['value_buy']
        venta = data['blue']['value_sell']
        promedio = round((compra + venta) / 2, 2)
        mensaje = f"A tus amigos puedes venderles los dólares a: ${promedio}"

        SENDER = "yeremyrincon@gmail.com"       # Cambia acá
        RECIPIENT = "yeremyrincon@gmail.com"    # Cambia acá
        AWS_REGION = "us-east-2"
        SUBJECT = "Precio promedio dólar"
        CHARSET = "UTF-8"

        client = boto3.client('ses', region_name=AWS_REGION)
        client.send_email(
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Body': {'Text': {'Charset': CHARSET, 'Data': mensaje}},
                'Subject': {'Charset': CHARSET, 'Data': SUBJECT},
            },
            Source=SENDER,
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Email enviado correctamente')
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Error: {str(e)}")
        }



