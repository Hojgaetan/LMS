from models.base_model import BaseModel
from utils.db_utils import DatabaseConnection


class Member(BaseModel):
    """Model class for library members."""

    TABLE_NAME = "members"
    PRIMARY_KEY = "member_id"

    def __init__(
        self,
        member_id=None,
        name=None,
        email=None,
        phone=None,
        address=None,
        registration_date=None,
        password=None,
        member_type=None,
        **kwargs,
    ):
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

    @classmethod
    def count(cls):
        """Count the total number of members."""
        query = f"SELECT COUNT(*) FROM {cls.TABLE_NAME}"
        result = DatabaseConnection.execute_query(query)
        return result[0][0] if result else 0

    @classmethod
    def count_active_members(cls):
        """Count the total number of active members based on recent loans."""
        query = f"""
        SELECT COUNT(DISTINCT m.member_id)
        FROM {cls.TABLE_NAME} AS m
        JOIN loans AS l ON m.member_id = l.member_id
        WHERE l.return_date IS NULL
        """
        result = DatabaseConnection.execute_query(query)
        return result[0][0] if result else 0

    @classmethod
    def get_all(cls):
        """Retrieve all members."""
        query = f"SELECT * FROM {cls.TABLE_NAME}"
        results = DatabaseConnection.execute_query(query)
        if results:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()
            return [cls(**dict(zip(columns, result))) for result in results]
        return []

    @classmethod
    def get_all_members_with_loans(cls):
        """Retrieve all members along with their loans."""
        from models.borrowing import Borrowing

        query = f"SELECT * FROM {cls.TABLE_NAME}"
        results = DatabaseConnection.execute_query(query)

        if results:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({cls.TABLE_NAME})")
            columns = [column[1] for column in cursor.fetchall()]
            conn.close()

            members = [cls(**dict(zip(columns, result))) for result in results]
            for member in members:
                member.loans = Borrowing.find_by_member(member.member_id)
            return members

        return []

    def get_borrowings(self):
        """Get all borrowings by this member."""
        from models.borrowing import Borrowing

        return Borrowing.find_by_member(self.member_id)

    def get_loans(self):
        """Get all loans by this member."""
        from models.borrowing import Borrowing

        return Borrowing.find_by_member(self.member_id)

    def validate(self):
        """Validate the member data."""
        if not self.name:
            return False, "Le nom du membre est obligatoire."

        if not self.email:
            return False, "L'adresse email est obligatoire."

        if not self.phone:
            return False, "Le numéro de téléphone est obligatoire."

        if not self.address:
            return False, "L'adresse est obligatoire."

        # Vérifier si l'email est unique uniquement si c'est un nouveau membre ou si l'email a changé
        if self.email and (not self.member_id or self.email != self._get_attribute("email")):
            existing_member = Member.find_by_email(self.email)
            if existing_member and existing_member.member_id != self.member_id:
                return False, f"Un membre avec l'adresse email {self.email} existe déjà."

        return True, "Les informations du membre sont valides."
