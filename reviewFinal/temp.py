from itertools import combinations


def get_k_skips_n_grams(k, n, input_str):
    # Convert the input string into a list of words
    words = input_str.split()
    result = []

    # Iterate through the list to generate k-skip n-grams
    for i in range(len(words)):
        # Generate the range of indices to consider for this k-skip n-gram
        indices = range(i, min(i + k + n, len(words)))
        for combination in combinations(indices, n):
            # Ensure the words in the combination are in order
            if all(combination[j] < combination[j + 1] for j in range(len(combination) - 1)):
                result.append(' '.join(words[idx] for idx in combination))

    # Print the result
    print(', '.join(result))


# Input and function call
k = int(input())  # Maximum skip distance
n = int(input())  # Length of n-grams
input_str = input().strip()  # Input text

get_k_skips_n_grams(k, n, input_str)
