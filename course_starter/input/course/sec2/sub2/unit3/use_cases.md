# UNIT ==========
{:
  display_name="Use Cases"
}

# COMPONENT ==========
{:
  type="html"
  display_name="Calculate Scenario Pricing"
}

For an overall scenario pricing, we have to add up all component prices - like the ones we calculated before - in our scenario, add data transfers to the internet and amount of storage in rest to the equation.

Additional storage costs are associated with the Simple Object Storage (SOS). A scalable, reliable, and cost-effective solution to support your application. Backup or serve your data from any Exoscale zone with no hidden fees, using your existing S3-compatible tooling and a familiar API.


#### Application Server Data Transfer 

* Data transfer to the Internet: 1000 GB / month
* free tier definition = 1.42 GB / hour / instance

The free tier for our web-application scenario consisting of 6 instances is:

**6 x 720 x 1.42 GB = 6134.40 GB / month**

The monthly data transfer (1.000 GB)  to the Intenet is **below** the free tier for our scenario (6.134 GB).


#### Public File Bucket

* 200 GB data stored
* 10 TB data transferred (10000 GB)

**200 x 0.01800 + 10000 x 0.01818 = 185.40 EUR / month**


#### Backup Bucket

* 1 TB data stored (1000 GB)

**1000 x 0.01800 = 18.00 EUR / month**


#### Calculation of Complete Scenario

```
Application Server Instances             76.90 EUR / month
Database Server Instances	              199.60 EUR / month
Backup Server Instance	                 13.80 EUR / month
Elastic IP	                             18.17 EUR / month
DNS	                                      0.91 EUR / month
Application Server Data Transfer          0.00 EUR / month
Public File Bucket	                    185.40 EUR / month
Backup Bucket	                           18.00 EUR / month
----------------------------------------------------------
TOTAL	                                  512.78 EUR / month
```
