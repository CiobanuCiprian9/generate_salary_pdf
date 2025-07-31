from app import myapp
from Services.Create.CreatePdfService import createPdf

@myapp.route("/createPdfForEmployees", methods=['GET'])
def createPdfReport():
    createPdf()

    return "PDFs generated successfully"