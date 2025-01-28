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


while True:
    rim_raqam = input("Rim raqamini kiriting (yoki 'exit' yozib chiqib keting): ").upper()
    if rim_raqam == 'EXIT':
        print("Dastur tugatildi.")
        break
    try:
        oddiy_son = RimdanOddiy.rimni_oddiyga(rim_raqam)
        print(f"Oddiy son: {oddiy_son}")
    except Exception as e:
        print("Xato! To'g'ri rim raqamini kiriting.")
