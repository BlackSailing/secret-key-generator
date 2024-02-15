import os
from ecdsa import SigningKey, SECP256k1

def generate_key_pair():
    # Generate a new private key
    private_key = SigningKey.generate(curve=SECP256k1)

    # Derive the corresponding public key
    public_key = private_key.verifying_key

    return private_key, public_key

def main():
    # Generate key pair
    private_key, public_key = generate_key_pair()

    # Get the hex representations of the keys
    private_key_hex = private_key.to_string().hex()
    public_key_hex = "04" + public_key.to_string().hex()

    # Print the keys
    print("Private Key:", private_key_hex)
    print("Public Key(Uncompressed):", public_key_hex)

if __name__ == "__main__":
    main()
