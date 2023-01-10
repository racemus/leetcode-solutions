def numberToWords(num: int) -> str:
    if num == 0: return 'Zero'
    number_dict = {0: '',
                   1: 'One',
                   2: 'Two',
                   3: 'Three',
                   4: 'Four',
                   5: 'Five',
                   6: 'Six',
                   7: 'Seven',
                   8: 'Eight',
                   9: 'Nine'}
    teens_dict = {10: 'Ten',
                  11: 'Eleven',
                  12: 'Twelve',
                  13: 'Thirteen',
                  14: 'Fourteen',
                  15: 'Fifteen',
                  16: 'Sixteen',
                  17: 'Seventeen',
                  18: 'Eighteen',
                  19: 'Nineteen'}
    dozens_dict = {2: 'Twenty',
                   3: 'Thirty',
                   4: 'Forty',
                   5: 'Fifty',
                   6: 'Sixty',
                   7: 'Seventy',
                   8: 'Eighty',
                   9: 'Ninety'}
    number_depth = ['Thousand', 'Million', 'Billion']
    result = ''
    dozens_list = [str(num)[::-1][x-3:x][::-1] for x in range(3, len(str(num))+3,3)][::-1]

    for i in range(len(dozens_list)):
        if int(dozens_list[i]) == 0:
            continue
        if int(dozens_list[i]) >= 100:
            result += ' ' + number_dict[int(dozens_list[i]) // 100] + ' Hundred'
        if int(dozens_list[i]) % 100 > 0:
            j = int(dozens_list[i]) % 100 // 10
            if j == 1:
                result += ' ' + teens_dict[int(dozens_list[i]) % 100]
            elif j == 0:
                result += ' ' + number_dict[int(dozens_list[i]) % 100 % 10]
            else:
                result += ' ' + dozens_dict[j] + ' ' + number_dict[int(dozens_list[i]) % 100 % 10]
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