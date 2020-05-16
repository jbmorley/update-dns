#!/usr/bin/env python3

import argparse

import requests


class Cloudflare(object):

    def __init__(self, email, auth):
        self.email = email
        self.auth = auth
        self._headers = {
            "X-Auth-Email": self.email,
            "X-Auth-Key": self.auth,
            "Content-Type": "application/json"
        }

    def _get(self, url, params={}):
        return requests.get(url, params=params, headers=self._headers).json()

    def _put(self, *args, **kwargs):
        return requests.put(*args, headers=self._headers, **kwargs)

    def get_zone_identifier(self, zone):
        return self._get("https://api.cloudflare.com/client/v4/zones",
                         params={"name": zone})['result'][0]['id']

    def get_record_identifier(self, zone_identifier, record):
        return self._get(f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records",
                         params={"name": record})['result'][0]['id']

    def update_record(self, zone_identifier, record_identifier, details):
        return self._put(f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/{record_identifier}",
                         json=details)


def get_address():
    return requests.get("http://ipv4.icanhazip.com").text.strip()


def update_address(email, auth, zone, record, address):
    cloudflare = Cloudflare(email=email,
                            auth=auth)
    zone_identifier = cloudflare.get_zone_identifier(zone=zone)
    record_identifier = cloudflare.get_record_identifier(zone_identifier=zone_identifier, record=record)
    cloudflare.update_record(zone_identifier=zone_identifier,
                             record_identifier=record_identifier,
                             details={
                                "id": zone_identifier,
                                "type": "A",
                                "name": record,
                                "content": address
                             })


def main():
    parser = argparse.ArgumentParser(description="Updates Cloudflare record with current IP address.")
    parser.add_argument("email", type=str, help="email address")
    parser.add_argument("auth", help="authorization key")
    parser.add_argument("record", type=str, help="record to update")
    options = parser.parse_args()
    (_, zone) = options.record.split(".", 1)
    update_address(email=options.email,
                   auth=options.auth,
                   zone=zone,
                   record=options.record,
                   address=get_address())


if __name__ == "__main__":
    main()
