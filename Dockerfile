# Use Python base image
FROM python:3.11

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run your script
CMD ["streamlit", "run", "epon_command_generate.py"]

