terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
  }
}

resource "local_file" "sunny_note" {
  filename = "terraform-created-file.txt"
  content  = "This file was created by Terraform! - Sunny, future NZ Cloud Architect"
}
