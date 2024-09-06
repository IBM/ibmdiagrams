# @file data.py
#
# Copyright contributors to the ibmdiagrams project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import _IBMItem
from .colors import Colors

class _Data(_IBMItem):
    def __init__(self, label, sublabel="", icon=""):
        super(_Data, self).__init__(label=label, sublabel=sublabel, 
                                    linecolor=Colors.lines["data"], 
                                    shape="pnode", icon=icon)

class Db2(_Data):
    def __init__(self, label, sublabel=""):
        super(Db2, self).__init__(label, sublabel=sublabel, 
                                  icon="Db2")

class Db2Warehouse(_Data):
    def __init__(self, label, sublabel=""):
        super(Db2Warehouse, self).__init__(label, sublabel=sublabel, 
                                           icon="Db2 Warehouse")

class Cloudant(_Data):
    def __init__(self, label, sublabel=""):
        super(Cloudant, self).__init__(label, sublabel=sublabel, 
                                       icon="Cloudant")

class DataStax(_Data):
    def __init__(self, label, sublabel=""):
        super(DataStax, self).__init__(label, sublabel=sublabel, 
                                       icon="DataStax")

class Elasticsearch(_Data):
    def __init__(self, label, sublabel=""):
        super(Elasticsearch, self).__init__(label, sublabel=sublabel, 
                                            icon="Elasticsearch")

class EnterpriseDB(_Data):
    def __init__(self, label, sublabel=""):
        super(EnterpriseDB, self).__init__(label, sublabel=sublabel, 
                                           icon="EnterpriseDB")

class etcd(_Data):
    def __init__(self, label, sublabel=""):
        super(etcd, self).__init__(label, sublabel=sublabel, 
                                   icon="etcd")

class MongoDB(_Data):
    def __init__(self, label, sublabel=""):
        super(MongoDB, self).__init__(label, sublabel=sublabel, 
                                      icon="Mongo DB")

class MySQL(_Data):
    def __init__(self, label, sublabel=""):
        super(MySQL, self).__init__(label, sublabel=sublabel, 
                                     icon="MySQL")

class PostgreSQL(_Data):
    def __init__(self, label, sublabel=""):
        super(PostgreSQL, self).__init__(label, sublabel=sublabel, 
                                         icon="PostgreSQL")

class Rabbit(_Data):
    def __init__(self, label, sublabel=""):
        super(Rabbit, self).__init__(label, sublabel=sublabel, 
                                     icon="Rabbit")

class Redis(_Data):
    def __init__(self, label, sublabel=""):
        super(Redis, self).__init__(label, sublabel=sublabel, 
                                    icon="Redis")

class Database(_Data):
    def __init__(self, label, sublabel=""):
        super(Database, self).__init__(label, sublabel=sublabel, 
                                       icon="Database")

class EventStreams(_Data):
    def __init__(self, label, sublabel=""):
        super(EventStreams, self).__init__(label, sublabel=sublabel,
                                           icon="Event Streams")

class DataPak(_Data):
    def __init__(self, label, sublabel=""):
        super(DataPak, self).__init__(label, sublabel=sublabel,
                                      icon="Data Pak")

# Aliases
Ds = DataStax
Es = Elasticsearch
En = EnterpriseDB
Et = etcd
Mg = MongoDB
My = MySQL
Ra = Rabbit 
Rd = Redis
DB = Database
