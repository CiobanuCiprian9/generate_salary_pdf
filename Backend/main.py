from Controllers import GenerateExcelController
from Controllers import GeneratePdfController
from Controllers import SendPdfController
from Controllers import SendExcelController

from app import myapp

if __name__ == "__main__":
    print(myapp.url_map)
    myapp.run(port=8000)