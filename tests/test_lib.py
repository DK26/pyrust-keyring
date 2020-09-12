import unittest
from uuid import uuid4
import rskeyring


def generate_password():
    return str(uuid4())


class RSKeyringTests(unittest.TestCase):

    service_name = "rskeyring_unit_test_service_name"
    username = "rskeyring_unit_test_username"

    def test_set_password(self):

        rskeyring.set_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username,
            password=generate_password()
        )

    def test_update_password(self):

        first_password = generate_password()

        rskeyring.set_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username,
            password=first_password
        )

        stored_password = rskeyring.get_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username
        )

        self.assertEqual(first_password, stored_password)

        second_password = generate_password()

        rskeyring.set_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username,
            password=second_password
        )

        stored_password = rskeyring.get_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username
        )

        self.assertEqual(second_password, stored_password)

    def test_get_password(self):

        generated_password = generate_password()

        rskeyring.set_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username,
            password=generated_password
        )

        stored_password = rskeyring.get_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username
        )

        self.assertEqual(stored_password, generated_password)

    def test_delete_password(self):

        generated_password = generate_password()

        rskeyring.set_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username,
            password=generated_password
        )

        stored_password = rskeyring.get_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username
        )

        self.assertEqual(stored_password, generated_password)

        rskeyring.delete_password(
            service=RSKeyringTests.service_name,
            username=RSKeyringTests.username
        )

        with self.assertRaises(OSError):

            rskeyring.get_password(
                service=RSKeyringTests.service_name,
                username=RSKeyringTests.username
            )

    def test_exceptions(self):

        random_user_name = 'rskeyring_unittest_' + generate_password()

        with self.assertRaises(OSError):
            rskeyring.get_password(
                service=RSKeyringTests.service_name,
                username=random_user_name
            )

        with self.assertRaises(OSError):
            rskeyring.delete_password(
                service=RSKeyringTests.service_name,
                username=random_user_name
            )


if __name__ == '__main__':
    unittest.main()
