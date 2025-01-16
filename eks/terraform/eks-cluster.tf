module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "~> 18.0"
  cluster_name    = "microservices-cluster"
  cluster_version = "1.27"

  subnets = module.vpc.private_subnets
  vpc_id  = module.vpc.vpc_id

  node_groups = {
    private-nodes = {
      desired_capacity = 2
      max_capacity     = 3
      min_capacity     = 1

      instance_types = ["t3.medium"]
      subnets        = module.vpc.private_subnets
    }
  }

  tags = {
    Name = "eks-cluster"
  }
}
