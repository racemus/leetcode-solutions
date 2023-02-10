var ones = []string{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"}
var tens = []string{"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"}
var thousands = []string{"", "Thousand", "Million", "Billion"}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	result := ""
	i := 0
	for num > 0 {
		if num%1000 != 0 {
			result = helper(num%1000) + thousands[i] + " " + result
		}
		num /= 1000
		i++
	}

	return strings.TrimSpace(result)
}

func helper(num int) string {
	if num == 0 {
		return ""
	} else if num < 20 {
		return ones[num] + " "
	} else if num < 100 {
		return tens[num/10] + " " + helper(num%10)
	}

	return ones[num/100] + " Hundred " + helper(num%100)
}
