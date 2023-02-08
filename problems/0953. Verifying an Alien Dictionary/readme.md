### 953. Verifying an Alien Dictionary
**Easy**
<br>
<br>

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.
<br>

**Example 1:**

<pre>
<b>Input:</b> words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
<b>Output:</b> true
<b>Explanation:</b> As 'h' comes before 'l' in this language, then the sequence is sorted.
</pre>

**Example 2:**

<pre>
<b>Input:</b> words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
<b>Output:</b> false
<b>Explanation:</b> As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
</pre>

**Example 3:**

<pre>
<b>Input:</b> words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
<b>Output:</b> false
<b>Explanation:</b> The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character [<a href="https://en.wikipedia.org/wiki/Lexicographical_order">More info</a>].
</pre>
<br>

**Constraints:**

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `order.length == 26`
- All characters in `words[i]` and `order` are English lowercase letters.