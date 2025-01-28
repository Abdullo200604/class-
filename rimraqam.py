class RimdanOddiy:
    rim_harflar = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    @classmethod
    def rimni_oddiyga(cls, rim_raqam):
        natija = 0
        oqiymat = 0

        for harf in reversed(rim_raqam):
            qiymat = cls.rim_harflar.get(harf, 0)
            if qiymat < oqiymat:
                natija -= qiymat
            else:
                natija += qiymat
            oqiymat = qiymat

        return natija


rim_raqam = input("Rim raqamini kiriting: ").upper()
print(f"Oddiy son: {RimdanOddiy.rimni_oddiyga(rim_raqam)}")
