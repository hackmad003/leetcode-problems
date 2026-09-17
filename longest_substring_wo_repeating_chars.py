"""
PYTHON SOLUTION - Longest Substring Without Repeating Characters
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(min(N, K)) where K = size of character set
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ####################################
    ## LENGTH OF LONGEST SUBSTRING    ##
    ####################################
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty string has no substring, so max length is 0
        if not s:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Sliding Window with a Hash Map
        # KEY INSIGHT: Maintain a "window" [left, right] that always
        # contains UNIQUE characters. As we expand 'right' one character
        # at a time:
        #   - If the new character is a DUPLICATE within the current window,
        #     shrink the window from the LEFT until the duplicate is removed
        #   - Track the LARGEST window size seen throughout the process
        #
        # A hash map storing "character -> most recent index seen" lets us
        # jump 'left' DIRECTLY to just past the duplicate's last position,
        # rather than shrinking one step at a time (this is what makes it O(N)
        # instead of O(N^2)).
        
        # Map each character to the most recent index where it was seen
        char_index_map = {}
        
        left = 0            # Left boundary of the current window
        max_length = 0       # Best (longest) window size found so far
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If this character was seen BEFORE, and that occurrence is
            # WITHIN our current window, we must shrink the window
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Jump left to just AFTER the duplicate's previous position
                left = char_index_map[current_char] + 1
            
            # Record/update this character's most recent index
            char_index_map[current_char] = right
            
            # Current window size is (right - left + 1)
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length

#########
## EOF ##
#########