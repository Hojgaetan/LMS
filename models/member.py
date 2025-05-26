from models.base_model import BaseModel
from utils.db_utils import DatabaseConnection


class Member(BaseModel):
    """Model class for library members."""

    TABLE_NAME = "members"
    PRIMARY_KEY = "member_id"

    def __init__(self, member_id=None, name=None, email=None, phone=None, address=None, registration_date=None, **kwargs):
        """Initialize a Member instance."""
        super().__init__(**kwargs)
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.registration_date = registration_date

    @property
    def member_id(self):
        """Get the member ID."""
        return self._get_attribute("member_id")

    @member_id.setter
    def member_id(self, value):
        """Set the member ID."""
        self._set_attribute("member_id", value)

    @property
    def name(self):
        """Get the member name."""
        return self._get_attribute("name")

    @name.setter
    def name(self, value):
        """Set the member name."""
        self._set_attribute("name", value)

    @property
    def email(self):
        """Get the member email."""
        return self._get_attribute("email")

    @email.setter
    def email(self, value):
        """Set the member email."""
        self._set_attribute("email", value)

    @property
    def phone(self):
        """Get the member phone."""
        return self._get_attribute("phone")

    @phone.setter
    def phone(self, value):
        """Set the member phone."""
        self._set_attribute("phone", value)

    @property
    def address(self):
        """Get the member address."""
        return self._get_attribute("address")

    @address.setter
    def address(self, value):
        """Set the member address."""
        self._set_attribute("address", value)

    @property
    def registration_date(self):
        """Get the member registration date."""
        return self._get_attribute("registration_date")

    @registration_date.setter
    def registration_date(self, value):
        """Set the member registration date."""
        self._set_attribute("registration_date", value)

    @classmethod
    def find_by_name(cls, name):
        """Find members by name (partial match)."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE name LIKE ?"
        results = DatabaseConnection.execute_query(query, (f"%{name}%",))

        if results:
            # Convert the result tuples to dictionaries using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            return [cls(**dict(zip(columns, result))) for result in results]

        return []

    @classmethod
    def find_by_email(cls, email):
        """Find a member by email."""
        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE email = ?"
        result = DatabaseConnection.execute_query(query, (email,))

        if result and len(result) > 0:
            # Convert the result tuple to a dictionary using column names
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            record_dict = dict(zip(columns, result[0]))
            return cls(**record_dict)

        return None

    def get_borrowings(self):
        """Get all borrowings by this member."""
        from models.borrowing import Borrowing

        return Borrowing.find_by_member(self.member_id)

    def validate(self):
        """Validate the member data."""
        if not self.name:
            return False, "Member name is required"

        if self.email:
            # Check if email is unique
            existing_member = Member.find_by_email(self.email)
            if existing_member and existing_member.member_id != self.member_id:
                return False, f"A member with email {self.email} already exists"

        return True, "Member is valid"
