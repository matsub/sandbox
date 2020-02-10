enum Keys {
    A,
    B,
}

fn main() {
    let k = Keys::A;

    let v = match k {
        Keys::A => 4,
        Keys::B => 42,
    };

    println!("{:}", v);

    let l = Keys::B;

    let w = match l {
        Keys::A => 4,
        Keys::B => 42,
    };

    println!("{:}", w);
}
