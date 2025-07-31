from app import myapp
from Services.Send.SendExcelService import sendExcel,excelReady

@myapp.route("/sendAggregatedEmployeeData" ,methods=['GET'])
def sendExcelReport():
    sendExcel()
    excelReady()

    return "Excels sent"