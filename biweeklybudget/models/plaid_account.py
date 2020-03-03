"""
The latest version of this package is available at:
<http://github.com/jantman/biweeklybudget>

################################################################################
Copyright 2020 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of biweeklybudget, also known as biweeklybudget.

    biweeklybudget is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    biweeklybudget is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with biweeklybudget.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/biweeklybudget> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
################################################################################
"""

import logging
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utc import UtcDateTime

from biweeklybudget.models.base import Base, ModelAsDict

logger = logging.getLogger(__name__)


class PlaidAccount(Base, ModelAsDict):

    __tablename__ = 'plaid_accounts'
    __table_args__ = (
        PrimaryKeyConstraint('plaid_id', 'plaid_item_id'),
        {'mysql_engine': 'InnoDB'}
    )

    #: Plaid Account ID - part of composite key
    plaid_id = Column(String(70), nullable=False)

    #: Referenced Plaid Item ID - part of composite key
    plaid_item_id = Column(
        String(70), ForeignKey('plaid_items.item_id'), nullable=False
    )

    #: PlaidItem this PlaidAccount is associated with
    plaid_item = relationship('PlaidItem', uselist=False)

    #: Plaid name for the account
    name = Column(String(70))

    #: Plaid account number mask for this account
    mask = Column(String(20))

    #: Account ID this PlaidAccount is associated with
    account_id = Column(
        Integer, ForeignKey('accounts.id'), nullable=True, unique=True
    )

    #: When this item was last updated
    last_updated = Column(UtcDateTime)

    def __repr__(self):
        return "<PlaidAccount(plaid_id=%s, name='%s')>" % (
            self.plaid_id, self.name
        )
