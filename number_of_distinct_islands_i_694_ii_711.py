# 思路：https://blog.csdn.net/magicbean2/article/details/79248704
python: https://github.com/ChiahungTai/LeetCode/blob/master/Python/number-of-distinct-islands.py

# ii
一点点变化
思路：

DFS的套路不难，这里主要是如何处理小岛的旋转问题。我们的做法是：每次找到一个小岛之后，我们生成其8个对应的变形（包括本身，翻转以及旋转等）。然后返回其排序最小的那个，作为这种类型的小岛的代表。这样其余的思路就都可以照搬 [Leetcode] 694. Number of Distinct Islands 解题报告中的思路了。
---------------------
作者：魔豆Magicbean
来源：CSDN
原文：https://blog.csdn.net/magicbean2/article/details/79282937
版权声明：本文为博主原创文章，转载请附上博文链接！

