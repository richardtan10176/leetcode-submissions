#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <ctype.h>
#include <stack>

class Solution {
public:
    int largestRectangleArea(std::vector<int>& heights) {
        std::stack<int> s; 
        int n = heights.size();
    
        int max_area = 0; // Initialize max area 
        int tp; // To store top of stack 
        int area_with_top; // To store area with top bar as the smallest bar 
    
        // Run through all bars of given histogram 
        int i = 0; 
        while (i < n) { 
            // If this bar is higher than the bar on top 
            // stack, push it to stack 
            if (s.empty() || heights[s.top()] <= heights[i]) 
                s.push(i++); 
    
            else { 
                tp = s.top(); 
                s.pop(); 

                area_with_top = heights[tp] * (s.empty() ? i : i - s.top() - 1); 
    
                // update max area, if needed 
                if (max_area < area_with_top) {
                    max_area = area_with_top; 
                }
                    
            } 
        } 
    
        while (s.empty() == false) { 
            tp = s.top(); 
            s.pop(); 
            area_with_top = heights[tp] * (s.empty() ? i : i - s.top() - 1); 
    
            if (max_area < area_with_top){
                max_area = area_with_top; 
            }
                
        } 
    
        return max_area;
    }
};