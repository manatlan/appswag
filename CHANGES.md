## Changes

### 0.9.4

- now, compatible with python 3.10, and unittests compliant for 3.7, 3.8, 3.9, "3.10"
- only compat with pyyaml < 6.0 (but will be fixed soon)

### 0.9.3

- add register mime codec 'application/ate.error+json' (thanks @atchoum31)

### 0.9.2

- unquote local uri path


### 0.9.1 

- add register mime codec application/hal+json

### 0.9.0 (first version after the fork)

- first release as a real clone pyswagger -> appswag
- add .allprops on "BaseObj" to let all props be visible

### 0.8.39

- Fix the issue that case insensitive keys in headers not working

### 0.8.38

- Allow to access headers with case insensitive keys
- Drop support to py3.3 because of Tornado

### 0.8.37

- Fix loading error on 'yaml' document
- Fix parameter renderer failed on int/number without 'format'
- Windows Support

### 0.8.33

- Support customized headers when making requests

### 0.8.17

- (not support anymore) implicit dereferencing, which is conflict with 'relative file reference'
  ```json
  "definitions":{
    "User":{
    },
    "AuthorizedUser":{
      "$ref": "User"   --> deferenced to "#/definitions/User"
    }
  }
  ```
- __NEW__ relative file reference
  ```
  "definitions":{
    "User": {
      "$ref": "other_folder/User.json"
    }
  }
  ```
- __NEW__ the root object of external documents can be any object (need to be an Swagger/PathItem object before this version)
- fix issue: use 'netloc' only when no host provided.
