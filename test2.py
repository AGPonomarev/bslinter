# Copyright 2019 Tsukanov Alexander. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import List, Optional

from md.base import XMLParser
import md.conf as cf
from md.visitor import Plugin, Visitor

class TestPlugin(Plugin):

    def __init__(self):

        self.errors: List[str] = []

    def result(self) -> str:
        return '\n'.join(self.errors)

    def beforeVisitLocalStringTypeItem(self, node: cf.LocalStringTypeItem):
        self.errors.append(f'Синоним для языка {node.lang} = {node.content}')


path = 'C:/temp/ERP/Configuration.xml'
root = XMLParser(path, cf.Root).parse()
plugins = [TestPlugin()]
v = Visitor(plugins)
mdo: Optional[cf.MetaDataObject] = root.MetaDataObject
if mdo is not None and mdo.Configuration is not None:
    mdo.Configuration.__path__ = path
    mdo.Configuration.walk(v)
    print(plugins[0].result())