/* Takes the names of two CheckBoxList widgets and makes
 * the selected items of the first appear on the second
 */
function link_chkbox_lists (form_name, cbl1_name, cbl2_name, func_name) {
    var form = document.forms[form_name];
    var cbl1 = form[cbl1_name];

    for (var count = 0; count < cbl1.length; count++) {
	var cb = cbl1[count];
	var desc = cb.nextSibling.nextSibling.innerHTML;
	cb.setAttribute('onclick', "javascript:" + func_name + "('" + form_name + "', '" + cbl2_name + "', '" + cb.value + "', '" + desc + "', '" + cb.id + "')");
    }
}

function update_chkbox_list (form_name, cbl_name, value, desc, orig_cb_name) {
    var cbl = $(form_name + '_' + cbl_name);
    var cb_id = form_name + '_' + cbl_name + '_' + value;
    var orig_cb = $(orig_cb_name);

    if (orig_cb.checked == true) {
	var cb = LI({'id':'li_' + value}, 
		    INPUT({'type':'checkbox',
			   'id':cb_id,
			   'value':value,
			   'name':cbl_name}, desc),
		    LABEL({'for':cb_id}, desc));
	cbl.appendChild (cb);
    }
    else {
	var li = $('li_' + value);
	if (li) {
	    removeElement(li);
	}
    }
}