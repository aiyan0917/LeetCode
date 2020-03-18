
class Solution(object):
    def wordPattern(self, pattern, str):
        """

        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern2str = {}
        str2pattern = {}
        str1 = str.split(' ')
        print(str1)

        for i in range(len(pattern)):

            if (pattern[i] in pattern2str and pattern2str[pattern[i]] != str1[i]) or (str1[i] in str2pattern and str2pattern[str1[i]] != pattern[i]):



                return False
            pattern2str[pattern[i]] = str1[i]
            str2pattern[str1[i]]=pattern[i]

        return True





if __name__ == '__main__':
    pattern = "abba"
    str = "dog dog dog dog"

    solution = Solution()  # Solution solution = new Solution();
    print(solution.wordPattern(pattern, str))
