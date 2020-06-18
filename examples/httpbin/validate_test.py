# NOTE: Generated By HttpRunner v3.0.13
# FROM: examples/httpbin/validate.yml

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseValidate(HttpRunner):
    config = Config("basic test with httpbin").base_url("http://httpbin.org/")

    teststeps = [
        Step(
            RunRequest("validate response with json path")
            .get("/get")
            .with_params(**{"a": 1, "b": 2})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.args.a", "1")
            .assert_equal("body.args.b", "2")
        ),
        Step(
            RunRequest("validate response with python script")
            .get("/get")
            .with_params(**{"a": 1, "b": 2})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseValidate().test_start()
