"""Exception classes specific to extra_data."""


class SourceNameError(KeyError):
    def __init__(self, source):
        self.source = source

    def __str__(self):
        return (
            "This data has no source named {!r}.\n"
            "See data.all_sources for available sources.".format(self.source)
        )


class PropertyNameError(KeyError):
    def __init__(self, prop, source):
        self.prop = prop
        self.source = source

    def __str__(self):
        return "No property {!r} for source {!r}".format(self.prop, self.source)


class TrainIDError(KeyError):
    def __init__(self, train_id):
        self.train_id = train_id

    def __str__(self):
        return "Train ID {!r} not found in this data".format(self.train_id)


class MultiRunError(ValueError):
    def __str__(self):
        return (
            "The requested data is only available for a single run. This "
            "EXtra-data DataCollection may have data from multiple runs, e.g. "
            "because you have used .union() to combine data. Please retrieve "
            "this information before combining."
        )
