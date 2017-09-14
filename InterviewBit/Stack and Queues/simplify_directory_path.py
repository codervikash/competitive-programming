"""
Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
"""
class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        unix_path = []
        result_path = ''
        paths = A.split('/')

        for path in paths:
            if path:
                if path == '..':
                    if len(unix_path):
                        unix_path.pop()
                elif path == '.':
                    continue
                else:
                    unix_path.append(path)

        for i in xrange(len(unix_path)):
            popped = unix_path[i]
            result_path += '/' + popped

        return result_path if result_path else '/'
