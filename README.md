# QuickBio

This is a web application that crawls LinkedIn & Twitter data about a person and customizes an icebreaker with them.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

`SCRAPIN_API_KEY` 

`TAVILY_API_KEY`

`TWITTER_API_KEY`

`TWITTER_API_SECRET`

`TWITTER_ACCESS_TOKEN`

`TWITTER_ACCESS_SECRET`

`LANGCHAIN_TRACING_V2`  

`LANGCHAIN_API_KEY` 

## Run Locally

Clone the project

```bash
  git clone https://github.com/Rachel0619/QuickBio.git
```

Go to the project directory

```bash
  cd QuickBio
```

Install dependencies

```bash
  pipenv install
```

Start the flask server

```bash
  pipenv run app.py
```
