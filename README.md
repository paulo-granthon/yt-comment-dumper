# yt-comment-dumper

<h3 align="center"><i> ETL + flask server for dumping comments from youtube videos </i></h3>

<div align="center">
  
https://github.com/user-attachments/assets/bc36bdcd-c918-4315-935c-e96dcb1c1dd9

```rb
make VIDEO=https://www.youtube.com/watch?v=IH3W4WrM8qc
```

</div>
<br/>

<h2 align="center"> Projects: </h2>

## ETL

- ***Extract***s the comments from the youtube video, along with data such as the number of likes, the `parent_id` (in case of a response comment) and the user's profile picture url;
- ***Transform***s the data from the provider structure into the document structure used in the database;
- ***Load***s the formatted data into a `MongoDB` collection.

## Server

- Provides a tree view page with the comments present in the collection.

<br/>

<h2 align="center"> Environment: </h2>

#### `yt-comment-dumper` will only work if there's a properly configured `.env` file in the root of the repository directory.

<br/>

- Copy the `.env.example` file into a `.env` file and set your youtube api key:

> .env:
```rb
# shellcheck disable=2034,2148
# YouTube API keys
YOUTUBE_API_KEY=your_api_key_here
[...]
```

- If you are not using the pre-configured MongoDB container of this repository, you'll also need to change the environment variables prefixed with `DB_` in your `.env` file:

> .env:
```rb
[...]
# MongoDB configuration
DB_HOST=localhost
DB_PORT=27017
DB_NAME=yt_comment_dumper
DB_COLLECTION=comments
DB_USERNAME=mongo
DB_PASSWORD=secret
```

<br/>

<h2 align="center"> Usage: </h2>

## Makefile:

It's possible to run everything using the Makefile commands.

```yaml
make VIDEO=<video_url_or_id>        # Runs everything (db, etl, server)
```

Default commands:

```yaml
make db-up   # starts the mongodb container

make prep    # installs poetry dependencies

make etl     # runs the ETL

make serve   # runs the server
```

End of session:

```yaml
make db-down # stops the mongodb container
```

## poetry:

Install project dependencies:

```yaml
poetry lock
poetry install
```

Run projects:

```yaml
poetry run python src/etl/main.py VIDEO=<video_url_or_id>   # runs the ETL
poetry run python src/server/app.py                         # runs server
```

## docker-compose:

MongoDB container management (or use yours)

```yaml
docker-compose up   # start mongodb container
docker-compose down # stop mongodb container
```
