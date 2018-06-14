// Configure the Google Cloud provider
provider "google" {
  credentials = "${file("account.json")}"
  project     = "civil-entry-205507"
  region      = "asia-east1"
}
