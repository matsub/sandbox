// Create instances

variable "machine_type"      { default = "f1-micro" }
variable "zone" 	     { default = "asia-east1-a" }
variable "image" 	     { default = "debian-cloud/debian-8" }

resource "google_compute_instance" "controller" {
  name         = "controller-ae1a-1"
  machine_type = "${var.machine_type}"
  zone = "${var.zone}"
  tags = ["web"]

  boot_disk {
    initialize_params {
      image = "${var.image}"
    }
  }

  network_interface {
    network = "${google_compute_network.default.name}"
  }

  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro"]
  }
}


resource "google_compute_instance" "target" {
  count = "2"
  name         = "target-${count.index}"
  machine_type = "${var.machine_type}"
  zone = "${var.zone}"
  tags = ["web"]

  boot_disk {
    initialize_params {
      image = "${var.image}"
    }
  }

  network_interface {
    network = "${google_compute_network.default.name}"
  }

  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro"]
  }
}
