class PEDSAlgorithmScore(object):
    def __init__(self, formId, InterRAI_Complete_Value, InterRAI_Complete_Value_Label, testStatus,
                 expectedOutput_InterRAI_Complete_Value, expectedOutput_InterRAI_Complete_Value_Label, rowNumber):
        self.formId = formId
        self.InterRAI_Complete_Value = InterRAI_Complete_Value
        self.InterRAI_Complete_Value_Label = InterRAI_Complete_Value_Label
        self.testStatus = "PASS" if testStatus else "FAIL"
        self.expectedOutput_InterRAI_Complete_Value = expectedOutput_InterRAI_Complete_Value
        self.expectedOutput_InterRAI_Complete_Value_Label = expectedOutput_InterRAI_Complete_Value_Label
        self.rowNumber = rowNumber
