use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(move || {
        for i in 1..10 {
            println!("spawned: {}", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("main thread: {}", i);
        thread::sleep(Duration::from_millis(1));
    }
}
