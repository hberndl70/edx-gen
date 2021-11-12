# UNIT ==========
{:
  display_name="Calculating Product Pricing"
}

# COMPONENT ==========
{:
  type="html"
  display_name="Calculate Product Pricing"
}

Usually, you want to know the cost for a resource on a *monthly basis*, like you know your cost for other subscriptions like your mobile data plan, Spotify, Netflix, and so forth.

The official pricing can be found on the web <http://www.exoscale.com/pricing> and in the official price list. There you can find hourly pricing for the different products. In the Exoscale realm, we calculate with *720 hours per month*, and other cloud providers use, e.g. 730 hours per month, this information is relevant if you want to compare monthly pricing.

#### Application Server Instances

* 2x Medium (0.04040 EUR / hour)
* 100 GB disk (0.00013 EUR / hour / GB)
* 720 hours per month

**2 x 720 x (100 x 0.00013 + 0.04040) = 76.90 EUR / month**

#### Database Server Instances

* 3x Medium (0.04040 EUR / hour)
* 400 GB disk (0.00013 EUR / hour / GB)
* 720 hours per month

**3 x 720 x (400 x 0.00013 + 0.04040) = 199.60 EUR / month**

#### Backup Server Instance

* 1x Tiny (0.01263 EUR / hour)
* 50 GB disk (0.00013 EUR / hour / GB)
* 720 hours per month

**1 x 720 x (50 x 0.00013 + 0.01263) = 13.80 EUR / month**

#### Elastic IP

* 2x Elastic IP v2 (0.01262 EUR / hour)
* 720 hours per month

**2 x 720 x 0.01262 = 18.17 EUR / month**
