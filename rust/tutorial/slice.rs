fn main() {
    let xs = [0,1,2,3,4,5,6,7];
    let ys = &xs[4..8];

    let mut arr: [u8; 4] = [0; 4];

    for i in 0..4 {
        arr[i] = ys[i];
    }

    println!("{:?}", arr);
}
