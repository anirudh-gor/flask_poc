FROM python:3.11.0
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Install all dev dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

CMD ["/app/entrypoint.sh"]
