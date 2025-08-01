from app import myapp
from Services.Send.SendExcelService import sendExcel,excelReady

@myapp.route("/sendAggregatedEmployeeData" ,methods=['POST'])
def sendExcelReport():
    sendExcel()
    excelReady()

    return "Excels sent"