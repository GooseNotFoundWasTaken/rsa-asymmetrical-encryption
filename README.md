# RSA Project (User-Friendly Branch)

This is the **easy-to-use version** of my RSA project in Python.  
If you want to see the more bare-bones version, check out the `master` branch  
(it’s probably the most dogshit RSA algorithm ever).

---

## Getting Started

### 1. Generate your keys
Double-click **`rsa-key-generator.py`**.  
This will make two files:  
- **`rsakey.private`** → your secret key (don’t share this!)  
- **`rsakey.public`** → the key you share with friends  

---

### 2. Set up your private key
- Move **`rsakey.private`** into the **`private/`** folder.  
- Delete the placeholder file: **`put your private key here`**.  

---

### 3. Set up your contacts folder
- Inside **`contacts/`**, delete the two example folders and `readme.txt`.  
- Make a new folder with your name (example: `Alice/`).  
- Put your **`rsakey.public`** inside your folder.  

---

## Sending a Message

1. Get your friend’s **`rsakey.public`**.  
2. Inside **`contacts/`**, make a new folder with their name (example: `Bob/`).  
3. Put their **`rsakey.public`** in that folder.  
4. Create a file with your message (example: `message.txt`) in the same folder as **`encrypt.py`**.  
5. Double-click **`encrypt.py`**.  
6. When asked:  
   - Enter the file name (e.g. `message.txt`)  
   - Enter the friend’s name (must match their folder in **contacts**)  
7. Your message will now be encrypted — send it to your friend.  

---

## Receiving a Message

1. Make sure **`rsakey.private`** is inside the **`private/`** folder.  
2. Place the encrypted file you got into the same folder as **`decrypt.py`**.  
3. Double-click **`decrypt.py`**.  
4. Enter the encrypted file’s name.  
5. Your decrypted message will appear!  

---

## Quickstart (TL;DR)
1. Run `rsa-key-generator.py` → get your keys  
2. Put your private key in `private/`, public key in `contacts/YourName/`  
3. To send: put your friend’s public key in `contacts/FriendName/` and run `encrypt.py`  
4. To receive: keep your private key in `private/` and run `decrypt.py`  
