<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>Reports</title>
</head>
<body>
<div id="header">&nbsp;</div>
<div id="main_content">
  <div py:for="report_table in report_tables">
    ${report_table[0].display (report_table[1])}
  </div>
</div>
</body>
</html>
