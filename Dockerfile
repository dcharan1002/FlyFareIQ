FROM apache/airflow:2.8.1

USER root

# Copy requirements
COPY requirements.txt /requirements.txt

# Switch to airflow user to install packages
USER airflow

# Install Python dependencies
RUN pip install --no-cache-dir -r /requirements.txt