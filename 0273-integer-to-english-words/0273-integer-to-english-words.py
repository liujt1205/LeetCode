class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        thousands = ["", "Thousand", "Million", "Billion"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", ]
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        count = 0
           
        res = ""
        while num > 0:
            reminder = num % 1000
            cur = ""
            if reminder != 0:
                if reminder >= 100:
                    cur += ones[reminder // 100] + " Hundred "
                    reminder %= 100
                if reminder >= 20:
                    cur += tens[reminder // 10] + " "
                    reminder %= 10
                if reminder > 0:
                    cur += ones[reminder] + " "
                cur += thousands[count] + " "
            res = cur + res
            num = num // 1000
            
            count += 1
            
        return res.strip()