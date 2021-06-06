def reverseSentence(sentence):
    arr = sentence.split(" ")
    newstring  = " ".join(reversed(arr))
    return (newstring)
def main():
    inp = input("Enter a sentence: ")
    print(reverseSentence(inp))


if __name__ == "__main__":
    main()