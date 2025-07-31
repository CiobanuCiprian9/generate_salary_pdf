from Controllers import GenerateExcelController
from Controllers import GeneratePdfController
from Controllers import SendPdfController
from Controllers import SendExcelController

from app import myapp

if __name__ == "__main__":
    myapp.run(port=8000)