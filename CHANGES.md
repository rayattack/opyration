# Version 0.2.2
- Fix: opyration.results no longer throws an error when result data set is `None`

# Version 0.2.1
- Breaking Changes `.first` no longer accepts parameters and executes a fetching request
- New method to execute raw sql `.query(sql: str, *vals)` added to replace `.fetch`

# Version 0.1.4
- Allow raw sql to be passed and raw values i.e. `op.raw('select $1').values(1)`
- Refresh now allows to specify if to refresh with schema or keep schema but refresh op for reuse

# Version 0.1.3
- Add support for OFFSET command

# Version 0.1.2
- Fixed bug with limit not returning instance of Operation

