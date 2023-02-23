import hashlib
import argparse

parser = argparse.ArgumentParser(description="SHA-512 hash cracker")

parser.add_argument("hash", help="SHA-512 hash to crack")
parser.add_argument("wordlist", help="Wordlist File")

args = parser.parse_args()

# Using a wordlist file to crack the hash
with open(args.wordlist, "r") as f:
    for line in f:
        # Removing end-of-line characters
        word = line.strip()

        # Convert every word in wordlist file to SHA-512 hash
        hashed_word = hashlib.sha512(word.encode()).hexdigest()

        # Checking if the hash matches a word in the wordlist file
        if args.hash == hashed_word:
            print("Hash Crack:", word)
            break
