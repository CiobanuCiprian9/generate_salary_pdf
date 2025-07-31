from app import myapp
from Services.Create.CreateExcelService import createExcel


@myapp.route("/createAggregatedEmployeeData", methods=['GET'])
def createExelReport():
    createExcel()

    return "Excels generated successfully."