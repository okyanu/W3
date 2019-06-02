Inspiration
We were trying to find new things and entertainments to do nearby but we were having some troubles to find it. Today, we came up with an idea of creating web application to help people enjoy their free days with recommendations that we are giving to them based on their selections.

What it does
3wsTo (When, What, Where ), helps people to enjoy their free times by giving them recommendations based on their selections whether they want to spend time at home or outside.

How we built it
Firstly, we started by creating docker containers for our backend,database and GUI for database which are Django, MySQL and phpmyadmin. Then, we started to code our backend to get data from several API's to retrieve a unique algorithm for recommendations for our user based on dates, location, personal interests. After that, we started to code our frontend with html,css and javascript. After everything is done , we deployed our application to Amazon Web services by using Amazon EC2 instance as a server. Then we moved our static and media files to Amazon S3 which is a storage system , then we used this storage to create a CDN for our application to make our website faster and sustainable. By setting Docker as a container in our server, we believe that we will have more scalable and fault-tolerant application. Also we used Route53 for DNS and domain.

Challenges we ran into
We spent too much time on our frontend to make our website look great. This is our main goal when we are working on a project. We believe that it is the most important thing for users. This took so much time for us to create rather than implementation the backend and others.

Accomplishments that we're proud of
We are very proud of using Amazon Web Services and Docker in our application which made our application more professional.

What we learned
We improved ourselves at retrieving data from APIs. We learnt some trick when sending data from our backend to frontend to show data to users effectively.

What's next for 3wsTo
We want to improve 3wsTo by storing data from searchs and from users by creating registration and extending this model with some extra field to make the data valuable.

Built With
django
docker
amazon-ec2
amazon-web-services
amazon-cloudfront-cdn
python
html
css
javascript
