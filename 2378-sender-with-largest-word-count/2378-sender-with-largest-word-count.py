class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        from collections import defaultdict

        word_counts = defaultdict(int)

        for msg, sender in zip(messages, senders):
            word_counts[sender] += msg.count(' ') + 1

        best_sender = None
        best_count = -1

        for sender, count in word_counts.items():
            if count > best_count or (count == best_count and sender > best_sender):
                best_sender, best_count = sender, count

        return best_sender