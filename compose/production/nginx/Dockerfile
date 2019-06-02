FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
RUN cd etc
RUN mkdir ssl
ADD ssl/ /etc/ssl/

