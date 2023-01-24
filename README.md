# Telegram Auth

The application allows, after authorization in Telegram, to generate a session as a string that can be used in applications. This string is used, for example in [Telethon](https://pypi.org/project/Telethon/) or [GramJS](https://www.npmjs.com/package/telegram).

## Usage

```sh
tg-auth --api-id <api_id> --api-hash <api_hash> --phone <phone> --password <password>
```

`--api-id` - Telegram app api_id

`--api-hash` - Telegram app api_hash

`--phone` - User phone (optional)

`--password` - User cloud password (optional)

API ID and API hash can be found at https://my.telegram.org/apps. Before running the command, if present, delete `cli.session`. Session string is saved to a file `session`.

## License

[MIT](https://choosealicense.com/licenses/mit/)
