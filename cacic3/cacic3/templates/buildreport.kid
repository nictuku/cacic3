<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<script src="/static/javascript/reports.js" type="text/javascript"></script>
<title>Reports</title>
</head>
<body>
<div id="header">&nbsp;</div>
<div id="main_content">
  ${tform.display ()} <br />
  <script py:if="provides_statistics" type="text/javascript">
    <!--
	link_chkbox_lists ('report_form', 'Report Items', 'Statistics Items', 'update_chkbox_list')
      -->
  </script>
</div>
</body>
</html>
