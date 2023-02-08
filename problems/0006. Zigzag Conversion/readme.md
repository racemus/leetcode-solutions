### 6. Zigzag Conversion
**Medium**
<br>
<br>

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```
<br>

**Example 1:**

<pre>
<b>Input:</b> s = "PAYPALISHIRING", numRows = 3
<b>Output:</b> "PAHNAPLSIIGYIR"
</pre>

**Example 2:**

<pre>
<b>Input:</b> s = "PAYPALISHIRING", numRows = 4
<b>Output:</b> "PINALSIGYAHRPI"
<b>Explanation:</b>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

**Example 3:**

<pre>
<b>Input:</b> s = "A", numRows = 1
<b>Output:</b> "A"
</pre>
<br>

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`