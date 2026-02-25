import os
from cryptography.fernet import Fernet
directory = "/home/Rohit/Impfiles"
key_file = "secret.key"
with open(key_file, "rb") as f:
    key = f.read()
fernet = Fernet(key)
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        if file == key_file or file.endswith(".enc"):
            continue
        try:
            with open(filepath, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(filepath + ".enc", "wb") as f:
                f.write(encrypted_data)
            os.remove(filepath)

            print("Encrypted:", filepath)

        except Exception as e:
            print("Skipped:", filepath, "| Reason:", e)

print("Encryption complete.")
