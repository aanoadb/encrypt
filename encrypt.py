import random
import string #import modul string bawaan py

chars = " " + string.punctuation + string.digits + string.ascii_letters #var campuran spasi, tanda baca, huruf ASCII (huruf gede kecil), angka
chars = list(chars) #list character di atas
key = chars.copy() #copy dari chars dan disimpan di var key

random.shuffle(key) #agar acak output nya 

#ENCRYPT
plain_text = input("Ketik di sini yang mau di encrypt: ")
cipher_text = "" #Di sini, teks terenkripsi akan disimpan

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

#DECRYPT
#cipher_text = input("Mau decrypt apaan bang: ")
#plain_text = ""

#for letter in cipher_text:
#    index = key.index(letter)
#    plain_text += chars[index]

#print(f"encrypted message: {cipher_text}")
#print(f"original message : {plain_text}")
