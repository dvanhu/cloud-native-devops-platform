provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "devops_example" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  tags = {
    Name = "devops-platform-instance"
  }
}
