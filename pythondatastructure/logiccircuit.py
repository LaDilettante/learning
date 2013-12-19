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

    def getpinA(self):
        if self.pinA == None:
            return input("Enter pin A for gate" + self.getLabel() + " -->")
        else:
            return self.pinA.getFrom().getOutput()

    def getpinB(self):
        if self.pinB == None:
            return input("Enter pin B for gate" + self.getLabel() + " -->")
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        # If pin A is empty, set pinA to connector
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.getpinA()
        b = self.getpinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class NandGate(BinaryGate):
    def __init__(self,label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.getpinA()
        b = self.getpinB()
        if not (a == 1 and b == 1):
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.getpinA()
        b = self.getpinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NorGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.getpinA()
        b = self.getpinB()
        if not(a == 1 or b == 1):
            return 0
        else:
            return 1

class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def getpin(self):
        if self.pin == None:
            return input("Enter pin for gate" + self.getLabel() + " -->")
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class NotGate(UnaryGate):
    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.getpin()
        if a == 1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3, g4)

    g1a = NandGate("G1a")
    g2a = NandGate("G2a")
    g3a = AndGate("G3a")
    c1a = Connector(g1a, g3a)
    c2a = Connector(g2a, g3a)

    print g4.getOutput()
    print g3a.getOutput()

if __name__ == "__main__":
    main()
