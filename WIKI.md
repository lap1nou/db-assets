## 📖 Usage

### Credentials
Add a credential:
```
dbassets add creds -u 'Administrator' -p 'Passw0rd!'
```

Add a credential with a hash and a domain:
```
dbassets add creds -u 'Administrator' -p 'Passw0rd!' -H 'FC525C9683E8FE067095BA2DDC971889' -d 'test.local'
```

Add multiple credentials from a CSV file:
```
dbassets add creds --file creds.csv --file-type CSV
```

Get a specific credential in JSON format:
```
dbassets get creds -u 'Administrator' --json
```

Get all credentials in TXT format:
```
dbassets get creds --txt
```

Delete a credential:
```
dbassets del creds -u 'Administrator'
```

### Hosts
Add a host:
```
dbassets add hosts --ip '127.0.0.1'
```

Add a host with a hostname and a role:
```
dbassets add hosts --ip '127.0.0.1' -n 'dc.test.local' -r 'DC'
```

Add multiple hosts from a CSV file:
```
dbassets add hosts --file hosts.csv --file-type CSV
```

Get a specific host in JSON format:
```
dbassets get hosts --ip '127.0.0.1'
```

Get all hosts in CSV format:
```
dbassets get hosts --csv
```

Delete a credential:
```
dbassets del hosts --ip '127.0.0.1'
```