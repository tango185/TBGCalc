class Card:

    def __init__(self):
        self.tier_list = {"RR", "VG", "PL", "NM", "SS19"}
        self.proc_list = {"P", "T", "S", "C", "PT", "PS", "PC", "TS", "TC", "SC"}
        self.arrow_list = {"U", "D", "L", "R"}
        self.tier = input("Tier: ")
        self.name = input("Name: ")
        self.power = input("POW: ")
        self.toughness = input("TGH: ")
        self.speed = input("SPD: ")
        self.charisma = input("CHA: ")
        self.proc_stat = input("Proc Stat(s): ")
        self.proc_amt = input("Proc Amount: ")
        self.arrow = input("Arrow: ")

    @property
    def tier(self):
        return self._tier

    @tier.setter
    def tier(self, t):
        if not (t in self.tier_list):
            raise Exception("The TIER entered is invalid.")
        self._tier = t

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        if not n:
            raise Exception("The NAME cannot be empty.")
        self._name = n

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, p):
        if not (p > 0):
            raise Exception("POW must be greater than zero.")
        self._power = p

    @property
    def toughness(self):
        return self._toughness

    @toughness.setter
    def toughness(self, t):
        if not (t > 0):
            raise Exception("TGH must be greater than zero.")
        self._toughness = t

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, s):
        if not (s > 0):
            raise Exception("SPD must be greater than zero.")
        self._speed = s

    @property
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, c):
        if not (c > 0):
            raise Exception("CHA must be greater than zero.")
        self._charisma = c

    @property
    def proc_stat(self):
        return self._proc

    @proc_stat.setter
    def proc_stat(self, p):
        if not (p in self.proc_list):
            raise Exception("The PROC STAT entered is invalid.")
        self._proc = p

    @property
    def proc_amt(self):
        return self._proc_amt

    @proc_amt.setter
    def proc_amt(self, p):
        if not (p > 0):
            raise Exception("The PROC AMOUNT must be greater than zero.")

    @property
    def arrow(self):
        return self._arrow

    @arrow.setter
    def arrow(self, a):
        if not (a in self.arrow_list):
            raise Exception("The ARROW entered is invalid.")
        self._arrow = a
