# https://leetcode.com/problems/defanging-an-ip-address/

'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".


Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''


class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_ip = ''
        for s in address:
            if s == '.':
                new_ip += '[.]'
            else:
                new_ip += s
        return new_ip


if __name__ == '__main__':
    address = "255.100.50.0"
    print(Solution().defangIPaddr(address))
