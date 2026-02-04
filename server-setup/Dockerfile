FROM debian:bookworm-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    openssh-client \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user first
RUN useradd -m -s /bin/bash claude

# Install Claude Code natively as the claude user
USER claude
WORKDIR /home/claude
RUN curl -fsSL https://claude.ai/install.sh | sh

# Add claude to PATH
ENV PATH="/home/claude/.claude/bin:${PATH}"

WORKDIR /workspace

# Default command
CMD ["claude"]
