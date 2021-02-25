class ErrorResponse(object):
    def __init__(self, formId, rowNumber, errorMessage):
        self.formId = formId
        self.rowNumber = rowNumber
        self.errorMessage = errorMessage

