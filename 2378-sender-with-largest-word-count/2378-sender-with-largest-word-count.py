class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        from collections import defaultdict
        max_n_words = {}
        max_n = 0

        for message, sender in zip(messages, senders):
            n_words_message = len(message.split(' '))
            if max_n < n_words_message:
                max_n = n_words_message
            if sender not in max_n_words:
                max_n_words[sender] = n_words_message
            else:
                max_n_words[sender] += n_words_message
                if max_n < max_n_words[sender]:
                    max_n = max_n_words[sender]

        result = []

        for key, val in max_n_words.items():
            if val == max_n:
                result.append(key)

        return sorted(result)[-1]