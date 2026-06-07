class MinStack {
    stack<int> stk;
    stack<int> mins;

public:
    MinStack() {}

    void push(int val) {
        if (mins.empty() || val <= mins.top()) {
            mins.push(val);
        }
        stk.push(val);
    }
    
    void pop() {
        if (stk.top() == mins.top()) {
            mins.pop();
        }
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return mins.top();
    }
};
