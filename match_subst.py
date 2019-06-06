import re


def change(s, prog, version):

    # parse the input and Remove the lines containing "Corporation" and "Level" completely.
    parsed = {i.split(":")[0]: i.split(":")[1] for i in s.replace(": ", ":").splitlines()
              if i.split(":")[0] not in ['Corporation', 'Level']}

    # check if phone and version valid
    if not (re.fullmatch('^\d+\.\d+$', parsed["Version"]) and re.fullmatch('^\+1-\d{3}-\d{3}-\d{4}$', parsed["Phone"])):
        return "ERROR: VERSION or PHONE"

    return "Program: {program} Author: {author} Phone: +1-503-555-0090 Date: 2019-01-01 Version: {version}".format(
                program=prog,
                author='g964',
                version=(version, '2.0')[parsed['Version'] == '2.0']
            )


s1 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0091\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'
s11 = 'Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-0090\nDate: Tues March 29, 2017\nVersion: 2.0\nLevel: Release'
s12 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-009\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'

print(change(s12, 'Balance', '1.1'))

"""
		Test.assert_equals(change(s1, 'Ladder', '1.1'), 'Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1')
		Test.assert_equals(change(s11, 'Balance', '1.5.6'), 'Program: Balance Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 2.0')
		Test.assert_equals(change(s12, 'Ladder', '1.1'), 'ERROR: VERSION or PHONE')

The function change(s, prog, version) given:

s=data, prog="Ladder" , version="1.1" will return:

"Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1"

Rules:

The date should always be "2019-01-01".

The author should always be "g964".

Replace the current "Program Title" with the prog argument supplied to your function. Also remove "Title", so in the example case "Program Title: Primes" becomes "Program: Ladder".

Remove the lines containing "Corporation" and "Level" completely.

Phone numbers and versions must be in valid formats.

A valid version in the given string data is one or more digits followed by a dot, followed by one or more digits. So 0.6, 5.4, 14.275 and 1.99 are all valid, but versions like .6, 5, 14.2.7 and 1.9.9 are invalid.

A valid phone format is +1-xxx-xxx-xxxx, where each x is a digit.

If the phone or version format is not valid, return "ERROR: VERSION or PHONE".

If the version format is valid and the version is anything other than 2.0, replace it with the version parameter supplied to your function. If it’s 2.0, don’t modify it.

If the phone number is valid, replace it with "+1-503-555-0090".



"""