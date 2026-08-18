# AWS Cloud Infrastructure Project

A Flask application containerized with Docker and deployed on an Ubuntu EC2 instance.

## Architecture

- AWS EC2
- Ubuntu Linux
- Docker
- Flask
- GitHub
- EC2 Security Group

## Project Structure

```text
aws-cloud-infrastructure/
├── app/
│   ├── app.py
│   └── requirements.txt
├── architecture/
├── docker/
│   └── Dockerfile
├── scripts/
├── troubleshooting/
└── README.md
q

## Deployment

1. Launch an Ubuntu EC2 instance on AWS.
2. Connect to the instance using EC2 Instance Connect.
3. Clone the GitHub repository.
4. Build the Docker image:
   docker build -t aws-cloud-app -f docker/Dockerfile .
5. Run the Docker container:
   docker run -d --name aws-cloud-container -p 5000:5000 aws-cloud-app
6. Verify the application:
   curl http://localhost:5000/
7. Verify the health endpoint:
   curl http://localhost:5000/health

## Application Endpoints

- `/` - Displays the AWS Cloud Infrastructure project page.
- `/health` - Returns the application health status.

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Docker
- Python
- Flask
- Git & GitHub

## Testing

The application was tested from the EC2 instance using curl.

Expected health response:

{"status":"healthy","service":"flask-app"}

## Troubleshooting

Common issues encountered during deployment:

- Docker permission denied: resolved by running Docker with appropriate permissions.
- Port 5000 already allocated: checked running containers using `docker ps`.
- Dockerfile path issue: used the correct Dockerfile location with `-f docker/Dockerfile`.
