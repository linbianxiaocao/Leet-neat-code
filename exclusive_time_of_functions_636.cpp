class Solution {
public:
    // https://www.cnblogs.com/grandyang/p/7244767.html
	// 特别分析这个testcase: 
	// 2
	// ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
	// Expected:
	// [8,1]
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> res(n, 0);
        stack<int> st;
        int preTime = 0;
        
        for (string log : logs) {
            int found1 = log.find(":");
            int found2 = log.find_last_of(":");
            int idx = stoi(log.substr(0, found1));
            string type = log.substr(found1+1, found2-found1-1);
            int time = stoi(log.substr(found2+1));
            if (!st.empty()) res[st.top()] += time-preTime;
            preTime = time;
            if (type == "start") st.push(idx);
            else {
                auto t = st.top(); st.pop();
                ++res[t];
                ++preTime;
            }
        }
        
        return res;
    }
};