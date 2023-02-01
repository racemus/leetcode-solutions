### 1071. Greatest Common Divisor of Strings
**Easy**


For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.


**Example 1:**

<pre>
<b>Input:</b> str1 = "ABCABC", str2 = "ABC"
<b>Output:</b> "ABC"
</pre>

**Example 2:**

<pre>
<b>Input:</b> str1 = "ABABAB", str2 = "ABAB"
<b>Output:</b> "AB"
</pre>

**Example 3:**

<pre>
<b>Input:</b> str1 = "LEET", str2 = "CODE"
<b>Output:</b> ""
</pre>


**Constraints:**

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of English uppercase letters.