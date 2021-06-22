msg = input("Enter your message! ")

key = "abcdefghijklmnopqrstuvwxyz0123456789 !"
val = key[:: -1]

e_msg = dict(zip(key , val))


enc_msg = "".join([e_msg[words] for words in msg.lower()])

print((enc_msg))

decrypter = dict(zip(val , key))
dec_msg = "".join([e_msg[words] for words in enc_msg.lower()])
print((dec_msg))