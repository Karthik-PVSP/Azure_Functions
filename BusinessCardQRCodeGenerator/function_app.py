import azure.functions as func
import logging
import qrcode
from io import BytesIO
# Initialize the Function App
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="BusinessVCard")
@app.route(route="BusinessVCard", methods=["GET", "POST"])
def BusinessVCard(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP-triggered Azure Function to generate a QR code for a business vCard.

    Args:
        req (func.HttpRequest): The HTTP request object.

    Returns:
        func.HttpResponse: The HTTP response containing the QR code image or an error message.
    """
   
    logging.info('Python HTTP trigger function processed a request.')
    # Extract parameters from the query string or request body
    name = req.params.get('name')
    tel = req.params.get('tel')
    email = req.params.get('email')
    
    if not name or not tel or not email:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')
        tel = req_body.get('tel')
        email = req_body.get('email')

    if name and tel and email:
        # vCard data
        vcard_data = f"""BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{tel}\nEMAIL:{email}\nEND:VCARD"""
        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(vcard_data)
        qr.make(fit=True)
        # Create an image from the QR code
        img = qr.make_image(fill='black', back_color='white')
        buffered = BytesIO()
        img.save(buffered, format="PNG")

        return func.HttpResponse(buffered.getvalue(), mimetype="image/png")
    else:
        return func.HttpResponse(
            "Pass name, tel, and email in the query string or in the request body.",
            status_code=400
        )
