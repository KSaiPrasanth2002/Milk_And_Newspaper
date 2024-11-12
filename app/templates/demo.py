keyid = 'rzp_test_kY71FTFw40NENF'
keySecret = 'UAHjDNR6V01i358nRzfJowTK'

import razorpay
client = razorpay.Client(auth=(keyid, keySecret))

data = {
    'amount' : 850*100,
    "currency" : "INR",
    "receipt" : "Feelfreetocode123",
    "notes" : {
        "name" : "Venkata Prasanth",
        "Payment_for" : "Milk"
    }
}

order = client.order.create(data = data)

print(order)