# UNIT ==========
{:
  display_name="Exoscale Compute"
}

# COMPONENT ==========
{:
  type="html"
  display_name="Creating an Instance via the CLI"
}

Using a Command Line Interface (CLI) is an entirely different approach to configure required infrastructure components, but a very efficient one if you managed the learning curve.

From scaling and repeating tasks point of view, the CLI tool is pure joy. In the demo video, we used the following command to create a compute instance. The exo vm create - command provides 11 flags, with which we can achieve the same configuration flexibility as with the fields from the form provided on the portal.

```
Usage:
exo vm create <name> [flags] 

Flags: 
-a, --anti-affinity-group strings
-f, --cloud-init-file string    
-d, --disk int  
-h, --help 
-6, --ipv6 
-k, --keypair string 
-p, --privnet strings 
-s, --security-group strings   
-o, --service-offering string   
-t, --template string       
    --template-filter string   
-z, --zone string  
``` 

