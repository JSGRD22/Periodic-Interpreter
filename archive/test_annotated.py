# https://pythontutor.com/render.html#code=def%20min_remaining_letters%28s,%20word_dict%29%3A%0A%20%20%20%20n%20%3D%20len%28s%29%20%20%23%20Get%20the%20length%20of%20the%20input%20string%0A%20%20%20%20dp%20%3D%20%5Bfloat%28'inf'%29%5D%20*%20%28n%20%2B%201%29%20%20%23%20Initialize%20the%20dp%20array%20with%20infinity%0A%20%20%20%20dp%5B0%5D%20%3D%200%20%20%23%20Base%20case%3A%20no%20remaining%20letters%20for%20an%20empty%20string%0A%20%20%20%20segments%20%3D%20%5B%5B%5D%20for%20_%20in%20range%28n%20%2B%201%29%5D%20%20%23%20Initialize%20the%20segments%20array%20to%20store%20the%20words%0A%0A%20%20%20%20for%20i%20in%20range%281,%20n%20%2B%201%29%3A%20%20%23%20Iterate%20over%20each%20position%20in%20the%20string%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%28i%29%3A%20%20%23%20Iterate%20over%20each%20possible%20starting%20position%20for%20the%20substring%0A%20%20%20%20%20%20%20%20%20%20%20%20debug_testword%20%3D%20s%5Bj%3Ai%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20s%5Bj%3Ai%5D%20in%20word_dict%3A%20%20%23%20Check%20if%20the%20substring%20s%5Bj%3Ai%5D%20is%20a%20valid%20word%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20dp%5Bj%5D%20%3C%20dp%5Bi%5D%3A%20%20%23%20If%20using%20this%20word%20results%20in%20fewer%20remaining%20letters%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20dp%5Bi%5D%20%3D%20dp%5Bj%5D%20%20%23%20Update%20dp%5Bi%5D%20to%20the%20minimum%20remaining%20letters%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20segments%5Bi%5D%20%3D%20segments%5Bj%5D%20%2B%20%5Bs%5Bj%3Ai%5D%5D%20%20%23%20Update%20the%20segments%20array%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%20%20%23%20If%20the%20substring%20s%5Bj%3Ai%5D%20is%20not%20a%20valid%20word%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20dp%5Bj%5D%20%2B%20%28i%20-%20j%29%20%3C%20dp%5Bi%5D%3A%20%20%23%20Check%20if%20adding%20the%20length%20of%20the%20invalid%20word%20results%20in%20fewer%20remaining%20letters%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20dp%5Bi%5D%20%3D%20dp%5Bj%5D%20%2B%20%28i%20-%20j%29%20%20%23%20Update%20dp%5Bi%5D%20to%20include%20the%20length%20of%20the%20invalid%20word%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20segments%5Bi%5D%20%3D%20segments%5Bj%5D%20%2B%20%5Bs%5Bj%3Ai%5D.lower%28%29%5D%20%20%23%20Add%20the%20invalid%20word%20in%20lowercase%20to%20the%20segments%20array%0A%0A%20%20%20%20%23%20Reconstruct%20the%20string%20with%20capitalized%20segments%0A%20%20%20%20result%20%3D%20%5B%5D%20%20%23%20Initialize%20the%20result%20list%20to%20store%20the%20final%20string%0A%20%20%20%20i%20%3D%20n%20%20%23%20Start%20from%20the%20end%20of%20the%20string%0A%20%20%20%20while%20i%20%3E%200%3A%20%20%23%20Iterate%20backwards%20through%20the%20string%0A%20%20%20%20%20%20%20%20if%20segments%5Bi%5D%3A%20%20%23%20If%20there%20are%20segments%20at%20position%20i%0A%20%20%20%20%20%20%20%20%20%20%20%20word%20%3D%20segments%5Bi%5D%5B-1%5D%20%20%23%20Get%20the%20last%20word%20in%20the%20segments%20array%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20word%20in%20word_dict%3A%20%20%23%20Check%20if%20the%20word%20is%20in%20the%20dictionary%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result.append%28word.upper%28%29%29%20%20%23%20Capitalize%20the%20word%20and%20add%20it%20to%20the%20result%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20result.append%28word%29%20%20%23%20Add%20the%20word%20as%20is%20%28in%20lowercase%29%20to%20the%20result%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20-%3D%20len%28word%29%20%20%23%20Move%20the%20index%20back%20by%20the%20length%20of%20the%20word%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20result.append%28s%5Bi-1%5D.lower%28%29%29%20%20%23%20Add%20the%20remaining%20character%20in%20lowercase%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20-%3D%201%20%20%23%20Move%20the%20index%20back%20by%20one%0A%0A%20%20%20%20return%20''.join%28result%5B%3A%3A-1%5D%29%20%20%23%20Join%20the%20result%20list%20into%20a%20string%20and%20reverse%20it%0A%0As%20%3D%20%22wfrowfwf%22%0Aword_dict%20%3D%20%7B%22wf%22,%20%22frow%22%7D%0Aprint%28min_remaining_letters%28s,%20word_dict%29%29%0A%23%20bad%20case%3A%20WF%20row%20WF%20WF%20-%3E%20expected%20for%20greedy%0A%23%20good%20case%3A%20w%20FROW%20WF%20WF&cumulative=false&curInstr=225&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
def min_remaining_letters(s, word_dict):
    n = len(s)  # Get the length of the input string
    dp = [float('inf')] * (n + 1)  # Initialize the dp array with infinity
    dp[0] = 0  # Base case: no remaining letters for an empty string
    segments = [[] for _ in range(n + 1)]  # Initialize the segments array to store the words

    for i in range(1, n + 1):  # Iterate over each position in the string
        for j in range(i):  # Iterate over each possible starting position for the substring
            debug_testword = s[j:i]
            if s[j:i] in word_dict:  # Check if the substring s[j:i] is a valid word
                if dp[j] < dp[i]:  # If using this word results in fewer remaining letters
                    dp[i] = dp[j]  # Update dp[i] to the minimum remaining letters
                    segments[i] = segments[j] + [s[j:i]]  # Update the segments array
            else:  # If the substring s[j:i] is not a valid word
                if dp[j] + (i - j) < dp[i]:  # Check if adding the length of the invalid word results in fewer remaining letters
                    dp[i] = dp[j] + (i - j)  # Update dp[i] to include the length of the invalid word
                    segments[i] = segments[j] + [s[j:i].lower()]  # Add the invalid word in lowercase to the segments array

    # Reconstruct the string with capitalized segments
    result = []  # Initialize the result list to store the final string
    i = n  # Start from the end of the string
    while i > 0:  # Iterate backwards through the string
        if segments[i]:  # If there are segments at position i
            word = segments[i][-1]  # Get the last word in the segments array
            if word in word_dict:  # Check if the word is in the dictionary
                result.append(word.upper())  # Capitalize the word and add it to the result
            else:
                result.append(word)  # Add the word as is (in lowercase) to the result
            i -= len(word)  # Move the index back by the length of the word
        else:
            result.append(s[i-1].lower())  # Add the remaining character in lowercase
            i -= 1  # Move the index back by one

    return ''.join(result[::-1])  # Join the result list into a string and reverse it

s = "wfrowfwf"
word_dict = {"wf", "frow"}
print(min_remaining_letters(s, word_dict))
# bad case: WF row WF WF -> expected for greedy
# good case: w FROW WF WF