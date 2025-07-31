import zipfile
import os

def add_to_arhive():
    if not (os.path.exists("flags/excel_ready.flag") and os.path.exists("flags/pdf_ready.flag")):
        return

    folders=['reports/excel_reports','reports/pdf_payslip']
    output_zip='reports/final_reports.zip'
    found_files = []

    with zipfile.ZipFile(output_zip,'w',zipfile.ZIP_DEFLATED) as zipf:
        for folder in folders:
            if not os.path.exists(folder):
                continue

            for root, _, files in os.walk(folder):
                for file in files:
                    if file.endswith(".pdf") or file.endswith(".xlsx"):
                        file_path=os.path.join(root,file)
                        arcname = os.path.relpath(file_path, folder)
                        zipf.write(file_path, os.path.join(folder, arcname))
                        found_files.append(file_path)

    os.remove("flags/excel_ready.flag")
    os.remove("flags/pdf_ready.flag")

    print(f"Files have been archived into {output_zip}")

