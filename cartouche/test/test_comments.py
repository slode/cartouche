import unittest

from cartouche._portability import u

from cartouche.parser import parse_cartouche_text, CartoucheSyntaxError
from cartouche.errors import CartoucheError

class CommentTests(unittest.TestCase):

    def test_comment1(self):
        source = """Fetches rows from a Bigtable.
        This is a continuation of the opening paragraph.

        Retrieves rows pertaining to the given keys from the Table instance
        represented by big_table.  Silly things may happen if
        other_silly_variable is not None.

        Args:
            big_table: An open Bigtable Table instance.
            keys: A sequence of strings representing the key of each table row
                to fetch.
            other_silly_variable (str): Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A dict mapping keys to the corresponding table row data
            fetched. Each row is represented as a tuple of strings. For
            example:

              {'Serak': ('Rigel VII', 'Preparer'),
               'Zim': ('Irk', 'Invader'),
               'Lrrr': ('Omicron Persei 8', 'Emperor')}

            If a key from the keys argument is missing from the dictionary,
            then that row was not found in the table.

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """

        expected = """        Fetches rows from a Bigtable.
        This is a continuation of the opening paragraph.

        Retrieves rows pertaining to the given keys from the Table instance
        represented by big_table.  Silly things may happen if
        other_silly_variable is not None.

        :param big_table: An open Bigtable Table instance.

        :param keys: A sequence of strings representing the key of each table row
                to fetch.

        :param other_silly_variable: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        :type other_silly_variable: str

        :returns: A dict mapping keys to the corresponding table row data
            fetched. Each row is represented as a tuple of strings. For
            example:

              {'Serak': ('Rigel VII', 'Preparer'),
               'Zim': ('Irk', 'Invader'),
               'Lrrr': ('Omicron Persei 8', 'Emperor')}

            If a key from the keys argument is missing from the dictionary,
            then that row was not found in the table.

        :raises:
            IOError - An error occurred accessing the bigtable.Table object.
        """
        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment2(self):
        source = """Determine if all elements in the source sequence satisfy a condition.

        All of the source sequence will be consumed.

        Note: This method uses immediate execution.

        Args:
            predicate: An optional single argument function used to test each
                elements. If omitted, the bool() function is used resulting in
                the elements being tested directly.

        Returns:
            True if all elements in the sequence meet the predicate condition,
            otherwise False.

        Raises:
            ValueError: If the Queryable is closed()
            TypeError: If predicate is not callable.
        """

        expected = """Determine if all elements in the source sequence satisfy a condition.

        All of the source sequence will be consumed.

        .. note::

            This method uses immediate execution.

        :param predicate: An optional single argument function used to test each
                elements. If omitted, the bool() function is used resulting in
                the elements being tested directly.

        :returns: True if all elements in the sequence meet the predicate condition,
            otherwise False.

        :raises:
            * ValueError - If the Queryable is closed()

            * TypeError - If predicate is not callable.
        """
        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment3(self):
        source = """Determine if all elements in the source sequence satisfy a condition.

        All of the source sequence will be consumed.

        Note: This method uses immediate execution.

        Args:
            predicate: An optional single argument function used to test each
                elements. If omitted, the bool() function is used resulting in
                the elements being tested directly.

        Returns:
            True if all elements in the sequence meet the predicate condition,
            otherwise False.

        Raises:
            ValueError: If the Queryable is closed()
            TypeError: If predicate is not callable.
        """

        expected = """Determine if all elements in the source sequence satisfy a condition.

        All of the source sequence will be consumed.

        .. note::

            This method uses immediate execution.

        :param predicate: An optional single argument function used to test each
                elements. If omitted, the bool() function is used resulting in
                the elements being tested directly.

        :returns: True if all elements in the sequence meet the predicate condition,
            otherwise False.

        :raises:
            * ValueError - If the Queryable is closed()

            * TypeError - If predicate is not callable.
        """
        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment4(self):
        source_lines = [u('Determine if all elements in the source sequence satisfy a condition.'),
                        u(''),
                        u('All of the source sequence will be consumed.'),
                        u(''),
                        u('Note: This method uses immediate execution.'),
                        u(''),
                        u('Args:'),
                        u('    predicate: An optional single argument function used to test each'),
                        u('        elements. If omitted, the bool() function is used resulting in'),
                        u('        the elements being tested directly.'),
                        u(''),
                        u('Returns:'),
                        u('    True if all elements in the sequence meet the predicate condition,'),
                        u('    otherwise False.'),
                        u(''),
                        u('Raises:'),
                        u('    ValueError: If the Queryable is closed()'),
                        u('    TypeError: If predicate is not callable.'),
                        u('')]

        expected = """Determine if all elements in the source sequence satisfy a condition.

All of the source sequence will be consumed.

.. note::

    This method uses immediate execution.

:param predicate: An optional single argument function used to test each
        elements. If omitted, the bool() function is used resulting in
        the elements being tested directly.

:returns: True if all elements in the sequence meet the predicate condition,
    otherwise False.

:raises:
    * ValueError - If the Queryable is closed()

    * TypeError - If predicate is not callable.

"""
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment5(self):
        source_lines = [u('An empty Queryable.'),
                        u(''),
                        u('Note: The same empty instance will be returned each time.'),
                        u(''),
                        u('Returns: A Queryable over an empty sequence.'),
                        u('')]

        expected = """An empty Queryable.

.. note::

    The same empty instance will be returned each time.

:returns: A Queryable over an empty sequence.

"""
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment6(self):
        source_lines = [u('A convenience factory for creating Records.'),
                        u(''),
                        u('Args:'),
                        u('    **kwargs: Each keyword argument will be used to initialise an'),
                        u('       attribute with the same name as the argument and the given'),
                        u('       value.'),
                        u(''),
                        u('Returns:'),
                        u('    A Record which has a named attribute for each of the keyword arguments.'),
                        u('')]

        expected = """A convenience factory for creating Records.

:param \*\*kwargs: Each keyword argument will be used to initialise an
       attribute with the same name as the argument and the given
       value.

:returns: A Record which has a named attribute for each of the keyword arguments.

"""
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment7(self):
        source = """Projects each element of a sequence to an intermediate new sequence,
        flattens the resulting sequences into one sequence and optionally
        transforms the flattened sequence using a selector function.

        Note: This method uses deferred execution.

        Args:
            collection_selector: A unary function mapping each element of the
                source iterable into an intermediate sequence. The single
                argument of the collection_selector is the value of an element
                from the source sequence. The return value should be an
                iterable derived from that element value. The default
                collection_selector, which is the identity function, assumes
                that each element of the source sequence is itself iterable.

            result_selector: An optional unary function mapping the elements in
                the flattened intermediate sequence to corresponding elements
                of the result sequence. The single argument of the
                result_selector is the value of an element from the flattened
                intermediate sequence. The return value should be the
                corresponding value in the result sequence. The default
                result_selector is the identity function.

        Returns:
            A Queryable over a generated sequence whose elements are the result
            of applying the one-to-many collection_selector to each element of
            the source sequence, concatenating the results into an intermediate
            sequence, and then mapping each of those elements through the
            result_selector into the result sequence.

        Raises:
            ValueError: If this Queryable has been closed.
            TypeError: If either collection_selector or result_selector are not
                callable.
        """

        expected = """        Projects each element of a sequence to an intermediate new sequence,
        flattens the resulting sequences into one sequence and optionally
        transforms the flattened sequence using a selector function.

        .. note::

            This method uses deferred execution.

        :param collection_selector: A unary function mapping each element of the
                source iterable into an intermediate sequence. The single
                argument of the collection_selector is the value of an element
                from the source sequence. The return value should be an
                iterable derived from that element value. The default
                collection_selector, which is the identity function, assumes
                that each element of the source sequence is itself iterable.

        :param result_selector: An optional unary function mapping the elements in
                the flattened intermediate sequence to corresponding elements
                of the result sequence. The single argument of the
                result_selector is the value of an element from the flattened
                intermediate sequence. The return value should be the
                corresponding value in the result sequence. The default
                result_selector is the identity function.

        :returns: A Queryable over a generated sequence whose elements are the result
            of applying the one-to-many collection_selector to each element of
            the source sequence, concatenating the results into an intermediate
            sequence, and then mapping each of those elements through the
            result_selector into the result sequence.

        :raises:
            * ValueError - If this Queryable has been closed.

            * TypeError - If either collection_selector or result_selector are not
                callable.
        """
        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment8(self):
        source = """A convenience factory for creating Records.

        Args:
            **kwargs: Each keyword argument will be used to initialise an
                attribute with the same name as the argument and the given
                value.

        Returns:
            A Record which has a named attribute for each of the keyword arguments.
        """

        expected = """A convenience factory for creating Records.

        :param \*\*kwargs: Each keyword argument will be used to initialise an
                attribute with the same name as the argument and the given
                value.

        :returns: A Record which has a named attribute for each of the keyword arguments.

"""
        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment9(self):
        source_lines = [u('Parse a single line of a tree to determine depth and node.'),
                        u(''),
                        u('Args:'),
                        u('    This line is missing an argument name.'),
                        u('    '),
                        u('Returns:'),
                        u('    A 2-tuple containing the tree 0 based tree depth as the first'),
                        u('    element and the node description as the second element.'),
                        u(''),
                        u('Raises:'),
                        u('    ValueError: If line does not have the expected form.'),
                        u('')]

        self.assertRaises(CartoucheError, lambda: parse_cartouche_text(source_lines))

    def test_comment10(self):
        source = """
        Execute the command described by concatenating the string function arguments
        with the p4 -s global scripting flag and return the results in a dictionary.

        For example, to run the command::

          p4 -s fstat -T depotFile foo.h

        call::

          p4('fstat', '-T', 'depotFile', 'foo.h')

        Args:
            args: The arguments to the p4 command as a list of objects which will
                be converted to strings.

        Returns:
            A dictionary of lists where each key in the dictionary is the field name
            from the command output, and each value is a list of output lines in
            order.

        Raises:
            PerforceError: If the command could not be run or if the command
                reported an error.
        """

        expected = """
        Execute the command described by concatenating the string function arguments
        with the p4 -s global scripting flag and return the results in a dictionary.

        For example, to run the command::

          p4 -s fstat -T depotFile foo.h

        call::

          p4('fstat', '-T', 'depotFile', 'foo.h')

        :param args: The arguments to the p4 command as a list of objects which will
                be converted to strings.

        :returns: A dictionary of lists where each key in the dictionary is the field name
            from the command output, and each value is a list of output lines in
            order.

        :raises:
            PerforceError - If the command could not be run or if the command
                reported an error.

"""

        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment11(self):
        source = """Projects each element of a sequence to an intermediate new sequence,
        flattens the resulting sequences into one sequence and optionally
        transforms the flattened sequence using a selector function.

        Warning: This method may explode at short notice.

        Args:
            collection_selector: A unary function mapping each element of the
                source iterable into an intermediate sequence. The single
                argument of the collection_selector is the value of an element
                from the source sequence. The return value should be an
                iterable derived from that element value. The default
                collection_selector, which is the identity function, assumes
                that each element of the source sequence is itself iterable.

            result_selector: An optional unary function mapping the elements in
                the flattened intermediate sequence to corresponding elements
                of the result sequence. The single argument of the
                result_selector is the value of an element from the flattened
                intermediate sequence. The return value should be the
                corresponding value in the result sequence. The default
                result_selector is the identity function.

        Returns:
            A Queryable over a generated sequence whose elements are the result
            of applying the one-to-many collection_selector to each element of
            the source sequence, concatenating the results into an intermediate
            sequence, and then mapping each of those elements through the
            result_selector into the result sequence.

        Raises:
            ValueError: If this Queryable has been closed.
            TypeError: If either collection_selector or result_selector are not
                callable.
        """

        expected = """        Projects each element of a sequence to an intermediate new sequence,
        flattens the resulting sequences into one sequence and optionally
        transforms the flattened sequence using a selector function.

        .. warning::

            This method may explode at short notice.

        :param collection_selector: A unary function mapping each element of the
                source iterable into an intermediate sequence. The single
                argument of the collection_selector is the value of an element
                from the source sequence. The return value should be an
                iterable derived from that element value. The default
                collection_selector, which is the identity function, assumes
                that each element of the source sequence is itself iterable.

        :param result_selector: An optional unary function mapping the elements in
                the flattened intermediate sequence to corresponding elements
                of the result sequence. The single argument of the
                result_selector is the value of an element from the flattened
                intermediate sequence. The return value should be the
                corresponding value in the result sequence. The default
                result_selector is the identity function.

        :returns: A Queryable over a generated sequence whose elements are the result
            of applying the one-to-many collection_selector to each element of
            the source sequence, concatenating the results into an intermediate
            sequence, and then mapping each of those elements through the
            result_selector into the result sequence.

        :raises:
            * ValueError - If this Queryable has been closed.

            * TypeError - If either collection_selector or result_selector are not
                callable.
        """
        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment12(self):
        source = """Determine if all elements in the source sequence satisfy a condition.

        All of the source sequence will be consumed.

        Note: This method uses immediate execution.

        Args:
            predicate: An optional single argument function used to test each
                elements. If omitted, the bool() function is used resulting in
                the elements being tested directly.

        Returns:
            True if all elements in the sequence meet the predicate condition,
            otherwise False.

        Raises:
            This is not a proper exception description
        """

        source_lines = source.splitlines()
        self.assertRaises(CartoucheError, lambda: parse_cartouche_text(source_lines))

    def test_comment13(self):
        source = """
        Execute the command described by concatenating the string function arguments
        with the p4 -s global scripting flag and return the results in a dictionary.

        For example, to run the command::

          p4 -s fstat -T depotFile foo.h

        call::

          p4('fstat', '-T', 'depotFile', 'foo.h')

        Args:
            args: The arguments to the p4 command as a list of objects which will
                be converted to strings.

        Yields:
            A dictionary of lists where each key in the dictionary is the field name
            from the command output, and each value is a list of output lines in
            order.

        Raises:
            PerforceError: If the command could not be run or if the command
                reported an error.
        """

        expected = """
        Execute the command described by concatenating the string function arguments
        with the p4 -s global scripting flag and return the results in a dictionary.

        For example, to run the command::

          p4 -s fstat -T depotFile foo.h

        call::

          p4('fstat', '-T', 'depotFile', 'foo.h')

        :param args: The arguments to the p4 command as a list of objects which will
                be converted to strings.

        :returns: A dictionary of lists where each key in the dictionary is the field name
            from the command output, and each value is a list of output lines in
            order.

        :raises:
            PerforceError - If the command could not be run or if the command
                reported an error.

"""

        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        expected_lines = expected.splitlines()
        self.assertEqual(len(actual_lines), len(expected_lines))
        for actual_line, result_line in zip(actual_lines, expected_lines):
            if len(actual_line.strip()) == 0:
                self.assertTrue(len(result_line.strip()) == 0)
            else:
                self.assertEqual(actual_line, result_line)

    def test_comment14(self):
        source = """Create a predicate which performs an identity comparison of its
argument with a value.

Args:
    rhs: (right-hand-side) The value against which the identity test will
    be performed.

Returns:
    A unary predicate function which determines whether its single
    arguments (lhs) has the same identity - that is, is the same object -
    as rhs.
"""
        source_lines = source.splitlines()
        self.assertRaises(CartoucheSyntaxError, lambda: parse_cartouche_text(source_lines))

    def test_comment15(self):
        source = """A well.

        A well represents a borehole which is drilled in order to discover or
        delimit a petroleum deposit and/ or to produce petroleum or water for
        injection purposes, to inject gas, water or other medium, or to map or
        monitor well parameters. A well may have one or several termination points.
        (source: Norwegian Petroleum Directorate)

        domain.rox respects this definition in the model. The Well
        owns its child WellTracks, which in turn own their child Surveys
        and LogRuns.

        Attributes:
            name: The name of the Well, as a string. For each Project, each Well
                must be uniquely named.
            project: The Project that owns the Well.
            rkb_elevation (double): The Rotary Kelly Bushing elevation for
                the well.
            well_track: The well track.
            wellhead: The coordinate location of the wellhead, as a 3-tuple.
                Individual elements of this tuple can be extracted as
                `well.wellhead.x`, `well.wellhead.y`, and `well.wellhead.z`.
        """
        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        pass

    def test_comment16(self):
        source = """The example docstring for the Example class.

        Within this class docstring we can both describe the class, but also
        use an attributes heading to list the attributes we expect the
        instances of the class to have.  There is no specific provision for
        distinguishing between class attributes and instance attributes at
        this point, so you should make that distinction clear in your
        descriptions.

        Attributes:
            fred: This attribute description just runs to a single line.
            shiela: This attribute description is somewhat longer and spans
                 multiple lines. Subsequent lines are indented one further
                 level.
            jim (int): As with function or method docstrings you can
                optionally provide a type in parentheses after the attribute
                name and before the colon which separates the name from the
                description.

            harry: With longer attribute descriptions it can help to separate
                the attributes with blank lines.  This takes up more room in
                the source code but is much easier to read when using the
                help() function.
        """
        source_lines = source.splitlines()
        actual_lines = parse_cartouche_text(source_lines)
        pass