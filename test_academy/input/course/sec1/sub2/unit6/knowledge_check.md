# UNIT ==========
{:
  display_name="Knowledge Check"
}

# COMPONENT ==========
{:
    type="problem-checkboxes"
    display_name="Knowledge Check - Question 1"
    max_attempts="3"
    rerandomize="always"
    weight="1.0"
}


If you create a Medium instance (0.04040 EUR/hr) with a 50 GB disk (0.00013 EUR/GB/hr) attached to it  
and run Windows (0.01010 EUR/hr) on it for 24 hours, how much will you pay?

===

[ ] 24 x 0.04040 = 0.97 EUR ... you only need to pay for the machine.

[ ] 24 x 0.04040 + 24 x 50 x 0.00013 = 1.13 EUR ... you pay for the machine and storage.

[x] 24 x 0.04040 + 24 x 50 x 0.00013 + 24 x 0.01010 = 1.24 EUR ... you pay for the machine, storage and license.

===

Have a look at answer 3, 3 like 3 parts to consider ...

===

Machine. Disk. License. 

If your calculation formular does not consist of 3 parts ... it might be wrong ;)


# COMPONENT ==========
{:
    type="problem-checkboxes"
    display_name="Knowledge Check - Question 2"
    max_attempts="3"
    rerandomize="always"
    weight="1.0"
}


If you have 3 machines on Exoscale and you have a sudden traffic spike and the machines transfer 5 GB in one hour but otherwise incur no traffic, for how much data do you have to pay excess bandwidth fees?

===

[ ] None, the usage is within my allowance.

[x] 5 - (3 x 1.42) = 0.74 GB of data.

[ ] 5 GB of data.

===

Ist the allowance sufficent for this scenario? No it isn't. So we have to pay for the difference. 

===

3 x 1.42 GB vs 5 GB ...

5 - (3 x 1.42) = ???



