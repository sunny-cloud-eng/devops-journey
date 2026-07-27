resource "kubernetes_deployment" "uptimeguard" {
  metadata {
    name = "uptimeguard-tf"
    labels = {
      app = "uptimeguard"
    }
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "uptimeguard"
      }
    }

    template {
      metadata {
        labels = {
          app = "uptimeguard"
        }
      }

      spec {
        container {
          name              = "uptimeguard"
          image             = "uptimeguard"
          image_pull_policy = "Never"

          port {
            container_port = 5000
          }

          liveness_probe {
            http_get {
              path = "/health"
              port = 5000
            }
            initial_delay_seconds = 5
            period_seconds        = 10
          }
        }
      }
    }
  }
}
