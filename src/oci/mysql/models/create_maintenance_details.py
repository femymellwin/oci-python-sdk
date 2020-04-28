# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMaintenanceDetails(object):
    """
    The Maintenance Policy for the DB System.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMaintenanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param window_start_time:
            The value to assign to the window_start_time property of this CreateMaintenanceDetails.
        :type window_start_time: str

        """
        self.swagger_types = {
            'window_start_time': 'str'
        }

        self.attribute_map = {
            'window_start_time': 'windowStartTime'
        }

        self._window_start_time = None

    @property
    def window_start_time(self):
        """
        **[Required]** Gets the window_start_time of this CreateMaintenanceDetails.
        The start of the 2 hour maintenance window.

        This string is of the format: \"{day-of-week} {time-of-day}\".

        \"{day-of-week}\" is a case-insensitive string like \"mon\", \"tue\", &c.

        \"{time-of-day}\" is the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero.


        :return: The window_start_time of this CreateMaintenanceDetails.
        :rtype: str
        """
        return self._window_start_time

    @window_start_time.setter
    def window_start_time(self, window_start_time):
        """
        Sets the window_start_time of this CreateMaintenanceDetails.
        The start of the 2 hour maintenance window.

        This string is of the format: \"{day-of-week} {time-of-day}\".

        \"{day-of-week}\" is a case-insensitive string like \"mon\", \"tue\", &c.

        \"{time-of-day}\" is the \"Time\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to zero.


        :param window_start_time: The window_start_time of this CreateMaintenanceDetails.
        :type: str
        """
        self._window_start_time = window_start_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
