### 45. Jump Game II
**Medium**
<br>
<br>

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:
- `0 <= j <= nums[i]` and
- `i + j < n`
Return the minimum number of jumps to reach `nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.
<br>

**Example 1:**

<pre>
<b>Input:</b> nums = [2,3,1,1,4]
<b>Output:</b> 2
<b>Explanation:</b> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

**Example 2:**

<pre>
<b>Input:</b> nums = [2,3,0,1,4]
<b>Output:</b> 2
</pre>
<br>

**Constraints:**

- <code>1 <= nums.length <= 10<sup>4</sup></code>
- `0 <= nums[i] <= 1000`