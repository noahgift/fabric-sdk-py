# Copyright arxanfintech.com 2016 All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

from hfc.fabric.chain.chain import Chain

_logger = logging.getLogger(__name__ + ".client")


class Client(object):
    """
        Main interaction handler with end user.
        Client can maintain several chains.
    """

    def __init__(self):
        """ Construct client"""
        self._channels = {}
        self._crypto_suite = None
        self._user_context = None

    def new_channel(self, name):
        """Init a channel instance with given name.

        :param name: The name of chain

        :return: The inited chain instance
        """
        _logger.debug("New a chain with name = {}".format(name))
        if name not in self._channels:
            self._channels[name] = Chain(name)
        return self._channels[name]

    def get_channel(self, name):
        """ Get a channel instance

        :param name: the name of the chain

        :return: Get the chain instance with the name or None
        """
        return self._channels.get(name, None)

    @property
    def crypto_suite(self):
        """Get the crypto suite.

        Returns: The crypto_suite instance or None

        """
        return self._crypto_suite

    @crypto_suite.setter
    def crypto_suite(self, crypto_suite):
        """Set the crypto suite to given one.

        Args:
            crypto_suite: The crypto_suite to use.

        Returns: None

        """
        self._crypto_suite = crypto_suite

    @property
    def user_context(self):
        """Get the user context.

        Returns: The user context or None

        """
        return self._crypto_suite

    @user_context.setter
    def user_context(self, user_context):
        """Set the user context to given one.

        Args:
            user_context: The user_context to use.

        Returns: None

        """
        self._user_context = user_context
