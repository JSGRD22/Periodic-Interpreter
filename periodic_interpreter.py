def alternate_case(s): # format double character elements without affecting singles
    return ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(s)])

def min_remaining_letters(s, word_dict, replacement_dict):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    segments = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i):
            # test = s[j:i]
            if s[j:i] in word_dict:
                if dp[j] < dp[i]:
                    dp[i] = dp[j]
                    segments[i] = segments[j] + [s[j:i]]
            else:
                if dp[j] + (i - j) < dp[i]:
                    dp[i] = dp[j] + (i - j)
                    segments[i] = segments[j] + [s[j:i]]
    
    # Reconstruct the string
    result = []
    # print(segments)
    i = n
    while i > 0:
        if segments[i]:
            word = segments[i][-1]
            if word in word_dict:
                result.append(alternate_case(word))
            else:
                # print(result)
                # print(word)
                result.extend(reversed([alternate_case(replacement_dict[character]) for character in word]))
            i -= len(word)
        else:
            result.append(s[i-1])
            i -= 1
    
    return ''.join(result[::-1])

def main():
    version = "1.1.1"
    word_dict = {
        "h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca",
        "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "y", "zr",
        "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "i", "xe", "cs", "ba", "la", "ce", "pr", "nd",
        "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg",
        "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm",
        "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl", "mc", "lv", "ts", "og"
    }
    replacement_dict = {
        "a": "ar",
        "d": "ds",
        "e": "es",
        "g": "ge",
        "j": "y",
        "l": "I",
        "m": "mn",
        "q": "k",
        "r": "rh",
        "t": "te",
        "x": "xe",
        "z": "zn"
    }
    # Procedure
    # Update dictionary
    # Update version number
    # pyinstaller periodic_interpreter.spec
    print("Periodic Interpreter v" + version + "\n------\n")
    while True:
        s = input(">").lower()

        words = s.split(" ")
        result = ""
        for word in words:
            if word.isalpha() == False:
                print("Error: must contain only letters!")
                break
            result += min_remaining_letters(word, word_dict, replacement_dict)
            result += " "
        else:
            print(result)

if __name__ == "__main__":
    main()
