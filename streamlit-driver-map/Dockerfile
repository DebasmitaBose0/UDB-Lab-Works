# Multi-stage build for a Python Streamlit app
# First stage installs dependencies without carrying unnecessary build artifacts
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt ./

RUN python -m pip install --upgrade pip \
    && python -m pip install --prefix=/install --no-cache-dir -r requirements.txt

# Final image is slim and only contains runtime files
FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /install /usr/local

# Copy only the app runtime files required to run Streamlit
COPY app.py ./
# If your app requires additional Python modules or assets, add them here explicitly:
# COPY helpers.py ./
# COPY assets/ ./assets/

EXPOSE 8501
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
