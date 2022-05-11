# Installing VYOS and put 2 virtual machines on same network

- Install VYOS from https://vyos.net/get/nightly-builds/
- Create 2 VYOS VMs
- `ip a` on VYOS1
- Note down the interface name (e.g eth0)
- `sudo ip addr add 192.168.100.1/24 dev eth0`
- Open VYOS2
- `ip a` on VYOS2
- Note down the interface name (e.g eth0)
- `sudo ip addr add 192.168.100.2/24 dev eth0`
- Now they are both on same network and we can ping one VM from another
