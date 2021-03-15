#!/usr/bin/env python3
#
# Parse Google Authenticator QR codes using protobuf definition from:
# https://alexbakker.me/post/parsing-google-auth-export-qr-code.html

import urllib.parse
from base64 import b64decode, b32encode

from otpauth_migrate_pb2 import MigrationPayload

def parse(code):
    # Split out the data field from the 'otpauth-migration' URI
    query = urllib.parse.parse_qsl(code)
    if query:
        path, data = query[0]
        data = b64decode(data)
    else:
        # See if we just got the urldecoded data field
        data = b64decode(code)

    # Unpack protobuf layer
    payload = MigrationPayload.FromString(data)
    for parameters in payload.otp_parameters:
        # Print parameters incase the type/algorithm is needed
        print(parameters)

        # Re-encode with base32 for consumption by other tools
        output = b32encode(parameters.secret).decode()
        print(f"Secret code = {output:s}\n")

if __name__ == '__main__':
    from argparse import ArgumentParser
    from sys import exit
    parser = ArgumentParser(
            description="Parse otpauth-migration data from Google Authenticator",
            epilog="If code is not provided, it is awaited on stdin,"
            " use this to pipe in data e.g. > zbarcam | ./otpauth-migrate.py")
    arg = parser.add_argument
    arg("code", nargs="?", default="-", help="otpauth-migration URI or data field")
    args = parser.parse_args()
    if args.code != "-":
        parse(args.code)
    else:
        try:
            parse(input())
        except KeyboardInterrupt:
            parser.print_help()
            exit(1)
