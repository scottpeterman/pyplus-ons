from pathlib import Path
import pytest
import subprocess

TEST_CASES = [
    # Skip modules tests
    # "../day3/modules/solutions/exercise1/exercise1.py",
    # "../day3/modules/solutions/exercise2/__init__.py",
    # "../day3/modules/solutions/exercise2/mod1.py",
    # "../day3/modules/solutions/exercise2/mod2.py",
    # "../day3/modules/solutions/exercise2/mod3.py",
    # Skip linting tests
    # "../day3/linting/solutions/exercise1_pylint.py",
    # "../day3/linting/solutions/devices.py",
    # "../day3/linting/solutions/exercise1_pep8.py",
    # "../day3/linting/solutions/exercise2.py",
    "../day3/parsers/solutions/exercise2.py",
    "../day3/parsers/solutions/exercise3.py",
    "../day3/parsers/solutions/exercise4.py",
    "../day3/serialization/solutions/exercise1.py",
    "../day3/serialization/solutions/exercise2.py",
    "../day3/serialization/solutions/exercise3.py",
    "../day3/data_struct/solutions/exercise1.py",
    "../day3/api/solutions/exercise1.py",
    "../day3/api/solutions/exercise2.py",
    "../day3/nxapi/solutions/exercise1.py",
    "../day3/nxapi/solutions/exercise2.py",
    "../day3/recap/solutions/exercise1.py",
]


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


def test_parsers_ex1():
    """
    Execute textfsm.py:

    $ textfsm.py exercise1.tpl ex1_show_int_status.txt
    """
    cmd_list = ["textfsm.py", "exercise1.tpl", "ex1_show_int_status.txt"]
    script_dir = "../day3/parsers/solutions/"
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    assert return_code == 0
    assert std_err == ""


@pytest.mark.parametrize("test_case", TEST_CASES)
def test_runner(test_case):
    path_obj = Path(test_case)
    python_script = path_obj.name
    script_dir = path_obj.parents[0]
    cmd_list = ["python", python_script]
    std_out, std_err, return_code = subprocess_runner(cmd_list, script_dir)
    assert return_code == 0
    assert std_err == ""
