def numberToWords(num: int) -> str:
    ''' It uses lists instead of dictionaries '''
    if num == 0: return 'Zero'
    numbers = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
               'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
               'Eighteen', 'Nineteen']
    dozens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    number_depth = ['Thousand', 'Million', 'Billion']
    result = ''
    dozens_list = [str(num)[::-1][x-3:x][::-1] for x in range(3, len(str(num))+3,3)][::-1]
    
    for i in range(len(dozens_list)):
        if int(dozens_list[i]) == 0:
            continue
        if int(dozens_list[i]) >= 100:
            result += ' ' + numbers[int(dozens_list[i]) // 100] + ' Hundred'
        if int(dozens_list[i]) % 100 > 0:
            j = int(dozens_list[i]) % 100
            k = j // 10
            if k == 1:
                result += ' ' + numbers[j]
            elif k == 0:
                result += ' ' + numbers[j % 10]
            else:
                result += ' ' + dozens[k] + ' ' + numbers[j % 10]
        if len(dozens_list) - i > 1:
            result += ' ' + number_depth[len(dozens_list) - 2 - i]
    
    return ' '.join(result.split())

print(numberToWords(123)) # One Hundred Twenty Three
print(numberToWords(12345)) # Twelve Thousand Three Hundred Forty Five
print(numberToWords(1234567)) # One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
print(numberToWords(0)) # Zero
print(numberToWords(20)) # Twenty
print(numberToWords(100)) # One Hundred
print(numberToWords(1000)) # One Thousand
print(numberToWords(101)) # One Hundred One
print(numberToWords(50868)) # Fifty Thousand Eight Hundred Sixty Eight
print(numberToWords(100000)) # One Hundred Thousand
print(numberToWords(1000000)) # One Million