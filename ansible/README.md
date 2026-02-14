# Ansible — Deployment Automation

## Overview

Simple Ansible playbooks to setup an Ubuntu server and deploy the API.

## Team 5 Responsibilities

- Update `hosts.ini` with the server IP and SSH details
- Update `deploy.yml` with the correct GitHub repo URL and env vars
- Run setup.yml once to install Docker
- Run deploy.yml to deploy/update the API

## Prerequisites

Install Ansible on your local machine:

```bash
# macOS
brew install ansible

# Ubuntu/Debian
sudo apt install ansible
```

## Files

| File       | Purpose                                        |
| ---------- | ---------------------------------------------- |
| hosts.ini  | Server inventory (IP, SSH user, key)           |
| setup.yml  | One-time: install Docker on the server         |
| deploy.yml | Deploy: clone repo, build image, run container |

## Usage

### 1. Update Inventory

Edit `hosts.ini` with your server details:

```ini
[servers]
food-court-server ansible_host=192.168.1.100 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

### 2. First-Time Setup

```bash
ansible-playbook -i hosts.ini setup.yml
```

This installs Docker on the server. Only needed once.

### 3. Deploy

```bash
ansible-playbook -i hosts.ini deploy.yml
```

This clones the repo, builds the Docker image, and runs the container.
Run this again anytime you want to update the deployment.

### 4. Verify

SSH into the server and check:

```bash
docker ps                          # Container should be running
curl http://localhost:5000/api/menu/stalls  # Should return stall data
```

## Notes

- Update `deploy.yml` vars section with your actual Supabase URL, key, and Telegram token
- For production, consider using Ansible Vault to encrypt secrets
- The container auto-restarts on server reboot (`--restart unless-stopped`)
