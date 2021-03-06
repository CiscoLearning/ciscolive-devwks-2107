"""
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Kareem Iskander, Lead Tech Advocate, L&C"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


from dnacentersdk import DNACenterAPI
import warnings

dnac_creds = {}
dnac_creds['url'] = 'https://sandboxdnac.cisco.com'
dnac_creds['username'] = 'devnetuser'
dnac_creds['password'] = 'Cisco123!'


if __name__ == '__main__':
    warnings.filterwarnings("ignore")  # this is bad practice and only doing this for live demo cleanliness
    dnac = DNACenterAPI(username=dnac_creds['username'], password=dnac_creds['password'], base_url=dnac_creds['url'], verify=False)
    print("Auth Token: ", dnac.access_token)