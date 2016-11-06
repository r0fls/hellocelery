# http://stackoverflow.com/a/30773882/1318734
FROM rabbitmq

# Define environment variables.
ENV RABBITMQ_USER hello
ENV RABBITMQ_PASSWORD world

ADD init.sh /init.sh
EXPOSE 15672
EXPOSE 5672

# Define default command
CMD ["/init.sh"]
