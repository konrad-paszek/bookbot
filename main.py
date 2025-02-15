def main():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        
        words_counter = count_words(file_contents)
        print(f"{words_counter} words found in the document")
        letter_counter = count_letter(file_contents)
        for k,v in letter_counter.items():
            if k.isalpha():
                print(f"The '{k}' character was found {v} times")
        print("--- End report ---")

def count_letter(text: str) -> dict[str, int]:
    res = dict()
    for sign in text.lower():
        if sign not in res:
            res[sign] = 1
        else:
            res[sign] += 1
    return res


def count_words(text: str) -> int:
    return len(text.split())
if __name__ == '__main__':
   main()