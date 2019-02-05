from haystack.forms import FacetedSearchForm


class FacetedProductSearchForm(FacetedSearchForm):

    def __init__(self, *args, **kwargs):
        data = dict(kwargs.get("data", []))
        self.categorys = data.get('category', [])
        super(FacetedProductSearchForm, self).__init__(*args, **kwargs)

    def search(self):
        sqs = super(FacetedProductSearchForm, self).search()
        if self.categorys:
            query = None
            for category in self.categorys:
                if query:
                    query += u' OR '
                else:
                    query = u''
                query += u'"%s"' % sqs.query.clean(category)
            sqs = sqs.narrow(u'category_exact:%s' % query)
        return sqs