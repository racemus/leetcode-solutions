var romanToInt = function(s) {
    let map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    let result = 0;
    let i = 0;

    while (i < s.length) {
        let current = map[s[i]];
        let nextVal = (i + 1 < s.length) ? map[s[i + 1]] : 0;

        if (current < nextVal) {
            result -= current;
        } else {
            result += current;
        }

        i += 1;
    }

    return result;
};