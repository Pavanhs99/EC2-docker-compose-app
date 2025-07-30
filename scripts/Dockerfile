FROM alpine

WORKDIR /app

RUN apk update && apk add bash

COPY system_info.sh .
COPY logger.sh .

RUN chmod +x /app/system_info.sh
RUN chmod +x /app/logger.sh

CMD ["sh", "system_info.sh"]
CMD ["sh", "logger.sh"]

