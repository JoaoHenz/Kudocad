provider "azurerm" {
  features {}
}

data "azurerm_client_config" "current" {}

resource "azurerm_kubernetes_cluster" "example" {
  name                = "KudocadCluster"
  location            = "eastus"
  resource_group_name = "PersonalResourceGroup"
  dns_prefix          = "KudocadCluster-dns"

  default_node_pool {
    name                = "agentpool"
    node_count          = 2
    vm_size             = "Standard_DS2_v2"
    max_pods            = 110
    min_count           = 2
    max_count           = 5
    enable_auto_scaling = true
    os_disk_size_gb     = 128
  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin     = "azure"
    service_cidr       = "10.0.0.0/16"
    dns_service_ip     = "10.0.0.10"
    docker_bridge_cidr = "172.17.0.1/16"
    load_balancer_sku  = "Standard"
  }

  tags = {
    Environment = "Production"
  }
}
