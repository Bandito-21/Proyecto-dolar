# Proyecto: Envío automático de precio promedio del dólar con AWS Lambda y SES

## ¿Qué construí?

Este proyecto es una función Lambda en AWS que consulta el precio de compra y venta del dólar blue desde una API pública, calcula el promedio y envía un correo electrónico automático con esa información. El envío se programa para que se repita cada 15 minutos usando Amazon EventBridge.

## ¿Cómo usé Amazon Q Developer / AWS?

- Usé AWS Lambda para ejecutar el código Python serverless.
- Usé Amazon SES para enviar los correos electrónicos.
- Usé Amazon EventBridge para programar la ejecución automática cada 15 minutos.
- Configuré IAM Roles con permisos necesarios para SES y Lambda.
- Usé la consola web de AWS para desarrollar y probar la función.

## ¿Qué aprendí?

- Cómo usar AWS Lambda para ejecutar código sin servidor.
- Cómo consumir APIs públicas en Lambda usando `urllib`.
- Cómo enviar emails usando Amazon SES desde Lambda.
- Cómo programar ejecuciones periódicas con EventBridge.
- Configurar permisos y roles IAM correctamente.

## Desafíos técnicos que enfrenté

- Aprender a manejar dependencias en Lambda (no se puede usar `requests` directamente).
- Configurar correctamente SES en modo sandbox y verificar correos.
- Ajustar la función para que corra en la región correcta.
- Programar la función para que se ejecute automáticamente cada 15 minutos.


## Cómo ejecutar el proyecto

1. Crear una función Lambda con el código en `lambda_function.py`.
2. Verificar correos en Amazon SES para permisos de envío.
3. Crear un trigger en EventBridge para ejecutar cada 15 minutos.
4. Probar la función manualmente desde la consola.



