class LogicGate:
    """Create a logic gate. Every logic gate has a label and is able to
    return label and output"""
    def __init__(self, label):
        self.label = label
        self.output = None
        
    def getLabel(self):
        return self.label
        
    def getOutput(self):
        self.output = self.perform_gate_logic()
        return self.output
        
class BinaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pinA = None
        self.pinB = None
        
    def setpinA(self):
        return input("Enter pin A for gate" + self.getLabel() + " -->")
        
    def setpinB(self):
        return input("Enter pin B for gate" + self.getLabel() + " -->")
        
        
class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None
        
    def setpin(self):
        return input("Enter pin for gate" + self.getLabel() + " -->")

class AndGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        self.pinA = self.setpinA()
        self.pinB = self.setpinB()
        if self.pinA == 1 and self.pinB == 1:
            return 1
        else:
            return 0
            
class OrGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)
        
    def perform_gate_logic(self, pinA, pinB):
        self.pinA = self.setpinA()
        self.pinB = self.setpinB()
        if self.pinA == 1 or self.pinB == 1:
            return 1
        else:
            return 0
            
and_gate = AndGate("g1")
print and_gate.perform_gate_logic()
