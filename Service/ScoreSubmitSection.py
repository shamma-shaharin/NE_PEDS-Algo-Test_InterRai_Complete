from Utility.Helper import *


def Submit_Section_A(driver, row):
    A1a_First = driver.find_element_by_name("answers[0].value")
    A1a_First.clear()
    A1a_First.send_keys(row["A1a_First"])

    A1b_Middle_Initial = driver.find_element_by_name("answers[1].value")
    A1b_Middle_Initial.clear()
    A1b_Middle_Initial.send_keys(row["A1b_Middle_Initial"])

    A1c_Last = driver.find_element_by_name("answers[2].value")
    A1c_Last.clear()
    A1c_Last.send_keys(row["A1c_Last"])

    A1d_Jr_Sr = driver.find_element_by_name("answers[3].value")
    A1d_Jr_Sr.clear()
    A1d_Jr_Sr.send_keys(row["A1d_Jr_Sr"])

    A2_GENDER = driver.find_element_by_xpath(
        "//input[@name='answers[4].refData' and @value='" + AdjustValue(row["A2_GENDER"], 1) + "']")
    A2_GENDER.click()

    A3_BIRTHDATE = driver.find_element_by_name("answers[5].value")
    A3_BIRTHDATE.clear()
    A3_BIRTHDATE = Format_Date(row["A3_BIRTHDATE"])
    A3_BIRTHDATE.send_keys(A3_BIRTHDATE)
    A3_BIRTHDATE.click()

    A4_MARITAL_STATUS_OF_PARENTS = driver.find_element_by_xpath(
        "//input[@name='answers[6].refData' and @value='" + AdjustValue(row["A4_MARITAL_STATUS_OF_PARENTS"], 1) + "']")
    A4_MARITAL_STATUS_OF_PARENTS.click()

    A5a_Social_Security_Number = driver.find_element_by_name("answers[7].value")
    A5a_Social_Security_Number.clear()
    A5a_Social_Security_Number.send_keys(row["A5a_Social_Security_Number"])

    A5b_Medicare_Number = driver.find_element_by_name("answers[8].value")
    A5b_Medicare_Number.clear()
    A5b_Medicare_Number.send_keys(row["A5b_Medicare_Number"])

    A5c_Medicaid_Number = driver.find_element_by_name("answers[9].value")
    A5c_Medicaid_Number.clear()
    A5c_Medicaid_Number.send_keys(row["A5c_Medicaid_Number"])

    A6_FACILITY_AGENCY_PROVIDER_NUMBER = driver.find_element_by_name("answers[10].value")
    A6_FACILITY_AGENCY_PROVIDER_NUMBER.clear()
    A6_FACILITY_AGENCY_PROVIDER_NUMBER.send_keys(row["A6_FACILITY_AGENCY_PROVIDER_NUMBER"])

    A7a_Medicaid = driver.find_element_by_xpath(
        "//input[@name='answers[11].refData' and @value='" + AdjustValue(row["A7a_Medicaid"], 1) + "']")
    A7a_Medicaid.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_B(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_C(driver, row):
    C1_Cog_Skills = driver.find_element_by_xpath(
        "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["C1_Cog_Skills"], 1) + "']")
    C1_Cog_Skills.click()

    C2a_Short_term = driver.find_element_by_xpath(
        "//input[@name='answers[1].refData' and @value='" + AdjustValue(row["C2a_Short_term"], 1) + "']")
    C2a_Short_term.click()

    C2b_Procedural = driver.find_element_by_xpath(
        "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["C2b_Procedural"], 1) + "']")
    C2b_Procedural.click()

    C2c_Situational = driver.find_element_by_xpath(
        "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["C2c_Situational"], 1) + "']")
    C2c_Situational.click()

    C3a_Easily_dist = driver.find_element_by_xpath(
        "//input[@name='answers[4].refData' and @value='" + AdjustValue(row["C3a_Easily_dist"], 1) + "']")
    C3a_Easily_dist.click()

    C3b_Epis_disorg_speech = driver.find_element_by_xpath(
        "//input[@name='answers[5].refData' and @value='" + AdjustValue(row["C3b_Epis_disorg_speech"], 1) + "']")
    C3b_Epis_disorg_speech.click()

    C3c_Ment_func_varies = driver.find_element_by_xpath(
        "//input[@name='answers[6].refData' and @value='" + AdjustValue(row["C3c_Ment_func_varies"], 1) + "']")
    C3c_Ment_func_varies.click()

    C4_Acute_change_mental = driver.find_element_by_xpath(
        "//input[@name='answers[7].refData' and @value='" + AdjustValue(row["C4_Acute_change_mental"], 1) + "']")
    C4_Acute_change_mental.click()

    if row["C5_Change_dec_making"] == '8':
        C5_Change_dec_making = driver.find_element_by_xpath(
            "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["C5_Change_dec_making"], -4) + "']")
    else:
        C5_Change_dec_making = driver.find_element_by_xpath(
            "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["C5_Change_dec_making"], 1) + "']")
    C5_Change_dec_making.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_D(driver, row):
    if IsValidRow(row["D1_Expression"]):
        D1_Expression = driver.find_element_by_xpath(
            "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["D1_Expression"], 0) + "']")
        D1_Expression.click()

    if IsValidRow(row["D3_Hearing"]):
        D3_Hearing = driver.find_element_by_xpath(
            "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["D3_Hearing"], 0) + "']")
        D3_Hearing.click()

    if IsValidRow(row["D4_Vision"]):
        D4_Vision = driver.find_element_by_xpath(
            "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["D4_Vision"], 0) + "']")
        D4_Vision.click()

    if IsValidRow(row["D5_Distance_Vision"]):
        D5_Distance_Vision = driver.find_element_by_xpath(
            "//input[@name='answers[4].refData' and @value='" + AdjustValue(row["D5_Distance_Vision"], 0) + "']")
        D5_Distance_Vision.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_E(driver, row):
    E3a_Wandering = driver.find_element_by_xpath(
        "//input[@name='answers[28].refData' and @value='" + AdjustValue(row["E3a_Wandering"], 0) + "']")
    E3a_Wandering.click()

    E3c_Verbal_abuse = driver.find_element_by_xpath(
        "//input[@name='answers[30].refData' and @value='" + AdjustValue(row["E3c_Verbal_abuse"], 0) + "']")
    E3c_Verbal_abuse.click()

    E3d_Physical_abuse = driver.find_element_by_xpath(
        "//input[@name='answers[31].refData' and @value='" + AdjustValue(row["E3d_Physical_abuse"], 0) + "']")
    E3d_Physical_abuse.click()

    E3f_Socially_Inappro = driver.find_element_by_xpath(
        "//input[@name='answers[33].refData' and @value='" + AdjustValue(row["E3f_Socially_Inappro"], 0) + "']")
    E3f_Socially_Inappro.click()

    E3h_Inappro_public_behav = driver.find_element_by_xpath(
        "//input[@name='answers[35].refData' and @value='" + AdjustValue(row["E3h_Inappro_public_behav"], 0) + "']")
    E3h_Inappro_public_behav.click()

    E3i_Resists_care = driver.find_element_by_xpath(
        "//input[@name='answers[36].refData' and @value='" + AdjustValue(row["E3i_Resists_care"], 0) + "']")
    E3i_Resists_care.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_F(driver, row):
    # F3 = driver.find_element_by_xpath(
    #     "//input[@name='answers[7].refData' and @value='" + AdjustValue(row["F3"], 0) + "']")
    # F3.click()
    # F4 = driver.find_element_by_xpath(
    #     "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["F4"], 0) + "']")
    # F4.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_G(driver, row):
    if row["G2a_bathing"] == '8':
        G2a_bathing = driver.find_element_by_xpath(
            "//input[@name='answers[22].refData' and @value='" + AdjustValue(row["G2a_bathing"], 0) + "']")
    else:
        G2a_bathing = driver.find_element_by_xpath(
            "//input[@name='answers[22].refData' and @value='" + AdjustValue(row["G2a_bathing"], 1) + "']")
    G2a_bathing.click()

    if row["G2b_pers_hygiene"] == '8':
        G2b_pers_hygiene = driver.find_element_by_xpath(
            "//input[@name='answers[24].refData' and @value='" + AdjustValue(row["G2b_pers_hygiene"], 0) + "']")
    else:
        G2b_pers_hygiene = driver.find_element_by_xpath(
            "//input[@name='answers[24].refData' and @value='" + AdjustValue(row["G2b_pers_hygiene"], 1) + "']")
    G2b_pers_hygiene.click()

    if row["G2c_dressing_upper"] == '8':
        G2c_dressing_upper = driver.find_element_by_xpath(
            "//input[@name='answers[26].refData' and @value='" + AdjustValue(row["G2c_dressing_upper"], 0) + "']")
    else:
        G2c_dressing_upper = driver.find_element_by_xpath(
            "//input[@name='answers[26].refData' and @value='" + AdjustValue(row["G2c_dressing_upper"], 1) + "']")
    G2c_dressing_upper.click()

    if row["G2d_dressing_lower"] == '8':
        G2d_dressing_lower = driver.find_element_by_xpath(
            "//input[@name='answers[28].refData' and @value='" + AdjustValue(row["G2d_dressing_lower"], 0) + "']")
    else:
        G2d_dressing_lower = driver.find_element_by_xpath(
            "//input[@name='answers[28].refData' and @value='" + AdjustValue(row["G2d_dressing_lower"], 1) + "']")
    G2d_dressing_lower.click()

    if row["G2e_walking"] == '8':
        G2e_walking = driver.find_element_by_xpath(
            "//input[@name='answers[30].refData' and @value='" + AdjustValue(row["G2e_walking"], 0) + "']")
    else:
        G2e_walking = driver.find_element_by_xpath(
            "//input[@name='answers[30].refData' and @value='" + AdjustValue(row["G2e_walking"], 1) + "']")
    G2e_walking.click()

    if row["G2f_locomotion"] == '8':
        G2f_locomotion = driver.find_element_by_xpath(
            "//input[@name='answers[32].refData' and @value='" + AdjustValue(row["G2f_locomotion"], 0) + "']")
    else:
        G2f_locomotion = driver.find_element_by_xpath(
            "//input[@name='answers[32].refData' and @value='" + AdjustValue(row["G2f_locomotion"], 1) + "']")
    G2f_locomotion.click()

    if row["G2g_transfer_toilet"] == '8':
        G2g_transfer_toilet = driver.find_element_by_xpath(
            "//input[@name='answers[34].refData' and @value='" + AdjustValue(row["G2g_transfer_toilet"], 0) + "']")
    else:
        G2g_transfer_toilet = driver.find_element_by_xpath(
            "//input[@name='answers[34].refData' and @value='" + AdjustValue(row["G2g_transfer_toilet"], 1) + "']")
    G2g_transfer_toilet.click()

    if row["G2h_toilet_use"] == '8':
        G2h_toilet_use = driver.find_element_by_xpath(
            "//input[@name='answers[36].refData' and @value='" + AdjustValue(row["G2h_toilet_use"], 0) + "']")
    else:
        G2h_toilet_use = driver.find_element_by_xpath(
            "//input[@name='answers[36].refData' and @value='" + AdjustValue(row["G2h_toilet_use"], 1) + "']")
    G2h_toilet_use.click()

    if row["G2k_Transfers"] == '8':
        G2k_Transfers = driver.find_element_by_xpath(
            "//input[@name='answers[42].refData' and @value='" + AdjustValue(row["G2k_Transfers"], 0) + "']")
    else:
        G2k_Transfers = driver.find_element_by_xpath(
            "//input[@name='answers[42].refData' and @value='" + AdjustValue(row["G2k_Transfers"], 1) + "']")
    G2k_Transfers.click()

    if row["G2l_eating"] == '8':
        G2l_eating = driver.find_element_by_xpath(
            "//input[@name='answers[44].refData' and @value='" + AdjustValue(row["G2l_eating"], 0) + "']")
    else:
        G2l_eating = driver.find_element_by_xpath(
            "//input[@name='answers[44].refData' and @value='" + AdjustValue(row["G2l_eating"], 1) + "']")
    G2l_eating.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_H(driver, row):
    H2_Urinary_Collection_Device = driver.find_element_by_xpath(
        "//input[@name='answers[1].refData' and @value='" + AdjustValue(row["H2_Urinary_Collection_Device"], 1) + "']")
    H2_Urinary_Collection_Device.click()

    # if row["H1_bladder_cont"] == '8':
    #     H1_bladder_cont = driver.find_element_by_xpath(
    #         "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["H1_bladder_cont"], -1) + "']")
    # else:
    #     H1_bladder_cont = driver.find_element_by_xpath(
    #         "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["H1_bladder_cont"], 1) + "']")
    # H1_bladder_cont.click()
    #
    # if row["H3_bowel_cont"] == '8':
    #     H3_bowel_cont = driver.find_element_by_xpath(
    #         "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["H3_bowel_cont"], -1) + "']")
    # else:
    #     H3_bowel_cont = driver.find_element_by_xpath(
    #         "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["H3_bowel_cont"], 1) + "']")
    # H3_bowel_cont.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_I(driver, row):
    I1f_Disease_Diagnoses_Other = driver.find_element_by_xpath(
        "//input[@name='answers[5].refData' and @value='" + AdjustValue(row["I1f_Disease_Diagnoses_Other"], 0) + "']")
    I1f_Disease_Diagnoses_Other.click()

    I1g_Spinal_cord_dysfunction = driver.find_element_by_xpath(
        "//input[@name='answers[7].refData' and @value='" + AdjustValue(row["I1g_Spinal_cord_dysfunction"], 0) + "']")
    I1g_Spinal_cord_dysfunction.click()

    I1h_Cerebral_palsy = driver.find_element_by_xpath(
        "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["I1h_Cerebral_palsy"], 0) + "']")
    I1h_Cerebral_palsy.click()

    I1i_Macro_Microcephaly = driver.find_element_by_xpath(
        "//input[@name='answers[9].refData' and @value='" + AdjustValue(row["I1i_Macro_Microcephaly"], 0) + "']")
    I1i_Macro_Microcephaly.click()

    I1k_Muscular_dystrophies = driver.find_element_by_xpath(
        "//input[@name='answers[11].refData' and @value='" + AdjustValue(row["I1k_Muscular_dystrophies"], 0) + "']")
    I1k_Muscular_dystrophies.click()

    I1l_Seizure_Disorder = driver.find_element_by_xpath(
        "//input[@name='answers[12].refData' and @value='" + AdjustValue(row["I1l_Seizure_Disorder"], 0) + "']")
    I1l_Seizure_Disorder.click()

    I1m_Traumatic_brain_injury = driver.find_element_by_xpath(
        "//input[@name='answers[13].refData' and @value='" + AdjustValue(row["I1m_Traumatic_brain_injury"], 0) + "']")
    I1m_Traumatic_brain_injury.click()

    I1n_Neuro_Other = driver.find_element_by_xpath(
        "//input[@name='answers[14].refData' and @value='" + AdjustValue(row["I1n_Neuro_Other"], 0) + "']")
    I1n_Neuro_Other.click()

    I1p_Congenital_heart_disorder = driver.find_element_by_xpath(
        "//input[@name='answers[17].refData' and @value='" + AdjustValue(row["I1p_Congenital_heart_disorder"],
                                                                         0) + "']")
    I1p_Congenital_heart_disorder.click()

    I1q_Disease_Diagnoses_Other = driver.find_element_by_xpath(
        "//input[@name='answers[18].refData' and @value='" + AdjustValue(row["I1q_Disease_Diagnoses_Other"], 0) + "']")
    I1q_Disease_Diagnoses_Other.click()

    I1u_Cystic_Fibrosis = driver.find_element_by_xpath(
        "//input[@name='answers[23].refData' and @value='" + AdjustValue(row["I1u_Cystic_Fibrosis"], 0) + "']")
    I1u_Cystic_Fibrosis.click()

    I1v_Disease_Diagnoses_Other = driver.find_element_by_xpath(
        "//input[@name='answers[24].refData' and @value='" + AdjustValue(row["I1v_Disease_Diagnoses_Other"], 0) + "']")
    I1v_Disease_Diagnoses_Other.click()

    I1y_Disease_Diagnoses_Other = driver.find_element_by_xpath(
        "//input[@name='answers[28].refData' and @value='" + AdjustValue(row["I1y_Disease_Diagnoses_Other"], 0) + "']")
    I1y_Disease_Diagnoses_Other.click()

    I1bb_Disease_Diagnoses_Other = driver.find_element_by_xpath(
        "//input[@name='answers[32].refData' and @value='" + AdjustValue(row["I1bb_Disease_Diagnoses_Other"], 0) + "']")
    I1bb_Disease_Diagnoses_Other.click()

    I1ii_Disease_Diagnoses_other = driver.find_element_by_xpath(
        "//input[@name='answers[40].refData' and @value='" + AdjustValue(row["I1ii_Disease_Diagnoses_other"], 0) + "']")
    I1ii_Disease_Diagnoses_other.click()

    I1kk_Cancer = driver.find_element_by_xpath(
        "//input[@name='answers[43].refData' and @value='" + AdjustValue(row["I1kk_Cancer"], 0) + "']")
    I1kk_Cancer.click()

    I1nn_Explicit_terminal_prognosis = driver.find_element_by_xpath(
        "//input[@name='answers[46].refData' and @value='" + AdjustValue(row["I1nn_Explicit_terminal_prognosis"],
                                                                         0) + "']")
    I1nn_Explicit_terminal_prognosis.click()

    I1oo_Failure_to_Thrive = driver.find_element_by_xpath(
        "//input[@name='answers[47].refData' and @value='" + AdjustValue(row["I1oo_Failure_to_Thrive"], 0) + "']")
    I1oo_Failure_to_Thrive.click()

    I1pp_Renal_Failure = driver.find_element_by_xpath(
        "//input[@name='answers[48].refData' and @value='" + AdjustValue(row["I1pp_Renal_Failure"], 0) + "']")
    I1pp_Renal_Failure.click()

    I1qq_Disease_Diagnoses_Other = driver.find_element_by_xpath(
        "//input[@name='answers[49].refData' and @value='" + AdjustValue(row["I1qq_Disease_Diagnoses_Other"], 0) + "']")
    I1qq_Disease_Diagnoses_Other.click()

    I1rr_Disease_Diagnoses_Other = driver.find_element_by_xpath(
        "//input[@name='answers[51].refData' and @value='" + AdjustValue(row["I1rr_Disease_Diagnoses_Other"], 0) + "']")
    I1rr_Disease_Diagnoses_Other.click()

    I1ss_Disease_Diagnoses_Other = driver.find_element_by_xpath(
        "//input[@name='answers[53].refData' and @value='" + AdjustValue(row["I1ss_Disease_Diagnoses_Other"], 0) + "']")
    I1ss_Disease_Diagnoses_Other.click()

    # Other_Disease_Modal = driver.find_element_by_xpath("//input[@class='btn btn-default'][2]")
    # Other_Disease_Modal.click()
    # Sleep(0.5)
    #
    # I2_Diagnosis = driver.find_element_by_id("diagnosisModal_iI2Diagnosis")
    # I2_Diagnosis.clear()
    # I2_Diagnosis.send_keys(row["I2_Diagnosis"])
    #
    # I2_Disease_Code_Dropdown_btn = driver.find_element_by_xpath("//button[@data-id='diagnosisModal_iI2DiseaseCode']")
    # I2_Disease_Code_Dropdown_btn.click()
    # I2_Disease_Code_Option = driver.find_element_by_xpath(
    #     "//ul[@class='dropdown-menu inner']/li["
    #     + MapI2DiseaseCodeByValue(row["I2_Disease_Code"])
    #     + "]/a/span[@class='text']")
    # I2_Disease_Code_Option.click()
    #
    # I2_Coding_System = driver.find_element_by_id(MapI2CodingSystemIdByValue(row["I2_Coding_System"]))
    # I2_Coding_System.click()
    #
    # I2_ICD_Code = driver.find_element_by_id("diagnosisModal_iI2IcdCode")
    # I2_ICD_Code.clear()
    # I2_ICD_Code.send_keys(row["I2_ICD_Code"])
    #
    # Other_Disease_Modal_Continue_Btn = driver.find_element_by_xpath(
    #     "//div[@class='form-group col-sm-12']/button[@class='btn btn-default']")
    # Other_Disease_Modal_Continue_Btn.click()
    # Sleep(0.5)

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_J(driver, row):
    Add_New_Surgery_Modal = driver.find_element_by_xpath(
        "//div[@id='iJ15']/div[@class='col-sm-12 text-right']/input[@class='btn btn-default']")
    Add_New_Surgery_Modal.click()
    Sleep(0.5)

    J2_sur_name = driver.find_element_by_id("surgeryModal_iJ15Surgery")
    J2_sur_name.clear()
    J2_sur_name.send_keys(row["J2_sur_name"])

    J2_sur_year = driver.find_element_by_id("surgeryModal_iJ15Year")
    J2_sur_year.clear()
    J2_sur_year.send_keys(row["J2_sur_year"])

    Continue_New_Surgery_Modal = driver.find_element_by_xpath("//button[@class='btn btn-default']")
    Continue_New_Surgery_Modal.click()
    Sleep(0.5)

    J7d_Pain_Control = driver.find_element_by_xpath(
        "//input[@name='answers[31].refData' and @value='" + AdjustValue(row["J7d_Pain_Control"], 1) + "']")
    J7d_Pain_Control.click()

    J8a_Instability_of_Conditions = driver.find_element_by_xpath(
        "//input[@name='answers[32].refData' and @value='" + AdjustValue(row["J8a_Instability_of_Conditions"],
                                                                         1) + "']")
    J8a_Instability_of_Conditions.click()

    J8c_End_stage = driver.find_element_by_xpath(
        "//input[@name='answers[34].refData' and @value='" + AdjustValue(row["J8c_End_stage"], 1) + "']")
    J8c_End_stage.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_K(driver, row):
    K3_Mode_of_Nutritional_Intake = driver.find_element_by_xpath(
        "//input[@name='answers[5].refData' and @value='" + AdjustValue(row["K3_Mode_of_Nutritional_Intake"], 0) + "']")
    K3_Mode_of_Nutritional_Intake.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_L(driver, row):
    # L1_Most_severe_pressure_ulcer = driver.find_element_by_xpath(
    #     "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["L1_Most_severe_pressure_ulcer"],
    #                                                                     0) + "']")
    # L1_Most_severe_pressure_ulcer.click()
    #
    # L4_Major_Skin_Problems = driver.find_element_by_xpath(
    #     "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["L4_Major_Skin_Problems"], 1) + "']")
    # L4_Major_Skin_Problems.click()

    L1_Most_Severe_Pressure_Ulcer = driver.find_element_by_xpath(
        "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["L1_Most_Severe_Pressure_Ulcer"], 0) + "']")
    L1_Most_Severe_Pressure_Ulcer.click()
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_M(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_N(driver, row):
    N2a_Chemotherapy = driver.find_element_by_xpath(
        "//input[@name='answers[8].refData' and @value='" + AdjustValue(row["N2a_Chemotherapy"], 0) + "']")
    N2a_Chemotherapy.click()

    N2b_Hemodialysis = driver.find_element_by_xpath(
        "//input[@name='answers[9].refData' and @value='" + AdjustValue(row["N2b_Hemodialysis"], 0) + "']")
    N2b_Hemodialysis.click()

    N2c_Peritoneal_dialysis = driver.find_element_by_xpath(
        "//input[@name='answers[10].refData' and @value='" + AdjustValue(row["N2c_Peritoneal_dialysis"], 0) + "']")
    N2c_Peritoneal_dialysis.click()

    N2e_IV_medication = driver.find_element_by_xpath(
        "//input[@name='answers[12].refData' and @value='" + AdjustValue(row["N2e_IV_medication"], 0) + "']")
    N2e_IV_medication.click()

    N2f_Routine_Oxygen_Therapy = driver.find_element_by_xpath(
        "//input[@name='answers[13].refData' and @value='" + AdjustValue(row["N2f_Routine_Oxygen_Therapy"], 0) + "']")
    N2f_Routine_Oxygen_Therapy.click()

    N2g_Radiation = driver.find_element_by_xpath(
        "//input[@name='answers[14].refData' and @value='" + AdjustValue(row["N2g_Radiation"], 0) + "']")
    N2g_Radiation.click()

    N2h_Nasopharyngeal_suct = driver.find_element_by_xpath(
        "//input[@name='answers[15].refData' and @value='" + AdjustValue(row["N2h_Nasopharyngeal_suct"], 0) + "']")
    N2h_Nasopharyngeal_suct.click()

    N2i_Tracheotomy_Care = driver.find_element_by_xpath(
        "//input[@name='answers[16].refData' and @value='" + AdjustValue(row["N2i_Tracheotomy_Care"], 0) + "']")
    N2i_Tracheotomy_Care.click()

    N2j_Transfusion = driver.find_element_by_xpath(
        "//input[@name='answers[17].refData' and @value='" + AdjustValue(row["N2j_Transfusion"], 0) + "']")
    N2j_Transfusion.click()

    N2k_Ventilator_or_respirator = driver.find_element_by_xpath(
        "//input[@name='answers[18].refData' and @value='" + AdjustValue(row["N2k_Ventilator_or_respirator"], 0) + "']")
    N2k_Ventilator_or_respirator.click()

    N2l_Wound_Care = driver.find_element_by_xpath(
        "//input[@name='answers[19].refData' and @value='" + AdjustValue(row["N2l_Wound_Care"], 0) + "']")
    N2l_Wound_Care.click()

    N2n_Urinary_Catheter_Care = driver.find_element_by_xpath(
        "//input[@name='answers[21].refData' and @value='" + AdjustValue(row["N2n_Urinary_Catheter_Care"], 0) + "']")
    N2n_Urinary_Catheter_Care.click()

    N2o_Comatose = driver.find_element_by_xpath(
        "//input[@name='answers[22].refData' and @value='" + AdjustValue(row["N2o_Comatose"], 0) + "']")
    N2o_Comatose.click()

    N2q_CPAP_BiPAP = driver.find_element_by_xpath(
        "//input[@name='answers[24].refData' and @value='" + AdjustValue(row["N2q_CPAP_BiPAP"], 0) + "']")
    N2q_CPAP_BiPAP.click()

    N2r_Breathing_vest = driver.find_element_by_xpath(
        "//input[@name='answers[25].refData' and @value='" + AdjustValue(row["N2r_Breathing_vest"], 0) + "']")
    N2r_Breathing_vest.click()

    N2s_Other = driver.find_element_by_xpath(
        "//input[@name='answers[26].refData' and @value='" + AdjustValue(row["N2s_Other"], 0) + "']")
    N2s_Other.click()

    N6a_Inpatient = driver.find_element_by_id("answers[49].value")
    N6a_Inpatient.send_keys(row["N6a_Inpatient"])

    N6d_Psych_Fac = driver.find_element_by_id("answers[52].value")
    N6d_Psych_Fac.send_keys(row["N6d_Psych_Fac"])

    N6e_LTC_Fac = driver.find_element_by_id("answers[53].value")
    N6e_LTC_Fac.send_keys(row["N6e_LTC_Fac"])

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_O(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_P(driver, row):
    # P1_Areas_Inf_Help_d1 = driver.find_element_by_xpath(
    #     "//input[@name='answers[6].refData' and @value='" + AdjustValue(row["P1_Areas_Inf_Help_d1"], 0) + "']")
    # P1_Areas_Inf_Help_d1.click()
    #
    # P1_Areas_Inf_Help_d2 = driver.find_element_by_xpath(
    #     "//input[@name='answers[7].refData' and @value='" + AdjustValue(row["P1_Areas_Inf_Help_d2"], 0) + "']")
    # P1_Areas_Inf_Help_d2.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_Q(driver, row):
    # Q1a_Home_Disrepair = driver.find_element_by_xpath(
    #     "//input[@name='answers[0].refData' and @value='" + AdjustValue(row["Q1a_Home_Disrepair"], 1) + "']")
    # Q1a_Home_Disrepair.click()
    #
    # Q1b_Home_Squalid = driver.find_element_by_xpath(
    #     "//input[@name='answers[1].refData' and @value='" + AdjustValue(row["Q1b_Home_Squalid"], 1) + "']")
    # Q1b_Home_Squalid.click()
    #
    # Q1c_Home_Inad_heat_cool = driver.find_element_by_xpath(
    #     "//input[@name='answers[2].refData' and @value='" + AdjustValue(row["Q1c_Home_Inad_heat_cool"], 1) + "']")
    # Q1c_Home_Inad_heat_cool.click()
    #
    # Q1d_Home_Lack_pers_safe = driver.find_element_by_xpath(
    #     "//input[@name='answers[3].refData' and @value='" + AdjustValue(row["Q1d_Home_Lack_pers_safe"], 1) + "']")
    # Q1d_Home_Lack_pers_safe.click()
    #
    # Q1e_Home_Lim_access = driver.find_element_by_xpath(
    #     "//input[@name='answers[4].refData' and @value='" + AdjustValue(row["Q1e_Home_Lim_access"], 1) + "']")
    # Q1e_Home_Lim_access.click()

    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_R(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_S(driver, row):
    driver.find_element_by_name("_action_update_next").click()


def Submit_Section_T(driver, row):
    T2_Assessment_Date_Picker_Element = driver.find_element_by_name("answers[1].value")
    T2_Assessment_Date_Picker_Element.clear()
    T2_Assessment_Date = Format_Date(row["T2_Assessment_Date"])
    T2_Assessment_Date_Picker_Element.send_keys(T2_Assessment_Date)
    T2_Assessment_Date_Picker_Element.click()

    # driver.find_element_by_name("_action_update_next").click()
