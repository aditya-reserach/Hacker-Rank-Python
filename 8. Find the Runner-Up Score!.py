"""
🏃 University Sports Day – Find the Runner-Up Score

📝 Problem Statement:
Your university recently held a Sports Day competition. Participants were scored based on their performances, 
and you are given the scores of all participants.

Your task is to determine the runner-up score — that is, the second highest score from the list. 
Note that there may be duplicate scores, but only the highest *distinct* score is considered the winner, 
and the next highest distinct score is the runner-up.

📥 Input Format:
- The first line contains an integer `n` — the number of participants.
- The second line contains `n` space-separated integers — the scores of each participant.

📌 Constraints:
- 2 ≤ n ≤ 100
- -100 ≤ score ≤ 100

📤 Output Format:
- Print a single integer — the runner-up score.

🧪 Sample Input 0:
5
2 3 6 6 5

✅ Sample Output 0:
5

💡 Explanation:
- The list of scores is: [2, 3, 6, 6, 5]
- The highest score is 6.
- After removing all instances of 6, the remaining scores are [2, 3, 5]
- The next highest score is 5 — this is the runner-up.
"""

# 1. Approch 

if __name__ == '__main__':
    # Read the number of participants (not used directly)
    n = int(input())

    # Read scores from input and convert them to integers
    arr = map(int, input().split())

    # Remove duplicate scores using set, convert back to list
    arr = list(set(arr))  # Only distinct scores remain

    # Sort the list in ascending order
    arr.sort()

    # Print the second highest score (runner-up)
    print(arr[-2])


# 2. Approch 

if __name__ == '__main__':
    n = int(input())  # Number of scores (still optional to use)
    arr = map(int, input().split())  # Convert input to integers

    # One-liner to print the runner-up score:
    print(sorted(list(set(arr)))[-2])
