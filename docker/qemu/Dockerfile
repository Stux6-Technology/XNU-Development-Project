FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    qemu-system-x86 \
    qemu-utils \
    ovmf \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /vm

COPY docker/qemu/run-qemu.sh /usr/local/bin/run-qemu.sh
RUN chmod +x /usr/local/bin/run-qemu.sh

ENTRYPOINT ["/usr/local/bin/run-qemu.sh"]
