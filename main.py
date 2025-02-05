def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        
    # print(file_contents)
    # print(count_words(file_contents))
    # print (count_char(file_contents))
    report(count_words(file_contents), count_char(file_contents))
    
def count_words(text_in):
    x = text_in.split()
    return len(x)

def count_char(text_in):
    char_count = {}
    for char in text_in.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def report(words_count, char_count):
    print (f"{words_count} words found in the document")
    for k in char_count:
        if k.isalpha() != True:
            continue
        print (f"The '{k}' character was found {char_count[k]} times")
          
main()