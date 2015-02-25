# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import time
from ..core import io
from ..lib import elasticbeanstalk
from ..resources.strings import prompts
from . import commonops


def print_events(app_name, env_name, region, follow):
    if follow:
        io.echo(prompts['events.hanging'])
    last_time = None
    while True:
        events = elasticbeanstalk.get_new_events(
            app_name, env_name, None, last_event_time=last_time, region=region
        )

        for event in reversed(events):
            commonops.log_event(event, echo=True)
            last_time = event.event_date

        if follow:
            time.sleep(4)
        else:
            break