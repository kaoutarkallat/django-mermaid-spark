
import paypalrestsdk
from paypalrestsdk import Payment
import logging

#  var domainName="localhost:8000"
domainName="mermaidspark.com"


# paypalrestsdk.configure({ # for metricgate live
#    "mode": "live",
#     "client_id": 'AfJmvrSwVcoXSUyQyRjkbFznJAewx8igQeTulCEMdRMLePl-Vk8WmVsA_yeQ3eQL9t048-I3lnMSDPpn',
#     "client_secret": 'EEUGVxNVhG51pm1aI5OtMwmGwX7Zvrj-TbfcfOuXqGpeT7msu8pU2jBIWqW6JB3Ebweo_7hKx8G3cMyo',
#   })
# paypalrestsdk.configure({   # for metricgate sandbox
#    "mode": "sandbox",
#     "client_id": 'Aarf6CYHdO1zlGzgnDLOPLn_IxB7YF8fCLnMNjjrIuulX5h9FpEepwzzttKJOMAo4T0tICcSQDndxl89',
#     "client_secret": 'EEph0xNg3t6iI8PLvhryHbhhdfA5J1LCBJZk_00qATq1jCFQu2GPkMtVK1HW_nFwrFz2xGBFs8yIFhCy',
#   })
# paypalrestsdk.configure({   # for mermaidspark sandbox
#    "mode": "sandbox",
#     "client_id": 'AYiMnQ-utd9uGIXEOjaiFTDfnpBY3Qy11Yp-uFdxsBn3Y2kRgSbRKo3xWcdrfw4kyRpoTth5RLQNJJNs',
#     "client_secret": 'EDHFLAuG95xX-Wqr09fZ0N0Z06VY77frDR0H_fA-xSCldPTJksxnhZMIIa8sG025myHCXn-UJFKQpMqx',
#   })
paypalrestsdk.configure({   # for mermaidspark live
   "mode": "live",
    "client_id": 'AWjkWeHqrsgF6yV1N3iFmeOoqh11XU_lXQF73BpEHfaXhTgGiEe8MLG0bQ9pT5t7rCsK0onZlo_zoMqV',
    "client_secret": 'EAQUCDWzeye_5j5yoMq-fDsbA2QZDUxV_onPIwdQVwGWL8pD71sRYQvs1WAujhiFLaJ4e8cL2ZZ3WsxP',
  })


def create_payment(product):
    '''Create Payment'''
    payment:Payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://"+domainName+"/payment/execute",
            "cancel_url": "http://"+domainName+"/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": "5.00",
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {
                "total": "5.00",
                "currency": "USD"},
            "description": "This is the payment transaction description."}]})

    if payment.create():
        print("Payment created successfully")
    else:
        print(payment.error)
    return payment


def authorize_payment(payment: Payment):
    '''Authorize Payment'''
    for link in payment.links:
        if link.rel == "approval_url":
            # Convert to str to avoid Google App Engine Unicode issue
            # https://github.com/paypal/rest-api-sdk-python/pull/58
            approval_url = str(link.href)
            print("Redirect for approval: %s" % (approval_url))
            return {'approval_url': approval_url}
    return None


def execute_payment(payment: Payment):
    '''Execute Payment'''
    payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")

    if payment.execute({"payer_id": "DUFRQ8GWYMJXC"}):
        print("Payment execute successfully")
    else:
        print(payment.error) 


def fetch_payment(id:str)->Payment:
    '''Fetch Payment'''
    # payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")
    payment = paypalrestsdk.Payment.find(id)
    return payment


def get_all_payments():
    # Get List of Payments
    payment_history = paypalrestsdk.Payment.all({"count": 10})
    payments = payment_history.payments
    return payments