use rand::{Rng, thread_rng, distributions::Uniform};
use std::time::Instant;



fn insertion_sort(l: &mut Vec<f32>, _low: usize, _high: usize){
    for i in 1..l.len(){
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
    for i in 0..length{
        for j in 0..(length-i-1){ // -1 to prevent l[j+1] from being out of bounds
            if l[j] > l[j+1]{
                l.swap(j, j+1);
            }
        }
    }
}

fn selection_sort(l: &mut Vec<f32>, _low: usize, _high: usize){
    for j in 0..l.len(){ //for each value...
        let mut minimum: f32 = 2.0;
        let mut mindex = 0;

        //find index of min val
        for (index, &val) in l[j..].iter().enumerate(){ //use l[j..] because we know elements before j have been sorted already (bc we make element j correct each time)
            if val < minimum{
                minimum = val;
                mindex = index;
            }
        }
        //swap with current val
        l.swap(mindex+j, j); //must do mindex+j because index is based on slice starting at j

    } //increment current val by 1 (for loop)
}


fn partition(l: &mut Vec<f32>, low: usize, high: usize) -> usize{
    let center: f32 = l[(high+low)/2] as f32;
    let mut low = low as i32 -1; //because usize is u need i :(
    let mut high = high+1;

    loop {
        while {
            low += 1;
            l[low as usize]<center
        } {}

        while {
            high -= 1;
            l[high] > center
        } {}

        if low as usize >=high{
            return high;
        }
        l.swap(low as usize, high);
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
    let mut m = merge_sort_main(l.clone());
    l.swap_with_slice(&mut m[..])
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


fn time_sort(name: String, sort: &dyn Fn(&mut Vec<f32>, usize, usize), iters: u32, length: u32){ //low is passes as 1, high is len-1
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
}

fn main() {
    use std::env;
    
    let args: Vec<String> = env::args().collect();

    if args.iter().any(|a| (a.contains("-") && a.contains("h") | (a.contains("--help")))){
        println!("usage: sorts ITERS SIZE [-h] [-a] [-t] [-m LENGTH]\n");
        println!("benchmark quick, insertion, selection, bubble, and merge sorts.\n");
        println!("positional arguments:");
        println!("   ITERS               (optional) Iterations to do of each sort before the main benchmark");
        println!("   SIZE                (optional) Length of lists to do for those arg-specified sorts\n");
        println!("options:");
        println!("   -h, --help          show this help message and exit");
        println!("   -a, --args-only     don't run the main benchmark, only the sorts specified by the arguments");
        println!("   -t, --show-total-time");
        println!("                       show the full, overall timer for all sorts in the main benchmark");
        println!("   -m, --max-list-len LENGTH");
        println!("                       (default 6) number of zeroes of maximum list length to go up to for the main benchmark (ie 6 means 1_000_000)");
        return;
    }

    if args.len()>=3 && args[1].parse::<u32>().is_ok() && args[2].parse::<u32>().is_ok(){
        let (iters, length) = (args[1].parse::<u32>().unwrap(), args[2].parse::<u32>().unwrap());
        println!("From Args:");
        println!("Method:            Sorts:  Length:    Min:         Max:         Avg:");
        time_sort(String::from("quicksort"), &quick_sort, iters, length);
        time_sort(String::from("insertion sort"), &insertion_sort, iters, length);
        time_sort(String::from("selection sort"), &selection_sort, iters, length);
        time_sort(String::from("bubble sort"), &bubble_sort, iters, length);
        time_sort(String::from("merge sort"), &merge_sort, iters, length);
        println!("");
    }

    if args.iter().any(|a| (a.contains("-") && a.contains("a"))| (a=="--args-only")) {return};
    

    let max_len_idx = args.iter().position(|a| (a.contains("-") && a.contains("m"))|(a=="--max-list-len"));
    let max_len = if max_len_idx == None {6} else {args[max_len_idx.unwrap()+1].parse::<u32>().unwrap()};

    let total_time_print = if args.iter().any(|a| (a.contains("-") && a.contains("t"))|(a=="--show-total-time")) {
        println!("Timer Started");
        |x: Instant| format!("Total Time: {}s", x.elapsed().as_secs())
    } else {
        |_: Instant| String::new()
    };

    let start = Instant::now();

    println!("Method:            Sorts:  Length:    Min:         Max:         Avg:");
    for i in 1..=max_len{time_sort(String::from("Insertion Sort"), &insertion_sort, 10, u32::pow(10, i));} println!("");
    println!("{}", total_time_print(start));
    for i in 1..=max_len{time_sort(String::from("Selection Sort"), &selection_sort, 10, u32::pow(10, i));} println!("");
    println!("{}", total_time_print(start));
    for i in 1..=max_len{time_sort(String::from("Bubble Sort"), &bubble_sort, 10, u32::pow(10, i));} println!("");
    println!("{}", total_time_print(start));
    for i in 1..=max_len{time_sort(String::from("Merge Sort"), &merge_sort, 10, u32::pow(10, i));} println!("");
    println!("{}", total_time_print(start));
    for i in 1..=max_len{time_sort(String::from("Quicksort"), &quick_sort, 10, u32::pow(10, i));} println!("");
    println!("{}", total_time_print(start));
}

#[cfg(test)]
mod tests {
    use super::*; //import the actual program because it's out of scope

    
    #[test]
    fn test_insertion_sort() {test_sort(&insertion_sort);}
    
    #[test]
    fn test_selection_sort() {test_sort(&selection_sort);}
    
    #[test]
    fn test_bubble_sort() {test_sort(&bubble_sort);}
    
    #[test]
    fn test_merge_sort() {test_sort(&merge_sort);}
    
    #[test]
    fn test_quick_sort() {test_sort(&quick_sort);}
    
    
    fn test_sort(sort: &dyn Fn(&mut Vec<f32>, usize, usize)) {
        let mut to_sort = vec![0.0f32; 10];
        let to_test = to_sort.clone();
        sort(&mut to_sort, 0, to_test.len()-1);
        assert_eq!(to_sort, to_test);

        let mut to_sort: Vec<f32> = vec![0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1];
        let to_test = to_sort.clone();
        sort(&mut to_sort, 0, to_test.len()-1);
        assert_eq!(to_sort, vec![0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]);

        let mut to_sort: Vec<f32> = vec![0.9, 0.8, 0.7, 0.6, 1.0];
        let to_test = to_sort.clone();
        sort(&mut to_sort, 0, to_test.len()-1);
        assert_eq!(to_sort, vec![0.6, 0.7, 0.8, 0.9, 1.0]);

        let mut to_sort: Vec<f32> = vec![0.9, 0.9, 0.7, 0.6, 0.5, 0.7, 0.75, 0.2, 0.0];
        let to_test = to_sort.clone();
        sort(&mut to_sort, 0, to_test.len()-1);
        assert_eq!(to_sort, vec![0.0, 0.2, 0.5, 0.6, 0.7, 0.7, 0.75, 0.9, 0.9]);
    }
}
