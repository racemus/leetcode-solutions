### 904. Fruit Into Baskets
**Medium**

<br>
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the i<sub>th</sub> tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
- You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array `fruits`, return the *__maximum__ number of fruits you can pick*.
<br>

**Example 1:**

<pre>
<b>Input:</b> fruits = [1,2,1]
<b>Output:</b> 3
<b>Explanation:</b> We can pick from all 3 trees.
</pre>

**Example 2:**

<pre>
<b>Input:</b> fruits = [0,1,2,2]
<b>Output:</b> 3
<b>Explanation:</b> We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
</pre>

**Example 3:**

<pre>
<b>Input:</b> fruits = [1,2,3,2,2]
<b>Output:</b> 4
<b>Explanation:</b> We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
</pre>
<br>

**Constraints:**

- <code>1 <= fruits.length <= 10<sup>5</sup></code>
- `0 <= fruits[i] < fruits.length`