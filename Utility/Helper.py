import csv
import json
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def Read_Config():
    with open('config.json') as config_file:
        return json.load(config_file)


def Get_Driver(config):
    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')

    if config["browser"] == "chrome":
        return webdriver.Chrome(ChromeDriverManager().install(), options=options)
    else:
        raise Exception(f'"{config["browser"]}" is not a supported browser')


def AdjustValue(actualValue, adjustmentValue):
    return str(int(actualValue) + adjustmentValue)


def IsValidRow(value):
    return value != ""


def Write_Output(output, config):
    outputFile = open(config["outputFilePath"], 'w', newline='')

    with outputFile:
        headers = ['Row_Number', 'Form_Id', 'Test_Status', 'Expected_Output_InterRAI_Complete_Value',
                   'Actual_Output_InterRAI_Complete_Value',
                   'Expected_Output_InterRAI_Complete_Value_Label', 'Actual_Output_InterRAI_Complete_Value_Label']
        writer = csv.DictWriter(outputFile, fieldnames=headers)
        writer.writeheader()

        for result in output:
            writer.writerow({'Row_Number': result.rowNumber, 'Form_Id': result.formId, 'Test_Status': result.testStatus,
                             'Expected_Output_InterRAI_Complete_Value': result.expectedOutput_InterRAI_Complete_Value,
                             'Actual_Output_InterRAI_Complete_Value': result.InterRAI_Complete_Value,
                             'Expected_Output_InterRAI_Complete_Value_Label':
                                 result.expectedOutput_InterRAI_Complete_Value_Label,
                             'Actual_Output_InterRAI_Complete_Value_Label': result.InterRAI_Complete_Value_Label})


def Write_Error_Output(errorOutput, config):
    errorOutputFile = open(config["errorOutputFilePath"], 'w', newline='')

    with errorOutputFile:
        headers = ['Form_Id', 'Row_Number', 'Exception_Message']
        writer = csv.DictWriter(errorOutputFile, fieldnames=headers)
        writer.writeheader()

        for error in errorOutput:
            writer.writerow({'Form_Id': error.formId, 'Row_Number': error.rowNumber,
                             'Exception_Message': error.errorMessage})


def Sleep(second):
    time.sleep(float(second))


def Format_Date(dateInMMDDYYYYFormat):
    return datetime.strptime(dateInMMDDYYYYFormat, '%m/%d/%Y').strftime('%m/%d/%Y')