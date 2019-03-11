FROM python:alpine3.8
RUN pip install requests
RUN pip install jsonpickle
ADD contract.py /
ADD run.sh /
RUN chmod +x run.sh
RUN apk add --no-cache --update iptables
CMD exec /bin/sh -c "trap : TERM INT; (while true; do sleep 1000; done) & wait"
