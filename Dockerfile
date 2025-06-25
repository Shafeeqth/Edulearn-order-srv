# Stage 1: Build the application
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc &&
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Stage 2: Create the runtime image
FROM python:3.12-slim AS runtime

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl &&
    rm -rf /var/lib/apt/lists/*

# Copy installed dependencies from builder stage
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY . .

# Ensure scripts in ~/.local/bin are in PATH
ENV PATH=/root/.local/bin:$PATH

# Create a non-root user for security
RUN useradd -m appuser
USER appuser

# Expose ports
EXPOSE 8000 50051

# # Health check
# HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
#     CMD curl -f http://localhost:8000/health || exit 1

# Command to run the application
CMD ["python", "src/infrastructure/api/main.py"]
