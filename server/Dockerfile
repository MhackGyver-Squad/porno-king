############################################################
#
# Porno-King Development And Testing Server
#
# Simple sample server with port knocking daemon turned on
# Use case:
# - for testing Porno-King 
# - needed for Porno-King standalone development environment
# - just for test or familiarize you with port knocking
#
############################################################
FROM ubuntu:latest
MAINTAINER Mh@ckGyv3R

#####################################
# Install packages
#####################################
RUN apt-get update
RUN apt-get install -y knockd
RUN apt-get install -y openssh-server
RUN apt-get install -y iptables

#####################################
# Configure Knockd daemon
#####################################
COPY knockd /etc/default/
COPY knockd.conf /etc/
COPY splash /etc/

EXPOSE 22

#####################################
# Start container
# 1. Display splash screen
# 2. Start services
# 3. Flush default configuration
# 4. Drop all traffic
# 5. At start allow loopback only
# 6. Print port knocking daemon log
#####################################
CMD cat /etc/splash && \
    service knockd start > /dev/null && \
    service ssh start > /dev/null && \
    iptables -F && \
    iptables -X && \
    iptables -P INPUT DROP && \
    iptables -P OUTPUT DROP && \
    iptables -P FORWARD DROP && \
    iptables -A INPUT -i lo -j ACCEPT && \
    iptables -A OUTPUT -o lo -j ACCEPT && \
    iptables -L && \
    echo "-----------------------------------" && \
    tail -f /var/log/knockd.log

