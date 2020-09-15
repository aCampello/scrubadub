.. _api:

API
===

``scrubadub`` consists of three separate components:

* The ``Scrubber`` is responsible for managing all of the ``Detector`` objects
  and resolving any conflicts that may arise between different ``Detector``
  objects.

* ``Detector`` objects are used to detect specific types of ``Filth``.

* ``Filth`` objects are used to identify specific parts of a piece of dirty
  dirty text that contain sensitive information and they are responsible for
  deciding how the resulting information should be replaced in the cleaned
  text.


Scrubber
--------

All of the ``Detector``'s are managed by the ``Scrubber``. The main job of the
``Scrubber`` is to handle situations in which the same section of text contains
different types of ``Filth``.

.. autoclass:: scrubadub.scrubbers.Scrubber
    :members:
    :undoc-members:
    :show-inheritance:


Detectors
---------

``scrubadub`` consists of several ``Detector``'s, which are responsible for
identifying and iterating over the ``Filth`` that can be found in a piece of
text. Every type of ``Filth`` has a ``Detector`` that inherits from
``scrubadub.detectors.base.Detector``:

.. autoclass:: scrubadub.detectors.base.Detector
    :members:
    :undoc-members:
    :show-inheritance:

For convenience, there is also a ``RegexDetector``, which makes it easy to
quickly add new types of ``Filth`` that can be identified from regular
expressions:

.. autoclass:: scrubadub.detectors.base.RegexDetector
    :members:
    :undoc-members:
    :show-inheritance:


Detectors enabled by default
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are the detectors that are enabled in the scrubber by default.

.. autoclass:: scrubadub.detectors.credential.CredentialDetector
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: scrubadub.detectors.email.EmailDetector
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: scrubadub.detectors.name.NameDetector
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: scrubadub.detectors.phone.PhoneDetector
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: scrubadub.detectors.skype.SkypeDetector
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: scrubadub.detectors.ssn.SSNDetector
    :members:
    :undoc-members:
    :show-inheritance:

.. autoclass:: scrubadub.detectors.url.UrlDetector
    :members:
    :undoc-members:
    :show-inheritance:

Filth
-----

Filth objects are responsible for marking particular sections of text as
containing that type of filth. It is also responsible for knowing how it should
be cleaned. Every type of ``Filth`` inherits from `scrubadub.filth.base.Filth`.

.. autoclass:: scrubadub.filth.base.Filth
    :members:
    :undoc-members:
    :show-inheritance:

There is also a convenience class for ``RegexFilth``, which makes it easy to
quickly remove new types of filth that can be identified from regular
expressions:

.. autoclass:: scrubadub.filth.base.RegexFilth
    :members:
    :undoc-members:
    :show-inheritance: