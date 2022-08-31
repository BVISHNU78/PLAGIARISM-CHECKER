from difflib import SequenceMatcher
with open('TXT.txt') as one_file,open('TXT 2.txt') as two_file:
    data_file = one_file.read()
    data_file2 = two_file.read()
    matches = SequenceMatcher(None,data_file,data_file2).ratio()
    print(f"The plagiarized content is{matches}%")
    print(f"The plagiarized content is {matches*100}%")
