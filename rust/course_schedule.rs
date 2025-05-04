use std::{collections::{HashMap, HashSet, VecDeque}, hash::Hash};

fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
    let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
    let mut in_degree: HashMap<i32, i32> = HashMap::new();

    // Initialize the graph and in-degree map
    for i in 0..num_courses {
        graph.insert(i, Vec::new());
        in_degree.insert(i, 0);
    }

    // Build the graph and update in-degrees
    for pair in prerequisites {
        let course = pair[0];
        let prereq = pair[1];
        graph.get_mut(&prereq).unwrap().push(course);
        *in_degree.get_mut(&course).unwrap() += 1;
    }

    // Find all courses with no prerequisites (in-degree 0)
    let mut q: VecDeque<i32> = VecDeque::new();
    for (&course, &degree) in &in_degree {
        if degree == 0 {
            q.push_back(course);
        }
    }

    let mut completed_courses = 0;

    // Process courses in topological order
    while let Some(course) = q.pop_front() {
        completed_courses += 1;
        if let Some(neighbors) = graph.get(&course) {
            for &neighbor in neighbors {
                *in_degree.get_mut(&neighbor).unwrap() -= 1;
                if in_degree[&neighbor] == 0 {
                    q.push_back(neighbor);
                }
            }
        }
    }
    
    completed_courses == num_courses
}

fn main() {
    let num_courses = 4;
    let prerequisites = vec![vec![1, 0], vec![2, 1], vec![3, 2]];
    let result = can_finish(num_courses, prerequisites);
    println!("Can finish all courses: {}", result); // Output: true
}