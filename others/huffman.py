def compress(text, codes):
    compressed = ""
    for c in text:
        code = codes.get(c)
        compressed += code
    return compressed

def decompress(compressed, codes):
    swapped_codes = {v: k for k, v in codes.items()}
    decompressed = ""
    code = ""
    for c in compressed:
        code += c
        value = swapped_codes.get(code)
        if value:
            decompressed += value
            code = ""
    
    print(decompressed)

def aggregate_frequency(text):
    freq: dict = dict()
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)

freq_list = aggregate_frequency("BDDAAAABACEBBBAA")
print(freq_list)

def main():
    codes = {'A': '1', 'B': '00', 'D': '010', 'C': '0110', 'E': '0111'}
    compressed = "0001001011110010110011100000011"
    decompress(compressed, codes)


main()
