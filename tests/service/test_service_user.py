import pytest

from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        self.service_user = ServiceUser()
        expected_result = "User added"
        result = self.service_user.add_user("Tainah", "Biologa")
        assert result == expected_result

    def test_add_user_empty_name_fail(self):
        self.service_user = ServiceUser()
        expected_result = "Empty parameters not allowed"
        result = self.service_user.add_user("", "Biologa")
        assert result == expected_result

    def test_add_user_empty_job_fail(self):
        self.service_user = ServiceUser()
        expected_result = "Empty parameters not allowed"
        result = self.service_user.add_user("Tainah", "")
        assert result == expected_result

    def test_add_user_invalid_name_fail(self):
        self.service_user = ServiceUser()
        expected_result = "Invalid parameters"
        result = self.service_user.add_user(3, "Biologa")
        assert result == expected_result

    def test_add_user_invalid_job_fail(self):
        self.service_user = ServiceUser()
        expected_result = "Invalid parameters"
        result = self.service_user.add_user("Tainah", 9)
        assert result == expected_result

    def test_update_user_success(self):
        expected_result = "Name updated"
        self.service_user = ServiceUser()
        self.service_user.add_user("Tainah", "Biologa")
        result = self.service_user.update_user("Tainah", "Maria")
        assert result == expected_result

    def test_update_nonexistent_user_fail(self):
        expected_result = "User does not exist"
        self.service_user = ServiceUser()
        self.service_user.add_user("Tainah", "Biologa")
        result = self.service_user.update_user("Jose", "Maria")
        assert result == expected_result

    def test_remove_user_success(self):
        expected_result = "User removed"
        self.service_user = ServiceUser()
        self.service_user.add_user("Tainah", "Biologa")
        result = self.service_user.remove_user("Tainah", "Biologa")
        assert result == expected_result

    def test_remove_user_nonexistent_fail(self):
        expected_result = "User does not exist"
        self.service_user = ServiceUser()
        self.service_user.add_user("Tainah", "Biologa")
        result = self.service_user.remove_user("Andre", "Biologa")
        assert result == expected_result

    def test_get_user_job_success(self):
        expected_result = "QA Engineer"
        self.service_user = ServiceUser()
        self.service_user.add_user("Tainah", "Biologa")
        result = self.service_user.get_user_by_name("Tainah")
        assert result == expected_result




