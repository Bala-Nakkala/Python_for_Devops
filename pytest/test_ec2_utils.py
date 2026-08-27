from ec2_utils import is_instance_running

def test_running_instance():
    assert is_instance_running("running") is True

def test_stopped_instance():
    assert is_instance_running("stopped") is False