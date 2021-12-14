## References
* https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
* https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14
* https://docs.python-requests.org/en/latest/

```python
from Mydoit import read, write

# Write and Read from file
write("./myFile.txt", data="One\nBrown\nFox")
read("./myFile.txt").text() # return string
read("./myFile.txt").show() # print

# Read from HTTP
read("https://httpbin.org/get").text()
read("https://httpbin.org/get").show() # show formatted and color coded text
write("https://httpbin.org/post", data={"foo":"bar"})  # Write with data defaults to POST
write("https://httpbin.org/put", data={"foo":"bar"}, options={"httpMethod": "PUT"}) 
```

## TODO
- [x] Find out a project with good API structure to model this project on (see `requests` in references)
- [x] Find out out to publish this library as a Python public repository (see `requests` in references)
- [x] Create HttpComponent supporting GET POST, PUT as Producer
- [ ] Color highlight `.show()` 
- [ ] Create project in Github with do.read() and do.write()
- [ ] CI using Travis CI (as per second reference)
- [ ] Publish v0.1 (hello world) to Python public repository