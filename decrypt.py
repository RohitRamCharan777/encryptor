import os
from cryptography.fernet import Fernet
directory="/home/Rohit/Impfiles"
key_file="secret.key"
with open(key_file, "rb") as f:
    key=f.read()
fernet=Fernet(key)
for root, dirs, files in os.walk(directory):
    for file in files:
        if not file.endswith(".enc"):
            continue
        filepath=os.path.join(root, file)
        try:
            with open(filepath,"rb") as f:
                encrypted_data=f.read()
            decrypted_data=fernet.decrypt(encrypted_data)
            with open(filepath,"wb") as f:
                f.write(decrypted_data)
            print("Decrypted(filename unchanged):",filepath)
        except Exception as e:
            print("Failed:", filepath, "| Reason:", e)

print("Decryption complete.")
