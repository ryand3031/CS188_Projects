import hashlib
import asyncio
import sys
import time
from hashlib import sha256

async def main():
    if(len(sys.argv) > 0):
        pass # if you want to add debugging (optional)

    # block header is 80 bytes total; for this assignment, these are dummy values
    # 4 byte field – change upon version upgrade (BIP implementation)
    version = 0b00000000000000000000000000000001

    # 32 byte field – SHA256 output of previous block header (32 bytes)
    hashPrevBlock = 0b0000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111

    # 32 byte field – merkle root of the merkle tree of transactions in the block
    hashMerkleRoot = 0b0000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111

    epochTime = format(int(time.time()), '#0' + str(len(str(int(time.time())))) + '0b')
    print("epochTime:", epochTime)

    # 4 byte field – adjust this to change tolerance of number of leading zeroes that is considered a successful block
    difficulty = 0b00000000000000000000000000000010  # currently set to 2 leading zeroes

    # 4 byte field – change this for each guess
    nonce = 0b00000000000000000000000000001111

    isValid = hashBlock(version, hashPrevBlock, hashMerkleRoot, epochTime, difficulty, nonce)

    print("Difficulty:", difficulty)
    print("Mined block is valid:", isValid)

    return

def sha(blockHeader):
    # takes the blockheader string and returns the sha256 hash sum in binary form

    encodedBH = bytes(str(blockHeader), 'ascii', errors='replace')
    m = hashlib.sha256()
    m.update(encodedBH)
    binaryHash = int(m.hexdigest(), 16)
    binaryRepHash = str(bin(binaryHash))

    while(len(binaryRepHash) < 258):  # 256 bits plus '0b' prefix
        binaryRepHash = '0b0' + binaryRepHash[2:]

    return binaryRepHash

def hashBlock(version, hashPrevBlock, hashMerkleRoot, epochTime, difficulty, nonce):
    #write your code in here
    #put all values into 1 header string
    #header = version + timestamp + hash of previous block + difficulty + merkle root + nonce;
    header = ('{:032b}'.format(version) + epochTime[-32:] + '{:0256b}'.format(hashPrevBlock) +
    '{:032b}'.format(difficulty) + '{:0256b}'.format(hashMerkleRoot) + '{:032b}'.format(nonce) )
    hashOutput = sha(header) #calculate the sha256 hash  based on header
    
    #count leading zeros in the string
    leadingZeros = 0 
    for c in hashOutput[2:]: #start counting at index 2 after the leading '0b'
        if c=='1':
            break
        leadingZeros += 1

    print(f'SHA256 hash output: {hashOutput}') #print hash output
    print(f'Leading Zeros: {leadingZeros}') #print Leading Zeros
    #print(f'Header length: {len(header)} bits or {len(header)/8} bytes') # checking that header was the correct length
   
    #return true if leading zeros is >= difficulty false otherwise
    if leadingZeros>=difficulty: 
        return True
    return False
    



if __name__ == "__main__":
    asyncio.run(main())
