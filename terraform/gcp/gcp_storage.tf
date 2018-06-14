resource "google_storage_bucket" "tfstore" {
  name          = "tfstore"
  location      = "asia-east1"
  storage_class = "STANDARD"
}

resource "google_storage_bucket_acl" "remote-acl" {
  bucket         = "${google_storage_bucket.tfstore.name}"
  predefined_acl = "private"
}
