FROM python:3.11-slim

# Set environment variable to ensure Python output is logged
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt first to leverage Docker's cache
COPY requirements.txt /app/requirements.txt

# Set the working directory
WORKDIR /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Default command
# CMD ["python", "test.py"]
# CMD ["sh", "-c", "python test.py && tail -f /dev/null"]


# # Expose port 8000
# EXPOSE 8000

# # Change the default command to run serve.py and then rag_app.py
# CMD ["sh", "-c", "python src/serve.py && python src/raggpt_app.py"]