FROM amazonlinux

RUN yum update -y && yum install -y \
  wget \
  unzip \
  dos2unix \
  python3

RUN wget https://releases.hashicorp.com/terraform/0.12.5/terraform_0.12.5_linux_amd64.zip \
  && unzip -o ./terraform_0.12.5_linux_amd64.zip \
  && mv terraform /usr/bin \
  && rm terraform_0.12.5_linux_amd64.zip

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN python3 get-pip.py

WORKDIR /app

COPY entrypoint.sh .
COPY requirements.txt .

RUN pip install -r requirements.txt

RUN dos2unix entrypoint.sh \
  && chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]