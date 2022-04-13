"""
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1: Input: words = ["cat", "bt", "hat", "tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2: Input: words = ["hello", "world", "leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    words[i] and chars consist of lowercase English letters.

Clarifications: can we assume both words and chare are non-empty? Are words and chars lowercase English letters?

Edge Cases:
Approach1: Traverse each word in strings. Naively, if the number of times this letter in a word is at least as many as
it appears in given chars, then add len(word) into our count.
Let N:= number of words in words list, K:= average number of letters in a word, M:= length of chars
Time: O(NMK)
Space: O(NK)

"""
from typing import List


class Solution:

    def correct_match(self, word: str, chars: str) -> bool:
        """
        Time: O(M * K)
        Space: O(1)

        :param word:
        :param chars:
        :return:
        """
        matched = 0
        for letter in word:
            if chars.count(letter) >= word.count(letter):
                matched += 1
        return matched == len(word)

    def countCharacters(self, words: List[str], chars: str) -> int:
        """
        Time: O(N * M * K)
        Space: O(1)

        :param words:
        :param chars:
        :return:
        """
        count = 0
        for word in words:
            if self.correct_match(word, chars):
                count += len(word)
        return count


if __name__ == '__main__':

    tests = [
        (["cat", "bt", "hat", "tree"], "atach", 6),
        (["cat", "bt", "hata", "tree"], "atach", 7),
        (["catt", "bt", "hata", "tree"], "atach", 4),
        (["hello", "world", "leetcode"], "welldonehoneyr", 10),
        (
            ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
             "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
             "boygirdlggnh", "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
             "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
             "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
             "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr", "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
             "oxgaskztzroxuntiwlfyufddl", "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
             "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv",
             "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz", "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
             "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
             "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob",
             "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
             "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"],
            "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp", 0
        )
    ]

    for words, chars, expected in tests:
        result = Solution().countCharacters(words, chars)
        assert result == expected

