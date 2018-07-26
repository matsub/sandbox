terraform {
  required_version = ">= v0.11.0"

  backend "gcs" {
    bucket = "tfstore"
    prefix = "terraform/state"
  }
}
