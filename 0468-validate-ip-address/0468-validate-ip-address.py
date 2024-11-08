class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkIPv4(string):
            sections = string.split('.')
            if len(sections) != 4:
                return "Neither"
            for section in sections:
                if not section.isdigit() or int(section) < 0 or int(section) > 255:
                    return "Neither"
                elif len(section) != 1 and section[0] == '0':
                    return "Neither"
                
            return "IPv4"
        
        def checkIPv6(string):
            sections = string.split(':')
            if len(sections) != 8:
                return "Neither"
            for section in sections:
                if not 1 <= len(section) <= 4:
                    return "Neither"
                for char in section:
                    if char not in "0123456789abcdefABCDEF":
                        return "Neither"
                
            return "IPv6"
        
        if '.' in queryIP:
            return checkIPv4(queryIP)
        elif ':' in queryIP:
            return checkIPv6(queryIP)
        else:
            return "Neither"
        
