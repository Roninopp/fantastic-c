#choti bachi ho kya
FROM python:latest

ENV PIP_NO_CACHE_DIR 1

RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

# Pypi package Repo upgrade
RUN pip3 install --upgrade pip setuptools

# Copy Python Requirements to /root/SuzuneHorikita 
RUN git clone https://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@github.com/Kanekiken099999/Shoto-Todoroki-.git
WORKDIR /root/SuzuneHorikita


#Copy config file to /root/Shoto-Todoroki-/SuzuneHorikita
COPY ./SuzuneHorikita/config.py ./SuzuneHorikita/config.py* /root/Shoto-Todoroki-/SuzuneHorikita/

ENV PATH="/home/bot/bin:$PATH"

# Install requirements
COPY requirements.txt .
RUN pip3 install -U -r requirements.txt

COPY . .

CMD ["python3", "-m", "SuzuneHorikita"]
