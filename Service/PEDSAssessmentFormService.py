import urllib.parse as urlparse
from urllib.parse import parse_qs

from selenium.webdriver.support.ui import Select
from Model.PEDSInterRaiCompleteAlgoScore import *
from Service.ScoreSubmitSection import *


def Login(driver, config):
    driver.get(config["baseUrl"] + config["loginAPI"])

    username = driver.find_element_by_id("loginName")
    username.clear()
    username.send_keys(config["userName"])

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(config["password"])

    providerCode = driver.find_element_by_name("providerCode")
    providerCode.clear()
    providerCode.send_keys(config["providerCode"])

    driver.find_element_by_name("submitButton").click()


def Create_Form(driver, config):
    driver.get(config["baseUrl"] + config["individualListAPI"])
    driver.get(config["baseUrl"] + config["createFormAPI"])

    # DropDown value select
    select = Select(driver.find_element_by_id('assessment.assessmentData.type'))
    select.select_by_value('PEDS_HC')

    select = Select(driver.find_element_by_id('assessment.assessmentData.assessmentVersion'))
    select.select_by_value('9.2.0')
    driver.find_element_by_name("_action_save").click()
    url = driver.current_url

    parsed = urlparse.urlparse(url)
    formId = parse_qs(parsed.query)['formId'][0]

    return formId


def Submit_Sections(driver, row):
    Submit_Section_A(driver, row)
    # Submit_Section_B(driver, row)
    # Submit_Section_C(driver, row)
    # Submit_Section_D(driver, row)
    # Submit_Section_E(driver, row)
    # Submit_Section_F(driver, row)
    # Submit_Section_G(driver, row)
    # Submit_Section_H(driver, row)
    # Submit_Section_I(driver, row)
    # Submit_Section_J(driver, row)
    # Submit_Section_K(driver, row)
    # Submit_Section_L(driver, row)
    # Submit_Section_M(driver, row)
    # Submit_Section_N(driver, row)
    # Submit_Section_O(driver, row)
    # Submit_Section_P(driver, row)
    # Submit_Section_Q(driver, row)
    # Submit_Section_R(driver, row)
    # Submit_Section_S(driver, row)
    # Submit_Section_T(driver, row)


def Submit_Form(driver, row, formId, output, rowNumber):
    driver.find_element_by_name("_action_update_show").click()
    driver.find_element_by_name("_action_submit").click()

    Get_Score_And_Determine_Output(driver, formId, output, row, rowNumber)

    driver.find_element_by_name("_action_confirm").click()


def Get_Score_And_Determine_Output(driver, formId, output, row, rowNumber):
    InterRAI_Complete_Value = driver.find_elements_by_xpath(
        "//table[@class='table table-bordered table-striped ']/tbody/tr[5]/td[2]")[0].text
    InterRAI_Complete_Value_Label = driver.find_elements_by_xpath(
        "//table[@class='table table-bordered table-striped ']/tbody/tr[5]/td[3]")[0].text

    expectedOutput_InterRAI_Complete_Value = row["Expected_Output_Value"]
    expectedOutput_InterRAI_Complete_Value_Label = row["Expected_Output_Value_Label"]
    testStatus = expectedOutput_InterRAI_Complete_Value == InterRAI_Complete_Value and expectedOutput_InterRAI_Complete_Value_Label == InterRAI_Complete_Value_Label
    output.append(PEDSAlgorithmScore(formId, InterRAI_Complete_Value, InterRAI_Complete_Value_Label, testStatus,
                                     expectedOutput_InterRAI_Complete_Value,
                                     expectedOutput_InterRAI_Complete_Value_Label, rowNumber))
