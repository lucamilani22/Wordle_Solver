import yaml
import math
from collections import Counter, defaultdict
from random import choice
from rich.console import Console

class Guesser:
    def __init__(self, manual):
        self.word_list = yaml.load(open('dev_wordlist.yaml'), Loader=yaml.FullLoader)
        self._manual = manual
        self.console = Console()
        self._tried = []                   
        self.candidates = list(self.word_list)  
        self.entropy_cache = {}            
        self.feedback_cache = {}           
        self.first_guess = self.precompute_best_first_guess()

    def restart_game(self):
        self._tried = []
        self.candidates = list(self.word_list)
        self.entropy_cache.clear()
        self.feedback_cache.clear()

    def get_guess(self, result):
        if self._manual == 'manual':
            return self.console.input('Your guess:\n')

        if not self._tried:
            guess = self.first_guess
        
        else:
            last_guess = self._tried[-1]
            self.candidates = [w for w in self.candidates if self.get_feedback(last_guess, w) == result]
            if not self.candidates:
                self.candidates = [w for w in self.word_list if w not in self._tried]
            guess = self.get_best_next_guess(self.candidates)

        self._tried.append(guess)
        self.console.print(guess)
        return guess

    def precompute_best_first_guess(self):
        letter_freq = Counter("".join(self.word_list))
        scored_words = sorted(
            self.word_list,
            key=lambda w: sum(letter_freq[c] for c in set(w)),
            reverse=True
        )
        return scored_words[0]

    def get_best_next_guess(self, candidates):
        if not candidates:
            return choice(self.word_list)
        return max(candidates, key=lambda w: self.compute_entropy(w, candidates))

    def compute_entropy(self, word, candidates):
        total = len(candidates)
        if total == 1:
            return 0.0

        key = (word, total)
        if key in self.entropy_cache:
            return self.entropy_cache[key]

        response_patterns = defaultdict(int)
        for target in candidates:
            fb = self.get_feedback(word, target)
            response_patterns[fb] += 1

        entropy = -sum(
            (count/total) * math.log2(count/total)
            for count in response_patterns.values() if count
        )
        self.entropy_cache[key] = entropy
        return entropy

    def get_feedback(self, guess, target):
        """Simulates the Wordle feedback:
           - Correct letter in correct position → letter itself.
           - Correct letter in wrong position → '-'
           - Letter not in target → '+'
        Caches results to reduce repeated computations."""
        key = (guess, target)
        if key in self.feedback_cache:
            return self.feedback_cache[key]

        result = ['+'] * 5
        target_counts = Counter(target)

        for i in range(5):
            if guess[i] == target[i]:
                result[i] = guess[i]
                target_counts[guess[i]] -= 1

        for i in range(5):
            if result[i] == '+' and guess[i] in target_counts and target_counts[guess[i]] > 0:
                result[i] = '-'
                target_counts[guess[i]] -= 1

        fb = ''.join(result)
        self.feedback_cache[key] = fb
        return fb