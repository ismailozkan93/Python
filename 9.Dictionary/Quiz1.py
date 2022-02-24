#soru1
file=open("kelimeler.txt")

def kelimeler_uygulamasi():
    kelime=dict()
    for index,line in enumerate(file):
        if(len(line)>19):
            kelime[line]=len(line)
    else:
        print(kelime)

kelimeler_uygulamasi()

#soru2
def uzunluk_kelimeler():
    kelime = dict()
    for index, line in enumerate(file):
        if (len(line) > 19):
            if not(len(line)) in kelime:
                kelime[len(line)] = [line]
            else:
                kelime[len(line)].append(line)
        print(kelime)
    return kelime

uzunluk_kelimeler()