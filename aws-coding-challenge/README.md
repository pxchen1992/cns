## Goal
Write a script for creation of a service, and a healthcheck script to verify it is up and responding correctly.
## Prerequisites
You will need an AWS account. Create one if you don't own one already. You can use free-tier resources for this test.
## The Task
You are required to provision and deploy a new service in AWS. It must-
* Be publicly accessible, but *only* on port 80.
* Return the current time on `/now`.
## Mandatory Work
- Script your service using CloudFormation or using any other IaC tool such as terraform etc. and your server configuration management tool of choice should you need one.
- Provision the service (if you want to give them a go and run the service inside a Docker container and make it highly available.) in your AWS account.
- Write a healthcheck script in Python/Go that can be run externally to periodically check if the service is up and its clock is not desynchronised by more than 1 second.
- Alter the README to contain instructions required to:
  * Provision the service.
  * Run the healthcheck script.

Once done, save the code under the `aws-coding-challenge` folder. Feel free to ask questions as you go if anything is unclear, confusing about any part.
