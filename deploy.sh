#!/bin/bash
az acr build --registry <your-registry> --image multi-agent-app .
az containerapp up --name multi-agent-app --resource-group <your-rg> --image <acr-image-path>
