# app.py
import json
import os
import stripe


def lambda_handler(event, context):
    """Sample Lambda function to handle Stripe Webhook Events

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format with a Webhook Event Payload

        Event doc: https://stripe.com/docs/api/events/object

    Returns
    ------
    Payment Intent: dict

        Return doc: https://stripe.com/docs/api/payment_intents/object
    """
    endpoint_secret = os.getenv('ENDPOINT_SECRET')
    payload = event['body']
    sig_header = event['headers']['Stripe-Signature']

    try:
        webhook = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e

    # Handle the webhook
    if webhook['type'] == 'payment_intent.amount_capturable_updated':
      payment_intent = webhook['data']['object']
    elif webhook['type'] == 'payment_intent.canceled':
      payment_intent = webhook['data']['object']
    elif webhook['type'] == 'payment_intent.created':
      payment_intent = webhook['data']['object']
    elif webhook['type'] == 'payment_intent.payment_failed':
      payment_intent = webhook['data']['object']
    elif webhook['type'] == 'payment_intent.processing':
      payment_intent = webhook['data']['object']
    elif webhook['type'] == 'payment_intent.requires_action':
      payment_intent = webhook['data']['object']
    elif webhook['type'] == 'payment_intent.succeeded':
      payment_intent = webhook['data']['object']
    # ... handle other event types
    else:
      print('Unhandled event type {}'.format(webhook['type']))

    return {
        "statusCode": 200,
        "body": json.dumps(payment_intent),
    }
