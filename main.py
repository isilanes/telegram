import sys
import json
import argparse

from telethon import TelegramClient, sync, events


def parse_args(args=sys.argv[1:]):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--to",
        help="Send message to this person.",
        default=None,
    )

    parser.add_argument(
        "--msg",
        help="Message to send.",
        default=None,
    )

    parser.add_argument(
        "--secrets",
        help="Path to JSON secrets file.",
        default="secrets.json",
    )

    return parser.parse_args(args)


def main(secrets, opts):
    phone = secrets.get("phone")
    if phone is None:
        raise ValueError("No phone.")

    recipient = secrets.get("address_book", {}).get(opts.to, None)
    if recipient is None:
        raise ValueError("No one to send message to.")

    if opts.msg is None:
        raise ValueError("No message to send.")

    credentials = (secrets.get("api_id"), secrets.get("api_hash"))
    if None in credentials:
        raise ValueError("Error with API ID or hash.")

    # Create a Telegram session:
    client = TelegramClient('session', *credentials)

    # Connect and build the session:
    client.start()

    # When run for the first time, it asks for log in:
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))

    # Send message:
    client.send_message(opts.to, opts.msg)

    # Disconnect the Telegram session:
    client.disconnect()


if __name__ == "__main__":
    opts = parse_args()

    with open(opts.secrets) as f:
        secrets = json.load(f)

    main(secrets, opts)

