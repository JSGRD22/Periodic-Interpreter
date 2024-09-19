def min_remaining_letters(s, word_dict):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    segments = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i):
            test = s[j:i]
            if s[j:i] in word_dict:
                if dp[j] < dp[i]:
                    dp[i] = dp[j]
                    segments[i] = segments[j] + [s[j:i]]
            else:
                if dp[j] + (i - j) < dp[i]:
                    dp[i] = dp[j] + (i - j)
                    segments[i] = segments[j] + [s[j:i].lower()]
    
    # Reconstruct the string with capitalized segments
    result = []
    i = n
    while i > 0:
        if segments[i]:
            word = segments[i][-1]
            if word in word_dict:
                result.append(word.upper())
            else:
                result.append(word)
            i -= len(word)
        else:
            result.append(s[i-1].lower())
            i -= 1
    
    return ''.join(result[::-1])

s = "wfrowfwf"
word_dict = {"wf", "frow"}
print(min_remaining_letters(s, word_dict))
