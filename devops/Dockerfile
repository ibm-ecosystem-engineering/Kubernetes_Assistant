FROM python:3.12-slim
LABEL maintainer="Anand Awasthi (anand.awasthi@in.ibm.com)"
RUN groupadd -r favuser && useradd -r -g favuser favuser
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application files
COPY . .
RUN chmod -R 775 /app && chown -R favuser:favuser /app
RUN mkdir -p /home/favuser && chown -R favuser:favuser /home/favuser

# Switch to the non-root user
USER favuser
EXPOSE 8080

CMD ["python", "kube-assistant.py"]
