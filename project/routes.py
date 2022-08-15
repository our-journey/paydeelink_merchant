from project import app
from flask import render_template, redirect, url_for, flash, request, send_file, send_from_directory, safe_join, abort, Response


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('Homepage.html', title="Home Page")

@app.route('/about', methods=['GET', 'POST'])
def account():
    return render_template('About.html', title="Account")

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/login_merchant', methods=['GET', 'POST'])
def login_merchant():
    return render_template('login_merchant.html')    

@app.route('/merchant_password_update', methods=['GET', 'POST'])
def merchant_password_update():
    return render_template('merchant_password_update.html', brandColor="#007a7c", companyName="Blue Coffee", currency="RM")     

@app.route('/merchant_payment_transaction', methods=['GET', 'POST'])
def merchant_payment_transaction():
    return render_template('merchant_payment_transaction.html', brandColor="#007a7c", companyName="Blue Coffee", currency="RM", errorMessage="This is an error message")      

@app.route('/merchant_payment_transaction_empty', methods=['GET', 'POST'])
def merchant_payment_transaction_empty():
    return render_template('merchant_payment_transaction_empty.html', brandColor="#007a7c", companyName="Blue Coffee", currency="RM")      


@app.route('/merchant_payment', methods=['GET', 'POST'])
def merchant_payment():
    return render_template('merchant_payment.html', brandColor="#007a7c", companyName="Blue Coffee", currency="RM")     

@app.route('/merchant_payment_err', methods=['GET', 'POST'])
def merchant_payment_err():
    return render_template('merchant_payment_err.html', brandColor="#007a7c", companyName="Blue Coffee", currency="RM")     


@app.route('/merchant_profile_setting', methods=['GET', 'POST'])
def merchant_profile_setting():
    return render_template('merchant_profile_settings.html', brandColor="#007a7c", companyName="Blue Coffee", currency="RM")     

@app.route('/password_recovery_invalid', methods=['GET', 'POST'])
def password_recovery_invalid():
    return render_template('password_recovery_invalid.html')    

@app.route('/password_recovery', methods=['GET', 'POST'])
def password_recovery():
    return render_template('password_recovery.html')          

@app.route('/payment_failed', methods=['GET', 'POST'])
def payment_failed():
    return render_template('payment_failed.html', brandColor="#007a7c", companyName="Blue Coffee", currency="RM", 
    errorMessage="Failed to send payment link, please try again")     

@app.route('/payment_success_generate_link', methods=['GET', 'POST'])
def payment_success_generate_link():
    return render_template('payment_success_generate_link.html', brandColor="#007a7c", companyName="Blue Coffee", 
        currency="RM", errorMessage="Failed to send payment link, please try again", paymentLinkValidity="24", paymentLink="https://pay.paydee.link/pl/dz",
        statusPaid="Link generated", statusColorCode="#0793f3", id="000001", formattedCreatedDate= "24 Apr 2022", formattedCreatedTime="10:10 AM", 
        remarks="Coffee Purchcase", referenceNumber = "AB20220425", amountValue="100.00")     



@app.route('/payment_success_generate_qr', methods=['GET', 'POST'])
def payment_success_generate_qr():
    return render_template('payment_success_generate_qr.html', brandColor="#007a7c", companyName="Blue Coffee", 
        currency="RM", errorMessage="Invalid PIN", paymentLinkValidity="24", paymentLink="https://pay.paydee.link/pl/dz",
        statusPaid="Link generated", statusColorCode="#0793f3", id="000001", formattedCreatedDate= "24 Apr 2022", formattedCreatedTime="10:10 AM", 
        remarks="Coffee Purchcase", referenceNumber = "AB20220425", amountValue="100.00", destination="shenni@yahoo.com")     

@app.route('/payment_success_send', methods=['GET', 'POST'])
def payment_success_send():
    return render_template('payment_success_send.html', brandColor="#007a7c", companyName="Blue Coffee", 
        currency="RM", errorMessage="Invalid PIN", paymentLinkValidity="24", paymentLink="https://pay.paydee.link/pl/dz",
        statusPaid="Link generated", statusColorCode="#0793f3", id="000001", formattedCreatedDate= "24 Apr 2022", formattedCreatedTime="10:10 AM", 
        remarks="Coffee Purchcase", referenceNumber = "AB20220425", amountValue="100.00", destination="shenni@yahoo.com")           