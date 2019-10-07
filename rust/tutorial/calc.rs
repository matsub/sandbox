pub fn add(x: i32, y: i32) -> i8 {
    let result: i8 = x as i8 + y as i8;
    return result;
}

fn main() {
    let x = 8;
    let y = 16;

    add(x, y);
}
