from app.lib.core import Scholiast

comments = (
  'lorem ipsum', 
  'dolor sit', 
  'amet, consectetur', 
  'adipiscing elit',
)

POST_URL = 'https://www.instagram.com/p/B0MIMm5nX0N/'
TIME_INTERVAL = (10, 12)
TEST=False

def main():
  login, comment = Scholiast(test=TEST)

  login()
  comment(
    post_url=POST_URL,
    comment_content=comments,
    interval_minutes=TIME_INTERVAL
  )

main()
