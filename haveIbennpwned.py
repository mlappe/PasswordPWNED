import hashlib
import requests



password = input("Please enter your password: ")



hash_func = hashlib.sha1()

hash_func.update(password.encode('utf-8'))
hash = hash_func.hexdigest()

website = f"https://api.pwnedpasswords.com/range/{hash[0:5]}"

print(website)
r = requests.get(website)

answer = r.text

for line in answer.split("\n"):
	h,o = line.split(":")
	if hash[5:].lower() == h.lower():
		print("found")

		print(o)
		break
