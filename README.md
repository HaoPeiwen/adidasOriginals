# Adidas Originals Wechat Applying
Apply `Adidas Original` sneakers automatically using [`@Wechat itchat`](https://github.com/littlecodersh/itchat)

## Usage
Edit the configuration file `ID.config`:

    # ID.config(UTF-8)
    [ID]
    # UK size according to adidas Originals （抢的码字）
    Size = L
    # Your phone number （手机号）
    Phone = 13800001111
    # Your ID （身份证）
    Id = 123456789123456789
Make sure both `main.py` and `ID.config` are in the same folder, then:

    $ pip3 install itchat
    $ python main.py

Then scan QR.png to login Wechat Web. This script aims to auto-reply authentication information like this:
![demo](demo.jpg)

If you do not want to stay logged in, delete `hotReload=True` in `main.py # 83`. See more [info](https://itchat.readthedocs.io/zh/latest/)

## Multiwindowing

You can simply copy the folder with `ID.config` and `main.py` for each wechat account.
    
