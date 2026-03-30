'''
# Python PIP

##  1. What is PIP?
* **PIP** is a **package manager for Python packages (modules)**
* It is used to:
  * Install libraries
  * Manage dependencies
  * Update/remove packages

 Note:
* PIP is **included by default in Python 3.4+** 

##  2. What is a Package?
* A **package** is a collection of files used as a module
* It contains:
  * Python code
  * Libraries
  * Dependencies

Packages help reuse code in projects 

##  3. Check if PIP is Installed
```bash
pip --version
```
* Shows installed version of pip
* If not installed → need to install manually 

##  4. Install a Package
```bash
pip install package_name
```
 Example:
```bash
pip install camelcase
```
* Downloads and installs the package 

##  5. Uninstall a Package

```bash
pip uninstall package_name
```
 Example:
```bash
pip uninstall camelcase
```
 Removes installed package 

## 9. Useful PIP Commands

| Command         | Description             |
| --------------- | ----------------------- |
| `pip install`   | Install package         |
| `pip uninstall` | Remove package          |
| `pip list`      | Show installed packages |
| `pip show`      | Show package details    |
| `pip --version` | Check version           |

'''

##  1. Check if PIP is installed
pip --version

## 2. Install a package
pip install requests

## 3. Use installed package
import requests
res = requests.get("https://api.github.com")
print(res.status_code)

##  4. List all installed packages
pip list

##  5. Show details of a package
pip show requests

##  6. Uninstall a package
pip uninstall requests

##  7. Install specific version
# pip install requests==2.28.1

##  8. Upgrade a package
# pip install --upgrade requests

##  9. Install multiple packages
# pip install numpy pandas matplotlib

##  10. Install from requirements file
# pip install -r requirements.txt
