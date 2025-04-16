
# LGED

LGED app for 
* LGED project management
* Project Wise Spending Entry
* Payment Entry
* Project Wise Bill Entry
* Automatic keep track on project wise spending, Bill, Bank Balance etc.

Note: This app is familiar Frappe version-15 or later.




## Demo

[Demo](https://lged.zinyecloud.com)

Login Details: 
username: 
password:


## Installation

Clone App:
```bash
  bench get-app https://github.com/nazmulfx/lged.git
```
Create a new site
```bash
  bench new-site lged.local
```
Install app into lged.local site
```bash
  bench --site lged.local install-app lged
```

Run site
```bash
  bench --site lged.local add-to-hosts
  or 
  bench use lged.local
```
Restart the bench
```bash
  bench start
```

visit on browser lged.local:8000 or 127.0.0.1:8000

## License

[MIT](https://choosealicense.com/licenses/mit/)