# Scholiast

<p align="center">
  <a href="https://yuridelgado.dev">
    <img alt="Scholiast" src="./assets/scholiast-preview.png">
  </a>
</p>


That's a comment bot for Instagram using Selenium Web Driver.
**Notice:** this repository is for studying purposes only. Be aware of the Instagram's terms of use and their policies.

---

### About
Scholiast was built to perform a set of comments sequentially in a random customized range of time in order to avoid failing responses or blocking.

Currently, Scholiast is resilient when it comes to denied reponses. If a comment request is not successfully done, the script waits, by default, 30min to follow the remaining comment list. Otherwise, comments keep going sequentially within the defined time range.

Your Instagram account cannot have 2FA activated to run Scholiast.

## Usage

To run Scholiast, you have to use Firefox Web Driver (default used driver). You can take a version of your preference in the [Mozilla Offical Repo for Geckodriver](https://github.com/mozilla/geckodriver/releases) and add the binary in the root folder of the application. Make sure you have Mozilla Firefox installed in your machine.

Make sure you have `pipenv` available to use in your terminal. You can check the documentation [here](https://pipenv-fork.readthedocs.io/en/latest/basics.html).

```bash
pipenv install
```

- As environment variables, you have to define `IGUSER` as your Instagram username and `PASSWORD` as your Instagram password in a `.env` file within `app/lib/`.

- In your Scholiast call, you have to provide the comments to be done in a tuple of strings, the post url and the time interval in minutes.

Check the example bellow to understand how to pass them.

## Example

```
from app.lib.core import Scholiast

# Comments tuple
comments = (
  'lorem ipsum', 
  'dolor sit', 
  'amet, consectetur', 
  'adipiscing elit',
)

# Post URL - the post must be visible to your account
POST_URL = 'https://www.instagram.com/p/<:id>/'

# Scholiast will get a random value within the range (min, max) in minutes
TIME_INTERVAL = (10, 12)

# When the flag is true, the comment is not sent indeed 
TEST=True

def main():
  login, comment = Scholiast(test=TEST)

  login()
  comment(
    post_url=POST_URL,
    comment_content=comments,
    interval_minutes=TIME_INTERVAL
  )

main()
```
