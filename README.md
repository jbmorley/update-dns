# update-dns

Cloudflare dynamic DNS updater

## Usage

Install the Python dependencies using `pipenv` from the root directory:

```bash
pipenv install
```

Scheule regular updates by adding the following to your crontab file:

```
0/10 * * * * /Users/pi/Projects/update-dns/update-dns <email address> <authorization key> <record> >> /Users/pi/logs/update-dns.log 2>&1
```
