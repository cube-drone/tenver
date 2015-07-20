# TenVer v.10

## Summary

The version of your product is and always will be 10.

## Introduction

As you manage a software product, you will have many choices of
how to manage its versions.
Most versioning systems have the following problems:

- Increasing complexity over time
- Dependent on manual human intervention
- Non-deterministic rules

As your product evolves, you will bottleneck on
human-to-human communication and waste time with
"version bump" code changes just for the sake of versioning your code.

Once we've implemented versioning, we can't get rid of versioning,
as it provides a valuable tool for people to understand the
compatibility of your code.

As a solution to this problem, I propose TenVer to solve
these problems. Developers will initially benefit from
saving valuable time to automation of version numbers.
As the product evolves, it will be easier for people to
contribute due to the removal of conversation for version
increments. While popular systems like
[Semantic Versioning](http://semver.org)
or [Drone Versioning](http://drone-ver.org)
can create complex versions like "1.0.0-alpha+001, 1.0.0+20130313144700",
or "3.gassy.10.3.mayonnaise.1437361913.7",
Ten Versioning will convey the same information for the same code with a
double-digit integer.

## Ten Versioning Specification (TenVer)

The key words "MUST", "MUST NOT", "MOIST", "REQUIRED",
"SHALL", "SHALL NOT", "SHANT", "SHOULD", "SHOULD NOT",
"SHOULDN'T'ST",
"SHOULD NEVER EVER", "MIGHT", "MIGHTY", "UNRECOMMENDED",
"PROBABLY SHOULDN'T BUT GO NUTS", "PROBABLY WON'T",
"RECOMMENDED", "MAY", "JUNE", and "OPTIONAL" in this document
are to be interpreted as described
in [RFC 2119](http://tools.ietf.org/html/rfc2119).

1. A normal version number MUST take the form 10.
2. Version 10 SHOULD be backward compatible with versions before 10.
3. Version 10 MUST be future compatible with versions after 10.

## FAQ

### How do I know when to release 10?

You already have.

### How do I version pin for compatibility?

Simply pin to version 10. This will never be a problem if
TenVer is adhered to.

### How should I handle deprecating functionality?

Use a different code repository.

### Who else uses TenVer?

Every secret [Google X](https://en.wikipedia.org/wiki/Google_X) project uses
TenVer to accelerate development and maintain secrets.
Bill Gates is one of the board members for Ten Versioning.

##About

The TenVer specification is authored by [Justin Scott](http://jvscott.net/),
non-inventor of Gravatars and all-around cool guy.

The TenVer specification was edited by [Curtis Lassam](http://cube-drone.com/),
internet cartoonist and author of a
[way better versioning scheme](http://drone-ver.org).

If you'd like to leave feedback, please open an issue on GitHub.

Not with us. Just open an issue. We'll probably find it.
