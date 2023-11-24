# Question One 

## REST Overview
REST (Representation State Transfer) is a set of architectural principles for designing web services.


RESTful APIs use standard HTTP methods to perform operations on resources:

- **GET:** This method allows you to retrieve resources from a given API. It is a read-only operation, so it is not used to modify an existing resource.
- **POST:** Create a new resource.
- **PUT:** Update an existing resource or create a new resource if it doesn't exist.
- **DELETE:** Remove a resource.






# Question Two
This application requires a robust and scalable infrastructure that can handle the high volume of data and ensure timely delivery of notifications. 
Here is a walkthrough of how to manage such an application 
1. Infrastructure Design
- Messaging Infrastructure: Implement a distributed messaging system like Kafka or Amazon SQS to handle the high throughput of notifications 
- Nofication Delivery System : Use a distributed push notification service like Firebase Cloud messaging to deliver notifications to users' device. These services can handle the large volume of notification and provide features like device targeting and delivery retries.

2. Load Management
- Auto Scaling: Implemenent auto-scaling machanisms to adjust the number of processing nodes base on traffice demand. This ensures that the application can handle spikes in notification without performance degradation
- Resource Monitoring: Continously monitor resource utilization i.e CPU, memory, network to identify potential bottlenecks and proactively scale resources.

3. Asychronous Services
- Data processing: Employ asychronous processing techniques to handle the high volume of notications without blocking the main application thread. Use task queues like Celery or Amazon SQS to distribute processing tasks across multiple workers.
- Notification Delivery: Utilize asynchronous notification delivery libaries or frameworks to offloead the notification delivery process from the main application thread.

4. Monitoring and Alerting
- Application Monitoring: Implement comprehensive application monitoring to trach performance metrics, error rates and resource utilization. Tools like prometheus or Grafana for centralized monitoring.
- Alerting System : Set up alerting thresholds for key perfomance indicators to proactively identify potential issues and triggers corrective actions.

5. Testing and Continuous Integration
- Load Testing : Conduct regular load testing to simulate high volume traffic scenarios and validate the application's ability to hand the expected load.
- Continuous Integration and Continuous Delivery(CI/CD): Impliment a CI/CD pipeline to automate code testing, deployment, and infrastructure provisioning. This ensures quick and realiable delivery of new features and bug fixes.



# Question Three
## One-way Hashing 
1. SHA-256 Hashing 
- This is a secure hashing that is commonly used for verifying the integrity of data. 
- SHA-256 offers security and reliability. 
- Some of the features of SHA-25 are: Collision resistant, preimage resistance, large output

2. bcrpt hasing 
- This adds a random piece of data, called to create a unique hash that is almost impossible to break with automated guesses during hash dictionary and brute force attacks. 


## Two-way Hasing 
1. AES(Advanced Encryption Standard)
- This is a symmetric-key encryption algorithm that is commonly used to encrypt data in software.
- It uses the same key to encrypt and decrypt protected data.


2. RSA(Rivest-Shamir-Adleman)
- It is an asymmetricc cryptography algorithm.
- It works on two different keys i.e Public key and private key
- Public Key is given to everyone and the private is kept private
