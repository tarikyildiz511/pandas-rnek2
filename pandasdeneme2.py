import pandas as pd
#30 tane meyve sebze karışık tablo
malzeme =["MUZ","ÇİLEK","KARPUZ","ELMA","SOĞAN","ARMUT","DOMATES","PATATES","PIRASA","SALATALIK",
"MANGO","PAPAYA","PİTAYA","ANANAS","SALATALIK","PORTAKAL","ÜZÜM","MANDALİNA","ERİK","ŞEFTALİ",
"BROKOLİ","ISPANAK","İNCİR","KAVUN","AVOKADO","HİNDİSTAN CEVİZİ","PATLICAN","MARUL","HAVUÇ",
"TURP"]
pd_series = pd.Series(malzeme)
print(pd_series)
