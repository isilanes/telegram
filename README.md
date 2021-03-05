This script can send messages to Telegram users programmatically.

Code and instructions based on https://www.geeksforgeeks.org/send-message-to-telegram-user-using-python/.

## Configuration

You need a `secrets.json` file, with the following contents:

```json
{
    "api_id": <api-id>,
    "api_hash": <api-hash>,
    "token": <token>,
    "phone": <my-phone>,
    "address_book": {
        <user1>: <phone-of-user1>,
        <user2>: <phone-of-user2>,
        <user3>: <phone-of-user3>,
        ...
    }
}
```

The values for `<api-id>`, `<api-hash>`, and `<token>` can be obtained as follows:

* Open Telegram app and search for `@BotFather`.
* Click on Start
* Send `/newbot` message, or click appropriate link to set up a name and a username.
* BotFather will give you a long string that will be you `<token>` value.
* Go to `my.telegram.org`
* Go to 'API development tools' and fill out the form to create an app.
* You will be given some info, including the values for `<api-id>` and `<api-hash>`.

The values for `<user1>`, `<user2>`, etc, will be user-friendly strings for people you might want to write to, such as "fred" or "grandma". All the `<phone>` values must be in international format ('+xy123456789').

### Python environment

You can create a Conda environment with all required packages by using the `environment.yml` file provided:

```bash
$ conda env create -f environment.yml
$ conda activate telegram
```

## Usage

To send a message to your friend 'fred' (see above, fred must be in your secrets.json file):

```bash
$ python main.py --to fred --msg "Hi, Fred!"
```

Full list of options:

```bash
$ python main.py -h
```
