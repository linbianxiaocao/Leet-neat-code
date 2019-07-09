class StockSpanner {
public:
    StockSpanner() {
        
    }
    
    // monotonic stack
    // https://blog.csdn.net/fuxuemingzhu/article/details/82781059
    // https://leetcode.com/problems/online-stock-span/discuss/168311/C++JavaPython-O(1)
    int next(int price) {
        int res = 1;
        while (!s.empty() && s.top().first <= price) {
            res += s.top().second;
            s.pop();
        }
        s.push({price, res});
        return res;
    }
    
private:
    stack<pair<int, int>> s;
    
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
 
 // also reference https://www.cnblogs.com/grandyang/p/11029306.html
 // which is the same idea as the dp solution by huahua: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-901-online-stock-span/