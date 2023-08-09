class CheckBox:
    def __init__(self, check_box):
        self.element = check_box

    def click(self):
        self.element.click()

    def is_enabled(self):
        self.element.is_enabled()
