import requests
#http://rahulshetty.com
# 'visit-month'
# If I need to send any cookie to site. I need to send it in dictionary format.
cookie= {'visit-month':'February'}
response=requests.get('http://rahulshettyacademy.com',allow_redirects=False, cookies=cookie, timeout=1)
#redirection and timeout. The concept in API testing calls.
#Before hitting rahulshettyacademy, there is a redirection happening.
# If there is redirection happening, the response will be 302.
# If I use response.status_code, I will be able to see the final and latest status code, not the past one.
# Redirection is very common, if there is any security implementation if any.
# I can still get the history by using the below command.
# The requirement is to validate there is no redirection. In that case we can use allow_redirects=False.
# If there is redirection in the end point or base url. The request will be stopped and it will not proceed further.
# There are some response which will take more than 2 or 3 seconds based on the load. In that case we need to use the timeout statement
print(response.history)
print(response.status_code)

response= requests.get("https://httpbin.org/cookies",cookies={'visit-month':'2021 Sepetember 15'})
print(response.status_code)
print(response.text)