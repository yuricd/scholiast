# Scholiast
That's a comment bot for Instagram using Selenium Web Driver.
**Notice:** this repository is for studying purposes only. Be aware of the Instagram's terms of use and their policies.

---

### About
Scholiast was built to perform a set of comments sequentially in a random customized range of time in order to avoid failing responses or blocking.

Currently, Scholiast is resilient when it comes to denied reponses. If a comment request is not successfully done, the script waits, by default, 30min to follow the remaining comment list. Otherwise, comments keep going sequentially within the defined time range.

To run Scholiast, you have to use Firefox Web Driver (default used driver). You can take a version of your preference in the [Mozilla Offical Repo for Geckodriver](https://github.com/mozilla/geckodriver/releases). Make sure you have Mozilla Firefox installed in your machine.

## Usage

`pip install -r requirements.txt`

- As environment variables, you have to define `IGUSER` as your Instagram username and `PASSWORD` as your Instagram password.

- In your Scholiast call, you have to provide the comments to be done in a tuple, the post url and the time interval.

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

# Scholiast will get a random value within the range (min, max) 
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