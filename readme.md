Run `git pull` when web hook is received from Github. Also restart the systemd service that runs the process. All of this is configured using `config.json`, with the format below:

```json
{
    "myrepo": {
        "path": "/path/to/local/myrepo",
        "service": "myrepo.service"
    },
    "another-repository": {
        "path": "/tmp/another-repository",
        "service": "repo.service"
    }
}
```