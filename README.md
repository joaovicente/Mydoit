## References
* https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
* https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14
* https://docs.python-requests.org/en/latest/

```python
from Mydoit import read, write
my_file_content = "One\nBrown\nFox"
write(my_file_content, "./myFile.txt")
read("./myFile.txt")
```

## TODO
- [x] Find out a project with good API structure to model this project on (see `requests` in references)
- [x] Find out out to publish this library as a Python public repository (see `requests` in references)
- [ ] Create project in Github with do.read() and do.write()
- [ ] CI using Travis CI (as per second reference)
- [ ] Publish v0.1 (hello world) to Python public repository