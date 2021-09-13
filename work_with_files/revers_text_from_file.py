result = ''
with open('text.txt') as file:
    for line in file:
        result += line.strip()

print(result[::-1])
# Input:
# Read secret_message.txt and print out the first letter of each line.
# Need Output:
# .enil hcae fo rettel tsrif eht tuo tnirp dna txt.egassem_terces daeR
