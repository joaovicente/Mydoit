## References
* https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
* https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14
* https://docs.python-requests.org/en/latest/

```python
from Mydoit import Mydoit as do
my_file_content = "One\nBrown\nFox"
do.write(my_file_content, "./myFile.txt")
do.read("./myFile")
```

## TODO
- [x] Find out a project with good API structure to model this project on (see `requests` in references)
- [x] Find out out to publish this library as a Python public repository (see `requests` in references)
- [ ] Create project in Github with do.read() API
- [ ] CI using Travis CI
- [ ] Publish v0.1 (hello world) to Python public repository