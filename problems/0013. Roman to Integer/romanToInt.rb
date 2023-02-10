def roman_to_int(s)
    map = {
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M' => 1000
    }

    result = 0
    i = 0

    while i < s.length
        current = map[s[i]]
        next_val = (i + 1 < s.length) ? map[s[i + 1]] : 0

        if current < next_val
            result -= current
        else
            result += current
        end

        i += 1
    end

    result
end