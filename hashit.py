import hashlib

def MD5(filename: str) -> str:
    
    #filename = input("Enter the file name: ")
    hash = hashlib.md5()
    with open(filename,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            hash.update(byte_block)
    return hash.hexdigest()

def SHA256(filename: str) -> str:
    
    #filename = input("Enter the file name: ")
    hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            hash.update(byte_block)
    return hash.hexdigest()


def main():
    print('Hashing Module!')

if __name__ == "__main__":
    main()