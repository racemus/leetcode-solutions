### 989. Add to Array-Form of Integer
**Easy**
<br>
<br>

The **array-form** of an integer `num` is an array representing its digits in left to right order.

- For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return *the __array-form__ of the integer* `num + k`.
<br>

**Example 1:**

<pre>
<b>Input:</b> num = [1,2,0,0], k = 34
<b>Output:</b> [1,2,3,4]
<b>Explanation:</b> 1200 + 34 = 1234
</pre>

**Example 2:**

<pre>
<b>Input:</b> num = [2,7,4], k = 181
<b>Output:</b> [4,5,5]
<b>Explanation:</b> 274 + 181 = 455
</pre>

**Example 3:**

<pre>
<b>Input:</b> num = [2,1,5], k = 806
<b>Output:</b> [1,0,2,1]
<b>Explanation:</b> 215 + 806 = 1021
</pre>
<br>

**Constraints:**

- <code>1 <= num.length <= 10<sup>4</sup></code>
- `0 <= num[i] <= 9`
- `num` does not contain any leading zeros except for the zero itself.
- <code>1 <= k <= 10<sup>4</sup></code>