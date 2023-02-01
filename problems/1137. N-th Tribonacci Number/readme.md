### 1137. N-th Tribonacci Number
**Easy**



The Tribonacci sequence Tn is defined as follows: 

T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n >= 0.

Given `n`, return the value of T<sub>n</sub>.


**Example 1:**

<pre>
<b>Input:</b> n = 4
<b>Output:</b> 4
<b>Explanation:</b>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

**Example 2:**

<pre>
<b>Input:</b> n = 25
<b>Output:</b> 1389537
</pre>


**Constraints:**

- `0 <= n <= 37`
- The answer is guaranteed to fit within a 32-bit integer, ie. <code>answer <= 2<sup>31</sup> - 1</code>.