from number_text_Ringgit_Malaysia import nombor_melayu

ringgit = input('Masukkan nilai/harga: ')

try:
    if '.' in ringgit:
        ringgit = float(ringgit)
    else:
        ringgit = int(ringgit)

    ringgit_text = nombor_melayu.number_to_text(ringgit)
    print(ringgit_text.upper())

except ValueError:
    print("Nilai yang dimasukkan tidak sah. Sila masukkan nombor sahaja.")
