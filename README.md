# update-dns

Cloudflare dynamic DNS updater

## Usage

Scheule regular updates by adding the following to your crontab file:

```
0/10 * * * * /Users/pi/Projects/update-dns/update-dns "cloudflare@inseven.co.uk" <cloudflare token> elsewhere.jbmorley.co.uk >> /Users/pi/logs/update-dns.log 2>&1
```