FROM python:latest

# Env & Arg variables
ARG USERNAME=username
ARG USERPASS=password

# Apt update & apt install required packages
# whois: required for mkpasswd
RUN apt-get update && apt-get -y install openssh-server whois
# RUN apt-get -y install openssh-server whois

# Add a non-root user & set password
RUN useradd -ms /bin/bash $USERNAME
# Save username on a file
#RUN echo "$USERNAME" > /.non-root-username

# Set password for non-root user
RUN usermod --password $(echo "$USERPASS" | mkpasswd -s) $USERNAME

# Change to non-root user
# USER $USERNAME
# WORKDIR /home/$USERNAME

# Copy the entrypoint
COPY ./entrypoint.sh entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create the ssh directory and authorized_keys file
USER $USERNAME
RUN mkdir /home/$USERNAME/.ssh && touch /home/$USERNAME/.ssh/authorized_keys
USER root

# ------------------------------------------------------------------------------------------------------
# RUN mkdir -p /home/project/script
# COPY ./script/. /home/project/script
# WORKDIR /home/project/script

# RUN apt-get install -y libgeos-dev libproj-dev liblapack-dev libblas-dev gfortran
COPY requirements.txt /home/$USERNAME/requirements.txt
RUN pip install --upgrade pip --no-cache-dir -r /home/$USERNAME/requirements.txt 
# RUN pip install cartopy scipy

WORKDIR /home/$USERNAME
COPY ./fstab /home/$USERNAME/
COPY ./python /home/$USERNAME/python
RUN mkdir /mnt/NAS_CALab
# ------------------------------------------------------------------------------------------------------

# Remove no-needed packages
RUN apt-get purge -y whois && apt-get -y autoremove && apt-get -y autoclean && apt-get -y clean

# Set volumes
VOLUME /home/$USERNAME/.ssh
VOLUME /etc/ssh

# expose ports
EXPOSE 22

# Run entrypoint
# CMD ["/entrypoint.sh"]
