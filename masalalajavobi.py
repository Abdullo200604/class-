class Public_trans:
    def __init__(self, autobus, metro):
        self.autobus = autobus
        self.metro = metro

    def get_autobus(self):
        return "narx: " + str(self.autobus)
    def seting(self, bag):

        if bag > 0:
            self.metro = bag


class Ticket:
    def __init__(self, ticket_type, price):
        self.ticket_type = ticket_type
        self.price = price

    def chipta_xaqida(self):
        return f"{self.ticket_type} chiptasi narxi: {self.price} so'm"

    def new_narx(self, yangi_narx):
        if yangi_narx > 0:
            self.price = yangi_narx


a1 = Public_trans(500, 1700)
t1 = Ticket("Metro", 1700)

a1.seting(2000)
t1.new_narx(2000)

print(a1.metro)
print(t1.chipta_xaqida())
