provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source = "./eks/vpc.tf"
}

module "eks" {
  source = "./eks/eks-cluster.tf"
}

resource "kubernetes_namespace" "default" {
  metadata {
    name = "default"
  }
}

provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  token                  = module.eks.token
}

resource "kubernetes_deployment" "user_service" {
  metadata {
    name      = "user-service"
    namespace = "default"
  }

  spec {
    replicas = 2
    selector {
      match_labels = {
        app = "user-service"
      }
    }

    template {
      metadata {
        labels = {
          app = "user-service"
        }
      }

      spec {
        container {
          image = "gcr.io/devops-demo-440509/user-service:latest"
          name  = "user-service"

          port {
            container_port = 8000
          }
        }
      }
    }
  }
}
