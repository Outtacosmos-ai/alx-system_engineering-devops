# Nginx Port 80 Configuration Script

This project contains a Bash script that configures Nginx to listen on port 80 and restarts the service.

## Prerequisites

- Ensure Nginx is installed on your Ubuntu 20.04 system.

## How to Run the Script

1. Make the script executable:

   ```bash
   chmod +x 0-nginx_likes_port_80
   ```

2. Run the script with sudo privileges:

   ```bash
   sudo ./0-nginx_likes_port_80
   ```

## Verification

After running the script, check the status of Nginx and confirm that it's listening on port 80:

```bash
sudo systemctl status nginx
ss -tuln | grep ':80'
