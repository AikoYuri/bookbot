def main():
    while True:
        try:
            path = input(f"\nInsert the path to a txt file:\nOr press {bcolors.OKBLUE}CTRL+C{bcolors.ENDC} to quit\n")
            with open(path) as f:
                file_contents = f.read()
                break
        except Exception as e:
            print (f"\n{bcolors.FAIL}Wrong filepath/extension:{bcolors.ENDC}\n{e}\n")
            pass
    wline()
    print(file_contents)
    wline()
    report(count_words(file_contents), count_char(file_contents))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

   
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
    print (f"{bcolors.OKGREEN}{words_count}{bcolors.ENDC} words found in the document")
    for k in char_count:
        if k.isalpha() != True:
            continue
        print (f"The {bcolors.OKBLUE}'{k}'{bcolors.ENDC} character was found {bcolors.OKGREEN}{char_count[k]}{bcolors.ENDC} times")

def wline():
    print("\n\n")
    for i in range (0,3):
        print("*******************************************")
    print("\n\n")
             
main()