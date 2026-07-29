// Last updated: 7/29/2026, 10:14:14 AM
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut number_map: HashMap<i32, i32> = HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&index) = number_map.get(&complement) {
                return vec![index, i as i32];
            }
            number_map.insert(num, i as i32);
        }
        vec![]  // Return an empty vector if no solution is found
    }
}