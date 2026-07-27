resource "kubernetes_service" "uptimeguard" {
  metadata {
    name = "uptimeguard-tf-service"
  }

  spec {
    selector = {
      app = "uptimeguard"
    }

    port {
      port        = 80
      target_port = 5000
    }

    type = "NodePort"
  }
}
