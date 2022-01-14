# UNIT ==========
{:
  display_name="Exoscale Compute"
}

# COMPONENT ==========
{:
  type="html"
  display_name="Creating an Instance via the Portal"
}

The process is similar to order a server-hardware, but with significantly faster delivery. You have the following 11 fields in the form, not all are mandatory, but they give you certain flexibility in defining your new server (compute instance).

New Instance Form Field Details explained:

#### Hostname
The hostname is optional and serves two purposes:

It helps you identify the compute instance in the dashboard.
If you have multiple compute instances, it is helpful to name them for easier identifiability.
It sets the server hostname in the used operating system; this is useful,
so the server's software knows which server it is running on.
If you do not provide a hostname, Exoscale will generate a random hostname for the server.

#### Template
With the template, you select the operating system for your compute instance. If you want to use your own license, you can opt for the BYOL (Bring Your Own License) model, or if you do not wish to use one of the pre-made templates, you can also build your specific custom template.

#### Instance Type
The instance type lets you choose the CPU and RAM available in the server. These affect the performance of the server. However, you can only adjust the CPU and RAM together.

#### Disk
The disk size can be adjusted independently from CPU and RAM within a range of the selected instance. The maximum disk size, however, depends on the instance type.

#### Zone
With the zone selection, you define where the server will run. Zones are entirely independent, so if an outage occurs in one zone, other zones are unaffected. A best practice is to build systems to run in multiple zones, failing-over to another site if there is an outage in one location.

#### Keypair
The keypair option lets you specify which key you want to use for login. Some operating systems, such as Linux, allow key login instead of passwords.

#### Private Networks
Exoscale can connect instances within one zone via a private network. A private network is a segment shared only by your instances, like if they were attached to a dedicated switch. Security groups do not apply to those networks.

Exoscale offers two types of private networks:

* unmanaged
there is no DHCP server to distribute IP addresses of your private network interfaces
* managed
there is a managed DHCP server that automatically configures the IP addresses of your interfaces

#### IPv6
With the IPv6 selection, you enable an additional public IP address (in the IPv6 format) for the compute instance. By default, all virtual machines on Exoscale receive a public IPv4 IP address to communicate on the internet. Both assigned IP addresses (IPv4 and IPv6) are for the lifetime of the compute instance. If the compute instance is stopped but not destroyed and then restarted, the IP address will not change. Destroying the compute instance will put back the IP addresses into the public IP addresses pool, meaning you cannot retrieve them back.

#### Security Groups
A security group is Exoscale's built-in network firewall functionality of compute instances. Assigning virtual machines to a security group applies the firewall rules to the compute instances. This option lets you select which security group(s) a virtual machine should belong to.

#### Anti-Affinity Groups
An anti-affinity group lets you define a set of machines that should never live on the same physical host. For implementing higher redundancy locally (in the same zone), use an anti-affinity group.

#### User Data
The user data field gives you the ability to automatically install or configure software after the operating system installation is finished.



