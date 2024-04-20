# track insurance claims and their status
def trackInsurance(self):
    self.insurance = self.insurance.apply(lambda x: 1 if x > 0 else 0)
    return self.insurance
