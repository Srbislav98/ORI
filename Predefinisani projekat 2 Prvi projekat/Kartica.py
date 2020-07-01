class Kreditna_Kartica:
    def __init__(self, q,w,e,r,t,y,u,m,o,p,a,s,d,f,g,h,j,k):
        self.CUSTID = q
        self.BALANCE = w
        self.BALANCEFREQUENCY = e
        self.PURCHASES =r
        self.ONEOFFPURCHASES=t
        self.INSTALLMENTSPURCHASES=y
        self.CASHADVANCE =u
        self.PURCHASESFREQUENCY =m
        self.ONEOFFPURCHASESFREQUENCY =o
        self.PURCHASESINSTALLMENTSFREQUENCY =p
        self.CASHADVANCEFREQUENCY=a
        self.CASHADVANCETRX=s
        self.PURCHASESTRX =d
        self.CREDITLIMIT =f
        self.PAYMENTS=g
        self.MINIMUM_PAYMENTS=h
        self.PRCFULLPAYMENT=j
        self.TENURE=k
        self.ULISTI = False

    def To_String(self):
        return self.CUSTID + "|"+str(self.BALANCE) + "|"+str(self.BALANCEFREQUENCY) + "|"+str(self.PURCHASES) + "|"+str(self.ONEOFFPURCHASES) + "|"+str(self.INSTALLMENTSPURCHASES) + "|"+str(self.CASHADVANCE) + "|" +str(self.PURCHASESFREQUENCY )+ "|"+str(self.ONEOFFPURCHASESFREQUENCY) + "|"+str(self.PURCHASESINSTALLMENTSFREQUENCY) + "|"+str(self.CASHADVANCEFREQUENCY) + "|"+str(self.CASHADVANCETRX) + "|"+str(self.PURCHASESTRX) + "|"+str(self.CREDITLIMIT) + "|"+str(self.PAYMENTS) + "|"+str(self.MINIMUM_PAYMENTS) + "|"+str(self.PRCFULLPAYMENT) + "|"+str(self.TENURE) + "\n"


