

use rand::{Rng, thread_rng, distributions::Uniform};
use std::time::Instant;

fn insertion_sort(l: &mut Vec<f32>, _low: usize, _high: usize){
    for i in 1..l.len(){
        // for j in (1..=i).rev(){
        //     if l[j-1] > l[j] {
        //         l.swap(j-1, j);
        //     }
        // }
        let mut j = i;
        while j > 0{
            if l[j - 1] > l[j] {
                l.swap(j - 1, j);
            }
            j -= 1;
        }
    }
}


fn bubble_sort(l: &mut Vec<f32>, _low: usize, _high: usize){
    let length = l.len();
    //let mut counter = 0;
    for i in 0..length{
        for j in 0..(length-i-1){ // -1 to prevent l[j+1] from being out of bounds
            if l[j] > l[j+1]{
                l.swap(j, j+1);
            }
        }
    }
}

fn selection_sort(l: &mut Vec<f32>, _low: usize, _high: usize){
    for j in 0..l.len(){
        let mut minimum: f32 = 2.0;
        let mut mindex = 0;

        for (index, &val) in l[j..].iter().enumerate(){
            if val < minimum{
                minimum = val;
                mindex = index;
            }
        }
        l.swap(mindex, j);
    }
}


fn partition(l: &mut Vec<f32>, low: usize, high: usize) -> usize{
    let center: f32 = l[(high+low)/2] as f32;
    let mut low = low-1;
    let mut high = high+1;

    loop {
        while {
            low += 1;
            l[low]<center
        } {}

        while {
            high -= 1;
            l[high] > center
        } {}

        if low>=high{
            return high;
        }
        l.swap(low, high);
    }
}

fn quick_sort(l: &mut Vec<f32>, low: usize, high: usize){
    if low < high{
        let p=partition(l, low, high);
        quick_sort(l, low, p);
        quick_sort(l, p+1, high);
    }
}

fn merge_sort(l: &mut Vec<f32>, _low: usize, _high: usize){
    let m = merge_sort_main(l.clone());
    let length = m.len();
    l.resize(length, 0.0 as f32);
    l.copy_from_slice(&m[0..]);
}

fn merge_sort_main(l: Vec<f32>) -> Vec<f32>{
    let length = l.len();
    if length <= 1{
        return l;
    }
    let mid=length/2;
    let lin = l[0..mid].to_vec();
    let rin = l[mid..].to_vec();
    let (left, right) = (merge_sort_main(lin), merge_sort_main(rin));
    return merge(&left, &right);
}


fn merge(l: &Vec<f32>, r: &Vec<f32>) -> Vec<f32> {
    let mut merged: Vec<f32> = Vec::new();
    let (mut lpos, mut rpos) = (0, 0);
    let (llen, rlen) = (l.len(), r.len());
    while lpos < llen && rpos < rlen {
        if l[lpos] > r[rpos] {
            merged.push(r[rpos]);
            rpos += 1;
        } else {
            merged.push(l[lpos]);
            lpos += 1;
        }
    }
    if lpos == llen {
        merged.extend(r[rpos..].to_vec());
    } else {
        merged.extend(l[lpos..].to_vec());
    }

    merged
}


fn time_sort<F: Fn(&mut Vec<f32>, usize, usize) -> ()>(name: String, sort: F, iters: u32, length: u32){ //low is passes as 1, high is len-1
    let mut rng = thread_rng();
    let range = Uniform::new(0.0, 1.0);
    
    let mut times:Vec<f64> = Vec::new();
    
    for _ in 0..iters{
        let vals: Vec<f32> = (0..length).map(|_| rng.sample(&range)).collect();
        let len = vals.len();
        let start=Instant::now();
        sort(&mut vals.clone(), 1, len-1);
        let elapsed = start.elapsed().as_secs_f64();
        times.push(elapsed);
    }
    println!("{:<18} {:<7} {:<10} {:<12} {:<12} {:<12}", name, iters, length, times.clone().into_iter().reduce(f64::min).unwrap(), times.clone().into_iter().reduce(f64::max).unwrap(), times.iter().sum::<f64>() / (times.len() as f64));
    //println!("Method: {:<15} Sorts: {:<5} List Length: {:<10} Min: {:<12} Max: {:<12} Avg: {:<12}", name, iters, length, times.clone().into_iter().reduce(f64::min).unwrap(), times.clone().into_iter().reduce(f64::min).unwrap(), times.iter().sum::<f64>() / (times.len() as f64));
}

fn main() {
    use std::env;

    let args: Vec<String> = env::args().collect();
    //println!("{:?}", args);
    if args.len() >= 3{
        let (iters, length) = (args[1].parse::<u32>().unwrap(), args[2].parse::<u32>().unwrap());
        println!("From args:");
        time_sort(String::from("quicksort"), quick_sort, iters, length);
        time_sort(String::from("insertion sort"), insertion_sort, iters, length);
        time_sort(String::from("selection sort"), selection_sort, iters, length);
        time_sort(String::from("bubble sort"), bubble_sort, iters, length);
        time_sort(String::from("merge sort"), merge_sort, iters, length);
        println!("");
    }
    // let mut v: Vec<f32> = vec![9.0,7.0,5.0,5.0,4.0,3.0,7.0,9.0];
    // bubble_sort(&mut v, 1, 1);
    // println!("sorted: {:?}", v);
    let start = Instant::now();

    println!("Method:            Sorts:  Length:    Min:         Max:         Avg:");
    for i in 1..=6{time_sort(String::from("Insertion Sort"), insertion_sort, 10, u32::pow(10, i));} println!("");
    println!("total time: {}", start.elapsed().as_secs());
    for i in 1..=6{time_sort(String::from("Selection Sort"), selection_sort, 10, u32::pow(10, i));} println!("");
    println!("total time: {}", start.elapsed().as_secs());
    for i in 1..=6{time_sort(String::from("Bubble Sort"), bubble_sort, 10, u32::pow(10, i));} println!("");
    println!("total time: {}", start.elapsed().as_secs());
    for i in 1..=6{time_sort(String::from("Merge Sort"), merge_sort, 10, u32::pow(10, i));} println!("");
    println!("total time: {}", start.elapsed().as_secs());
    for i in 1..=6{time_sort(String::from("Quicksort"), quick_sort, 10, u32::pow(10, i));} println!("");
    println!("total time: {}", start.elapsed().as_secs());
}
