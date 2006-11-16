from turbogears.widgets import Widget

class AjaxMultiSelect (Widget):
    #css = [CSSLink(static, "grid.css")]
    fields = None
    template = "<b>LALALALALAL</b>"

    params = ["options"]
    params_doc = {'options' : 'A list of tuples with the options for the ajax select'
                              'field'}
    options = []
