# Level 1

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."



def desencript(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    desencripted_text = ''
    for leter in text:
        if alphabet.find(leter) == -1:
            desencripted_text= desencripted_text + leter
        elif alphabet.find(leter) <= 23:
            index = alphabet.find(leter)
            desencripted_text= desencripted_text + alphabet[index+2]
        elif leter == 'y':
            desencripted_text= desencripted_text + 'a'

        else:
            desencripted_text= desencripted_text + 'b'

    print (desencripted_text)
    return desencripted_text

desencript(text)
url = 'map'
new_url = desencript(url)

print (f'Now go to http://www.pythonchallenge.com/pc/def/{new_url}.html')