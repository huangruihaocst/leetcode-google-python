# Solution 1: Using deque
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
from collections import deque

class Solution:
    def __init__(self):
        self.cache = deque()
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n <= len(self.cache):
            for i in range(n):
                buf[i] = self.cache.popleft()
            return n
        need = n - len(self.cache)
        read_times = need // 4 + (1 if need % 4 > 0 else 0)
        for _ in range(read_times):
            tmp = [''] * 4
            size = read4(tmp)
            for i in range(size):
                self.cache.append(tmp[i])
            if size < 4:
                break
        cnt = 0
        for i in range(n):
            if len(self.cache) > 0:
                buf[i] = self.cache.popleft()
                cnt += 1
            else:
                break
        return cnt


"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):


# Solution 2: Space optimized
# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
# class Solution:
#     def __init__(self):
#         self.buffer = [''] * 4
#         self.buffer_ptr = 0
#         self.size = 0
        
#     def read(self, buf, n):
#         """
#         :type buf: Destination buffer (List[str])
#         :type n: Number of characters to read (int)
#         :rtype: The number of actual characters read (int)
#         """
#         ptr = 0
#         while ptr < n:
#             if self.buffer_ptr == 0:
#                 self.size = read4(self.buffer)
#                 if self.size == 0:
#                     break
#             while ptr < n and self.buffer_ptr < self.size:
#                 buf[ptr] = self.buffer[self.buffer_ptr]
#                 ptr += 1
#                 self.buffer_ptr += 1
#             if self.buffer_ptr >= self.size:
#                 self.buffer_ptr = 0
#         return ptr
