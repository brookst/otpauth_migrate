# otpauth_migrate
Decode secret code from otpauth-migrate data in Google Authenticator QR code exports for entry into a password manager such as [KeepassXC](https://github.com/keepassxreboot/keepassxc).

If an app exports OTP secrets as an otpauth-migrate QR Code, it can be parsed by calling the `otpauth-migrate.py` script:

    ./otpauth_migrate.py otpauth-migration://offline?data=CiQKChkAMJCF7zetb50SEmdpdGh1Yi5jb206YnJvb2tzdBoCbWUQARgBKAE%3D
    
If not specified as an argument, input is awaited on stdin. This can be used to capture a QR code. E.g:

    zbarcam | ./otpauth_migrate.py
    
`zbarcam` is in the `zbar-tools` package on Ubuntu and is part of [ZBar suite](https://github.com/mchehab/zbar).

Uses Google protobuf definition from https://alexbakker.me/post/parsing-google-auth-export-qr-code.html
