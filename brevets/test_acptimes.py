
'''
Nose tests for acp_times.py
'''

import acp_times
import nose
import logging
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

assign_time = arrow.get('2017-01-01T00:00:00+00:00')


def test_acptime_200():
    assert acp_times.open_time(0, 200, assign_time) == '2017-01-01T00:00:00+00:00'
    assert acp_times.close_time(0, 200, assign_time) == '2017-01-01T00:00:00+00:00'
    
    assert acp_times.open_time(100, 200, assign_time) == '2017-01-01T02:56:00+00:00'
    assert acp_times.close_time(100, 200, assign_time) == '2017-01-01T06:40:00+00:00'

    assert acp_times.open_time(200, 200, assign_time) == '2017-01-01T05:53:00+00:00'
    assert acp_times.close_time(200, 200, assign_time) == '2017-01-01T13:20:00+00:00'
    
    assert acp_times.open_time(210, 200, assign_time) == '2017-01-01T06:12:00+00:00'
    assert acp_times.close_time(210, 200, assign_time) == '2017-01-01T14:00:00+00:00'
    print("test cases for Distance = 200")
    ###################################################################################
          
def test_acptime_400():
    assert acp_times.open_time(0, 400, assign_time) == '2017-01-01T00:00:00+00:00'
    assert acp_times.close_time(0, 400, assign_time) == '2017-01-01T00:00:00+00:00'
    
    assert acp_times.open_time(100, 400, assign_time) == '2017-01-01T02:56:00+00:00'
    assert acp_times.close_time(100, 400, assign_time) == '2017-01-01T06:40:00+00:00'

    assert acp_times.open_time(300, 400, assign_time) == '2017-01-01T09:00:00+00:00'
    assert acp_times.close_time(300, 400, assign_time) == '2017-01-01T20:00:00+00:00'
    
    assert acp_times.open_time(420, 400, assign_time) == '2017-01-01T12:48:00+00:00'
    assert acp_times.close_time(420, 400, assign_time) == '2017-01-02T04:00:00+00:00'
    print("test cases for Distance = 400")
    ###################################################################################

def test_acptime_1000():
    assert acp_times.open_time(0, 1000, assign_time) == '2017-01-01T00:00:00+00:00'
    assert acp_times.close_time(0, 1000, assign_time) == '2017-01-01T00:00:00+00:00'
    
    assert acp_times.open_time(200, 1000, assign_time) == '2017-01-01T05:53:00+00:00'
    assert acp_times.close_time(200, 1000, assign_time) == '2017-01-01T13:20:00+00:00'

    assert acp_times.open_time(800, 1000, assign_time) == '2017-01-02T01:57:00+00:00'
    assert acp_times.close_time(800, 1000, assign_time) == '2017-01-03T09:30:00+00:00'
    
    assert acp_times.open_time(1200, 1000, assign_time) == '2017-01-02T09:38:00+00:00'
    assert acp_times.close_time(1200, 1000, assign_time) == '2017-01-04T00:30:00+00:00'
    print("test cases for Distance = 1000")
    ###################################################################################
    

