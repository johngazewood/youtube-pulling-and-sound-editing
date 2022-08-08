use reqwest;

fn print_type_of<T>(_: &T) {
    println!("type: {}", std::any::type_name::<T>());
}

fn readfile(filename: &str) -> String {
    let content = std::fs::read_to_string(filename).expect(&*format!("Something went wrong reading the file {filename}"));
    return content;
}

#[tokio::main]
async fn main() {
    let api_key = readfile("/home/john/Scrap/youtube-pulling_with_rust/youtubepull/api_key.txt");
    //MSSP
    //let channel_id = "UC4fZeoNxAXfbIpT3swsVh9w";
    //RadioDawgz
    let channel_id = "UCcVTC5h21rvacpZ90E4YniQ";
    let main_endpoint = "https://www.googleapis.com/youtube/v3";
    let endpoint = format!("{main_endpoint}/search?key={api_key}&channelId={channel_id}");
    println!("what is the URL? {:?}", endpoint);
    let resp = reqwest::get(endpoint).await;
    print_type_of(&resp);
    println!("{:?}", resp);
    //let stat = resp.status();
    //println!("{:?}", stat);
}
