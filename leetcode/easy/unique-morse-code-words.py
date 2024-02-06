import string


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mores = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        uniques = set()

        for word in words:
            uniques.add("".join(map(lambda ch: mores[ord(ch) - 97], word)))

        return len(uniques)
