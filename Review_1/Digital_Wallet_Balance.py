class paytm:

    def __init__(self,balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance

class razorpay:

    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

class process():
    
    def __add__(self,wallets):
        return wallets[0].balance + wallets[1].balance


w1 = paytm(500)
w2 = razorpay(700)
new = process()
w3 = new + (w1,w2)
print(w3)
