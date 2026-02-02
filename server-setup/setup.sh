#!/bin/bash
set -e

# Claude Notion Server Setup Script
# Run this on your Ubuntu server after copying your SSH key

INSTALL_DIR="/opt/claude-notion"
REPO_URL="git@github.com:nate-kennedy/claude-notion.git"
SSH_KEY_PATH="$HOME/.ssh/id_ed25519"  # Adjust if using different key name

echo "=== Claude Notion Server Setup ==="

# Check if running as root or with sudo
if [ "$EUID" -ne 0 ]; then
    echo "Please run with sudo: sudo bash setup.sh"
    exit 1
fi

# Get the actual user (not root when using sudo)
ACTUAL_USER="${SUDO_USER:-$USER}"
ACTUAL_HOME=$(eval echo "~$ACTUAL_USER")

# 1. Install dependencies if needed
echo "Installing dependencies..."
apt-get update
apt-get install -y git docker.io docker-compose-v2

# Enable and start docker
systemctl enable docker
systemctl start docker

# Add user to docker group
usermod -aG docker "$ACTUAL_USER"

# 2. Create installation directory
echo "Creating $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"
chown "$ACTUAL_USER:$ACTUAL_USER" "$INSTALL_DIR"

# 3. Create persistence directories
echo "Creating persistence directories..."
mkdir -p "$INSTALL_DIR/claude-config"
mkdir -p "$INSTALL_DIR/claude-data"
chown -R "$ACTUAL_USER:$ACTUAL_USER" "$INSTALL_DIR"

# 4. Setup SSH for git (run as actual user)
echo "Setting up SSH..."
if [ ! -f "$ACTUAL_HOME/.ssh/id_ed25519" ] && [ ! -f "$ACTUAL_HOME/.ssh/id_rsa" ]; then
    echo ""
    echo "ERROR: No SSH key found!"
    echo "Please copy your private key to $ACTUAL_HOME/.ssh/ first"
    echo "Example: scp ~/.ssh/id_ed25519 user@server:~/.ssh/"
    echo ""
    exit 1
fi

# Add GitHub to known hosts
sudo -u "$ACTUAL_USER" bash -c 'ssh-keyscan github.com >> ~/.ssh/known_hosts 2>/dev/null'

# 5. Clone the repository
echo "Cloning repository..."
if [ -d "$INSTALL_DIR/repo" ]; then
    echo "Repository already exists, pulling latest..."
    sudo -u "$ACTUAL_USER" git -C "$INSTALL_DIR/repo" pull
else
    sudo -u "$ACTUAL_USER" git clone "$REPO_URL" "$INSTALL_DIR/repo"
fi

# 6. Copy docker-compose file
echo "Setting up Docker Compose..."
cp "$INSTALL_DIR/repo/server-setup/docker-compose.yml" "$INSTALL_DIR/docker-compose.yml"
chown "$ACTUAL_USER:$ACTUAL_USER" "$INSTALL_DIR/docker-compose.yml"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Log out and back in (for docker group permissions)"
echo "2. cd $INSTALL_DIR"
echo "3. Set your ANTHROPIC_API_KEY in docker-compose.yml or environment"
echo "4. Run: docker compose up -d"
echo ""
echo "The following directories will persist across container restarts:"
echo "  - $INSTALL_DIR/repo (your code)"
echo "  - $INSTALL_DIR/claude-config (claude auth & settings)"
echo "  - $INSTALL_DIR/claude-data (MCP configs, etc)"
