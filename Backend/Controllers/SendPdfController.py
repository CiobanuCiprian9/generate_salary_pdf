from app import myapp
from Services.Send.SendPdfService import sendPdf,pdfReady

@myapp.route("/sendPdfToEmployees" ,methods=['POST'])
def sendPdfToEmployees():
    sendPdf()
    pdfReady()

    return "PDFs sent"