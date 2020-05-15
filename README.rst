****************************
Mopidy-SaveStatePeriod
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-SaveStatePeriod
    :target: https://pypi.org/project/Mopidy-SaveStatePeriod/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/circleci/build/gh/konubinix/mopidy-savestateperiod
    :target: https://circleci.com/gh/konubinix/mopidy-savestateperiod
    :alt: CircleCI build status

.. image:: https://img.shields.io/codecov/c/gh/konubinix/mopidy-savestateperiod
    :target: https://codecov.io/gh/konubinix/mopidy-savestateperiod
    :alt: Test coverage

Save the state periodically to avoid loosing the state after a power outage


Installation
============

Install by running::

    python3 -m pip install Mopidy-SaveStatePeriod

See https://mopidy.com/ext/savestateperiod/ for alternative installation methods.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-SaveStatePeriod to your Mopidy configuration file::

    [savestateperiod]
    period = <number of seconds to refresh the state>


Project resources
=================

- `Source code <https://github.com/konubinix/mopidy-savestateperiod>`_
- `Issue tracker <https://github.com/konubinix/mopidy-savestateperiod/issues>`_
- `Changelog <https://github.com/konubinix/mopidy-savestateperiod/blob/master/CHANGELOG.rst>`_


Credits
=======

- Original author: `Samuel Loury <https://github.com/konubinix>`__
- Current maintainer: `Samuel Loury <https://github.com/konubinix>`__
- `Contributors <https://github.com/konubinix/mopidy-savestateperiod/graphs/contributors>`_
