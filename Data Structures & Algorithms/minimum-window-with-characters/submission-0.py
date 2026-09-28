class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = {}
        window = {}

        # Count characters required from t
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        have = 0
        required = len(need)

        min_len = float("inf")
        result = ""

        for right in range(len(s)):

            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Character requirement is now satisfied
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Try shrinking while window is valid
            while have == required:

                # Update smallest window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result