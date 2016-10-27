from allauth.socialaccount.models import SocialToken
import facebook
from django.contrib.auth import User

# EAAKwNso7u9UBADq1Roe7zH9Wy6ZBxGySixXzDcGfItC5Qs69qMndb3nhZBW7nZAsjJZCKVmVumBWmPnonacUgD6xdUaDDcgHa7nTJZA1ephIiySWSomC2RS6eZCzvK3LOerqnXezcM7kBJu3TxMdMo1eW20RhFpVUZD
def main():
    user = User.objects.get(id=1)
    tokens = SocialToken.objects.filter(
        account__user=user,
        account__provider='facebook'
    )
    if tokens:
        access_token = tokens[0].token
        graph = facebook.GraphAPI(access_token=access_token, version='2.2')
        print(graph)
