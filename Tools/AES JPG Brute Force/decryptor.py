import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
from itertools import product

# Encryption method configuration
ENCRYPTION_METHODS = {
    "aes-128-ecb": {
        "key_size": 16,
        "iv_size": 0,
        "mode": AES.MODE_ECB,
        "requires_iv": False,
    },
    "aes-128-cbc": {
        "key_size": 16,
        "iv_size": 16,
        "mode": AES.MODE_CBC,
        "requires_iv": True,
    },
    "aes-256-ecb": {
        "key_size": 32,
        "iv_size": 0,
        "mode": AES.MODE_ECB,
        "requires_iv": False,
    },
    "aes-256-cbc": {
        "key_size": 32,
        "iv_size": 16,
        "mode": AES.MODE_CBC,
        "requires_iv": True,
    },
}


def is_jpg_file(data):
    """Check if the data starts with JPG magic number (FF D8 FF)"""
    return len(data) >= 3 and data[:3] == b"\xff\xd8\xff"


def generate_keys(length, mode="lsbytes", allow_letters=True):
    """Generate all possible key combinations"""
    chars = "0123456789" if not allow_letters else "0123456789abcdef"

    for combo in product(chars, repeat=length):
        key_part = "".join(combo)

        if mode == "msbytes":
            # For MSBytes, we want to prioritize higher digits first
            key_part = key_part[::-1]  # Reverse to get the MSB-first behavior

        # Pad to 32 characters with zeros
        if mode == "msbytes":
            key = key_part.ljust(32, "0")
        else:
            key = key_part.rjust(32, "0")

        yield key


def decrypt_file(key_hex, encrypted_data, method):
    """Try to decrypt the file with the given key using specified method"""
    try:
        config = ENCRYPTION_METHODS[method]
        key_bytes = bytes.fromhex(key_hex)

        # Pad/truncate key to required size
        key_bytes = key_bytes.ljust(config["key_size"], b"\x00")[: config["key_size"]]

        if config["requires_iv"]:
            iv = encrypted_data[: config["iv_size"]]
            ciphertext = encrypted_data[config["iv_size"] :]
            cipher = AES.new(key_bytes, config["mode"], iv)
        else:
            ciphertext = encrypted_data
            cipher = AES.new(key_bytes, config["mode"])

        decrypted_data = cipher.decrypt(ciphertext)

        # Try to unpad if using CBC mode
        if "cbc" in method:
            try:
                decrypted_data = unpad(decrypted_data, AES.block_size)
            except ValueError:
                pass  # Keep unpadded data for JPG check

        if is_jpg_file(decrypted_data):
            return decrypted_data

    except Exception as e:
        print(f"Error decrypting with key {key_hex}: {e}")
    return None


def main():
    parser = argparse.ArgumentParser(description="Advanced brute force decryption tool")

    # Required arguments
    parser.add_argument(
        "-in", dest="encrypted_file", required=True, help="Input encrypted file"
    )

    # Key generation options
    parser.add_argument(
        "-d", type=int, required=True, help="Number of hex digits to try (1-32)"
    )
    parser.add_argument(
        "--msbytes", action="store_true", help="Try most significant bytes first"
    )
    parser.add_argument(
        "--no-letters", action="store_true", help="Only use digits in keys (no a-f)"
    )

    # Encryption method options
    parser.add_argument(
        "--enc",
        default="aes-128-ecb",
        choices=ENCRYPTION_METHODS.keys(),
        help="Encryption method to use",
    )

    # Testing options
    parser.add_argument("--test-key", help="Test a specific key")

    args = parser.parse_args()

    # Validate input
    if not 1 <= args.d <= 32:
        print("Error: Number of digits (-d) must be between 1 and 32")
        args.d = 1

    try:
        with open(args.encrypted_file, "rb") as f:
            encrypted_data = f.read()
    except IOError:
        print(f"Error: Could not read file {args.encrypted_file}")
        return

    # Create output directory
    output_dir = "decrypted_output"
    os.makedirs(output_dir, exist_ok=True)

    # Test specific key if provided
    if args.test_key:
        print(f"\nTesting key: {args.test_key} with method {args.enc}")
        decrypted_data = decrypt_file(args.test_key, encrypted_data, args.enc)
        if decrypted_data:
            print("SUCCESS: Key worked!")
            key_clean = (
                args.test_key.rstrip("0")
                if args.test_key.endswith("0")
                else args.test_key
            )
            mode = "msbytes" if args.msbytes else "lsbytes"
            output_file = os.path.join(
                output_dir, f"decrypted_{args.enc}_{mode}_{key_clean}.jpg"
            )
            with open(output_file, "wb") as f:
                f.write(decrypted_data)
            print(f"Saved as {output_file}")
            return
        else:
            print("FAILED: Key did not produce a valid JPG")
            return

    # Brute force
    found = False
    mode = "msbytes" if args.msbytes else "lsbytes"

    print(f"\nStarting brute force with method: {args.enc}")
    print(f"Key generation mode: {mode}")
    print(f"Using {'digits only' if args.no_letters else 'hex characters'}\n")

    for key in generate_keys(args.d, mode, not args.no_letters):
        print(f"Trying {key}", end="\r")
        decrypted_data = decrypt_file(key, encrypted_data, args.enc)

        if decrypted_data:
            print(f"\nFound valid key: {key}")
            key_clean = key[: args.d] if mode == "msbytes" else key[-args.d :]
            output_file = os.path.join(
                output_dir, f"decrypted_{args.enc}_{mode}_{key_clean}.jpg"
            )
            with open(output_file, "wb") as f:
                f.write(decrypted_data)
            print(f"-> Saved decrypted file as {output_file}")
            found = True
            # Continue to find all possible keys

    if not found:
        print("\nNo valid keys found.")


if __name__ == "__main__":
    main()
